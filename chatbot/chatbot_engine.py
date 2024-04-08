from langchain_openai import ChatOpenAI
from typing import Optional
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.language_models import BaseLanguageModel
from utilities.strict_decorator import strict_method
import datetime
import streamlit as st
import os


class ChatBotEngine:
    def __init__(self):
        pass

    def invoke(self, question: str):
        prompt_text = self._template
        prompt_text += question
        return self._llm.invoke(prompt_text).content
    @strict_method
    @st.cache_resource
    def create_engine(self):
        temp = ChatBotEngine()
        temp._initialize_llm()
        temp._initialize_template()
        return temp

    def _initialize_template(self, template: Optional[str] = None):
        if template is None:
            template = """Please organize schedule based only on the tasks listed below. 
            Do not add any tasks that are not included in this list.
            Don't give suggestions for time. Do not include free time on schedule. 
            if duration or end time is given explicitly include it,
            if not set it to 5 minutes. Every task should be one list of strings in python,
            where should be specified start time, end time and title. The time should be interpreted
            in the format of YYYY-MM-DD.Please give a only code. If you don't know the answer,
            just say that you don't know, don't try to make up an answer."""

        self._template = template

    def _initialize_llm(self, llm: Optional[BaseLanguageModel] = None):
        if llm is None:
            if datetime.datetime.now().date() < datetime.date(2023, 9, 2):
                llm_name = "gpt-3.5-turbo-0301"
            else:
                llm_name = "gpt-3.5-turbo"
            llm = ChatOpenAI(model_name=llm_name, temperature=0)
        self._llm = llm
