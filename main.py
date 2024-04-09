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

    # events = engine.invoke("""I will wake up at tomorrow 6:00 am.I need a breakfast which takes nearly 30 minutes.
    # After that i need 15 minutes to make my bad and 10 more minuter
    # for dressing.I have a class at the university at 10 am until 15:00. I have to go gym at 19:30.""")
    # print("invoke := ", events)

    events = EventsImporter.from_json(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                   '.data', 'event.json'))
    cal = st_calendarUI.StCalendar(events=events)
    cal.show()

    engine = ChatBotEngine.create_engine()
    chat_bot_app = ChatbotApp(engine)
    chat_bot_app.show()
