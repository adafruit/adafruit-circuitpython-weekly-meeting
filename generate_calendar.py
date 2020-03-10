#!/usr/bin/python3
# Makes the weekly meeting schedule, following some rules:
#  * Recognize a bunch of US-centric holidays and move meeting from Mon -> Tue
#  * Put in special notices when US daylight/standard changes occur
#  * Never hold a meeting from December 23 through December 31 inclusive
import datetime
import sys

import pytz
import icalendar
from holidays import CountryHoliday

hols = CountryHoliday('US', state='NY')
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

def make_calendar(year):
    c = icalendar.Calendar()
    c.add('prodid', '-//circuitpython weekly meeting generator//circuitpython.org//')
    c.add('version', '0.0.0-beta0')
    d0 = first_monday(year)
    olddst = None
    while d0 < datetime.datetime(year, 12, 23):
        d = d0
        hol = hols.get(d, None)
        if hol is not None:
            add_holiday_notice(c, d, hol)
            d = d + datetime.timedelta(days=1)
        dst = tz.utcoffset(d)
        if dst != olddst:
            note = '\n(1PM in UTC%+d)' % (
                dst.total_seconds()//3600)
            olddst = dst
        else:
            note = ''
        add_meeting_notice(c, d, note)
        d0 += datetime.timedelta(days=7)
    return c
 
if __name__ == "__main__":
    for arg in sys.argv[1:]:
        sys.stdout.buffer.write(make_calendar(int(arg)).to_ical())
