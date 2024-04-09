import streamlit as st
from ui import st_calendar as st_calendarUI
from event_management.events_importer import EventsImporter
import os


st.set_page_config(page_title="Calendar", page_icon="📆")

events = EventsImporter.from_json(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                               '../', '.data', 'event.json'))
cal = st_calendarUI.StCalendar(events=events)
cal.show()