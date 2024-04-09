import streamlit as st
from chatbot.chatbot_engine import ChatBotEngine
from utilities.env_manipulator import configure_environment
from chatbot.chatbot_app import ChatbotApp

if __name__ == "__main__":
    configure_environment()
    st.set_page_config(page_title="Chronastra")

    engine = ChatBotEngine.create_engine()
    chat_bot_app = ChatbotApp(engine)
    chat_bot_app.show()
