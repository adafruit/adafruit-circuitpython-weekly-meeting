#!/usr/bin/python3
# Makes the weekly meeting schedule, following some rules:
#  * Recognize a bunch of US-centric holidays and move meeting from Mon -> Tue
#  * Put in special notices when US daylight/standard changes occur
#  * Never hold a meeting from December 23 through December 31 inclusive
import datetime
import sys

import pytz
import icalendar
from holidays.countries.united_states import UnitedStates

from datetime import date
from dateutil.relativedelta import relativedelta as rd, MO, FR, TH, TU
from holidays.constants import JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, \
    OCT, \
    NOV, DEC

class CircuitPythonHoliday(UnitedStates):
    def _populate(self, year):
        super()._populate(year)

        try:
            del self[date(year, OCT, 1) + rd(weekday=MO(+2))]
        except KeyError:
            pass
        self[date(year, OCT, 1) + rd(weekday=MO(+2))] = "Indigenous Peoples' Day"

hols = CircuitPythonHoliday(state='NY')
tz = pytz.timezone('US/Eastern')
meeting_duration = datetime.timedelta(seconds=3600)

def localize(d):
    d = tz.localize(d)
    return d

now = localize(datetime.datetime.now())

def first_monday(year):
    d = datetime.datetime(year, 1, 2, 14)
    while d.weekday() != 0:
        d += datetime.timedelta(days=1)
    return d

def add_holiday_notice(calendar, d, note):
    d = localize(d)
    event = icalendar.Event()
    event.add('summary', note + ' -- Meeting Postponed due to holiday')
    event.add('dtstart', icalendar.vDatetime(d))
    event.add('dtend', icalendar.vDatetime(d + meeting_duration))
    event.add('dtstamp', now)
    calendar.add_component(event)

def add_meeting_notice(calendar, d, note):
    d = localize(d)
    event = icalendar.Event()
    event.add('summary', 'CircuitPython Discord Meeting' + note)
    event.add('dtstart', icalendar.vDatetime(d))
    event.add('dtend', icalendar.vDatetime(d + meeting_duration))
    event.add('dtstamp', icalendar.vDatetime(now))
    if 0:  # This doesn't work, makes google not show the calendar at all
        event.add('conference',
                  'https://adafru.it/discord',
                  parameters= {'VALUE':'URI'})
    calendar.add_component(event)

def make_calendar(calendar, year):
    d0 = first_monday(year)
    olddst = None
    while d0 < datetime.datetime(year, 12, 23):
        d = d0
        hol = hols.get(d, None)
        if hol is not None:
            add_holiday_notice(calendar, d, hol)
            d = d + datetime.timedelta(days=1)
        dst = tz.utcoffset(d)
        if dst != olddst:
            note = '\n(2PM in UTC%+d)' % (
                dst.total_seconds()//3600)
            olddst = dst
        else:
            note = ''
        add_meeting_notice(calendar, d, note)
        d0 += datetime.timedelta(days=7)

if __name__ == "__main__":
    calendar = icalendar.Calendar()
    calendar.add('prodid', '-//circuitpython weekly meeting generator//circuitpython.org//')
    calendar.add('version', '0.0.0-beta0')
    for arg in sys.argv[1:]:
        make_calendar(calendar, int(arg))
    sys.stdout.buffer.write(calendar.to_ical())
