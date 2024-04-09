import streamlit as st
from chatbot.chatbot_engine import ChatBotEngine
from event_management.events_exporter import EventsExporter
import os


class ChatbotApp:
    __instance = None
    __member_called = {}

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, engine: ChatBotEngine):
        self.__engine = engine

    def show(self):
        # Streamlit UI
        # Custom CSS styles

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'styles', 'text_field.css'), 'r') as f:
            style = f.read()
        st.markdown(
            style,
            unsafe_allow_html=True
        )
        # User input
        user_input: str | None = st.text_input("You:", "")

        if st.button("Send", key="send_button"):
            if user_input:
                bot_response = self.__engine.invoke(schedule=user_input)
                EventsExporter.from_raw_text_to_json(bot_response,
                                                     os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                  '..', '.data'),
                                                     "event.json",
                                                     "event.json")
            else:
                st.warning("Please enter a message.")
