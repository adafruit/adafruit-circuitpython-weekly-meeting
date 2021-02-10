# Participating in the CircuitPython weekly meeting

Anyone is welcome to participate in the CircuitPython weekly meeting. Please
read our [Code of Conduct](https://github.com/adafruit-circuitpython-weekly-meeting/blob/master/CODE_OF_CONDUCT.md)
before participating to help this project stay welcoming.

The meeting is held in the English language and usually lasts between 60 and 90
minutes.  If you can only attend part of the meeting, that's absolutely fine.

To participate in the meeting, or just attend it live as a listener, join us on
the [Adafruit Discord](https://adafru.it/discord). There is a _#circuitpython_
text channel and a _#circuitpython_ voice channel.

The text from the text channel and the audio from the voice channel are
recorded and uploaded to YouTube and podcast services. Please keep this in
mind if you plan to participate.

If you wish to speak in the meeting, you must ask any Community Moderator to add you to the
_@circuitpythonistas_ role. In this role, you will receive a small number of
notifications each week, almost always related to the meeting. You can mute
these notifications or request to leave the role anytime you like.

While we love to hear the voices of everyone in the community, we also
understand that it doesn't always work out to speak during the
meeting—whether you don't have a microphone, are in a noisy environment, are
simply uncomfortable speaking, or for any other reason—so the host will
read those notes aloud.

We encourage you to listen to a meeting or two before participating, so that
you know better what to expect. You can watch old meetings [on youtube](https://www.youtube.com/watch?v=lvo-seDO4yk&list=PLjF7R1fz_OOUvw7tMv45xjWp0ht8yNgg0)
or listen to them on podcast services. 

# Meeting Sections

The meeting is held in five parts, and in three of the parts (Hug Reports,
Status Updates, and In The Weeds) community members are invited to participate.

## Hug Reports

Hug reports is a time to highlight folks in the CircuitPython community and beyond for doing awesome things, and say thanks.

This section is held as a round-robin, starting with the host and continuing in alphabetical order by Discord handle.

When you give a hug report you'll want to say who you're giving it to and why, such as:

> * I have a hug report for @makermelissa for continuing to work on PortalBase refactoring as well as the libraries that make use of it.

or

> * Thank you to @anecdata and @jerryneedell for helping to identify Socket bugs

## Status Updates

In Status Updates, we want to hear what you have been working on recently and what you plan to work on in the near future.

Just like hug reports, this section is held as a round-robin in alphabetical order.

A typical report might say:

> * Last week:
>   * Worked on an issue where SD cards were not detected
> * This week:
>   * Creating a pull request to fix that bug
>   * Getting back to work on my photo frame project

Small amounts of discussion are appropriate during Status Updates, but if it goes beyond that the host may request that you
discuss it later during In The Weeds.

## In The Weeds

In The Weeds is a section for any longer discussion. Often it's to solicit
community ideas or to find consensus on how to approach an issue. 

> Issue with native busdevice
>
> * See hxxps://github.com/adafruit/circuitpython/issues/4109
>   * Initially filed against LIS3DH library
> * The issue is resolved if native BusDevice is not used.
> * Can also resolve by building with LONGINT_IMPL = MPZ
>   * But then it won’t fit in Flash unless something else is removed.



# Before the meeting

Remember to [check the meeting calendar](https://open-web-calendar.herokuapp.com/calendar.html?url=https%3A%2F%2Fraw.githubusercontent.com%2Fadafruit%2Fadafruit-circuitpython-weekly-meeting%2Fmaster%2Fmeeting.ical&title=CicuitPython%20Weekly%20Meeting%20Schedule&tab=agenda&tabs=month&tabs=agenda).
The meeting is usually every Monday at 1PM [US Eastern Time (UTC-0400 or UTC-0500)](https://en.wikipedia.org/wiki/Eastern_Time_Zone),
but we sometimes change the schedule for US holidays and other special events.
If you're outside the US remember that the dates for the start and end of your
"summer" time may differ from the rule followed in the US.

Each meeting is accompanied by a notes document in Google Docs. You can find
the link to the meeting document in Discord by looking in the "pinned
messages". Generally the link is made available soon after the previous
meeting is concluded.

If you plan to give Hug Reports, Status Updates, or have an issue to discuss In
The Weeds, you can update the notes doc at any time. For Hug Reports and
Status Updates, please put your notes in alphabetical order, starting with your
Discord handle.

If the host should read your notes, indicate that next to your name, such as:

> @foamyguy (lurking)

> @tannewt (missing meeting)

If you're going to be speaking and don't have time before the meeting to enter
your notes, at least add your Discord handle as a placeholder so that the
host knows to let you have your turn. If for some reason even that's not
possible, ask in the text chat for someone else to add it for you.

Your notes can be terse (they don't have to be full english sentences and
paragraphs) but if the host is going to be reading them make sure they
have enough context that what they say will make sense.

# During the meeting

Join a few minutes before the meeting if you want to check that your audio is working.

Please give the host a few minutes after the start of the hour to arrive.
The Discord meeting starts immediately after an internal Adafruit meeting.

When not actively speaking, please mute your microphone.

In the sections where you will participate, be attentive to the order of the
meeting so that you're ready to un-mute and speak when called on.

If the host accidentally skips you, please send a note in the Discord text chat
to make them aware of it.

## In The Weeds

In The Weeds topics are discussed in the order they appear in the notes document.

If you've brought an In The Weeds topic, the host will introduce you and you will
introduce the topic.  Then, anyone
who is interested in the discussion can unmute and speak freely, or participate
in the text chat as they prefer. At the end of the discussion, anyone who is
going to take action will state so clearly, such as "I will add additional
information to the relevant Issue", "I will fix the bug using the approach we
selected", etc. The person who brought the In The Weeds topic will also
briefly summarise the discussion in the notes document. Please do this
promptly, as the host has to finalize the notes document and upload it to
GitHub shortly after the meeting concludes.
