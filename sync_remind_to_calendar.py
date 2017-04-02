#!/usr/bin/env python
#coding=utf-8

import pytz
from datetime import datetime
from pyrfc3339 import generate
from lib.get_remind_note import get_note
from lib.calendar_server import service
from lib.create_events import create_google_event

def timestamp_to_3339_formatted(timestamp):
    timezone = pytz.timezone('Asia/Hong_Kong')
    dt = timezone.localize(datetime.fromtimestamp(timestamp / 1000))
    return generate(dt, utc=False)

def sync_calendar():
    notes = get_note()
    for note in notes:
        title = note.title
        reminderTime = note.attributes.reminderTime
        reminderOrder = note.attributes.reminderOrder
        if not reminderTime:
            reminderTime = reminderOrder

        dateTime = timestamp_to_3339_formatted(reminderTime)
        create_google_event(title, dateTime)


if __name__ == '__main__':
    sync_calendar()