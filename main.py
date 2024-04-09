import streamlit as st
from chatbot.chatbot_engine import ChatBotEngine
from ui import st_calendar as st_calendarUI
from utilities.env_manipulator import configure_environment
from chatbot.chatbot_app import ChatbotApp
from event_management.events_importer import EventsImporter
import os

if __name__ == "__main__":
    configure_environment()

    st.set_page_config(page_title="calendar App", page_icon="📆")

    events = EventsImporter.from_json(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                   '.data', 'event.json'))
    cal = st_calendarUI.StCalendar(events=events)
    cal.show()

    engine = ChatBotEngine.create_engine()
    chat_bot_app = ChatbotApp(engine)
    chat_bot_app.show()
