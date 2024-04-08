import streamlit as st
from utilities.logic_error import LogicError
from streamlit_calendar import calendar
import os
import datetime


class StCalendar:
    def __init__(self, *, style: str = None, events: list = None, calendar_resources: list = None,
                 calendar_basic_opts: dict = None, mode_opt: set = None):
        self._initialize_mode_option(mode_opt)

        self._initialize_calendar_style(style=style)

        self._events = events

        self._initialize_calendar_resources(calendar_resources)

        self._initialize_calendar_basic_opts(calendar_basic_opts)

        self._initialize_mapping_of_mods_and_options()

    def show(self):
        self._mode = st.selectbox("calendar Mode:",
                                  self._mode_opt,)

        self._set_current_option()

        self._calendar_wrapper = calendar(
            events=st.session_state.get("events", self._events),
            options=self._current_option,
            custom_css=self._style,
            key=self._mode,
        )

    def _initialize_mapping_of_mods_and_options(self):
        self._mapping_of_mods_and_options = {
            "resource-daygrid": {
                **self._calendar_basic_opts,
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "resourceDayGridDay",
                "resourceGroupField": "building",
            },

            "resource-timeline": {
                **self._calendar_basic_opts,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
                },
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "resourceTimelineDay",
                "resourceGroupField": "building",
            },

            "resource-timegrid":  {
                **self._calendar_basic_opts,
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "resourceTimeGridDay",
                "resourceGroupField": "building",
            },

            "daygrid": {
                **self._calendar_basic_opts,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "dayGridDay,dayGridWeek,dayGridMonth",
                },
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "dayGridMonth",
            },

            "timegrid": {
                **self._calendar_basic_opts,
                "initialView": "timeGridWeek",
            },

            "timeline":  {
                **self._calendar_basic_opts,
                "headerToolbar": {
                    "left": "today prev,next",
                    "center": "title",
                    "right": "timelineDay,timelineWeek,timelineMonth",
                },
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "timelineMonth",
            },

            "list":  {
                **self._calendar_basic_opts,
                "initialDate": datetime.date.today().strftime("%Y-%m-%d"),
                "initialView": "listMonth",
            },

            "multimonth":  {
                **self._calendar_basic_opts,
                "initialView": "multiMonthYear",
            }
        }

    def _set_current_option(self):
         self._current_option = self._mapping_of_mods_and_options[self._mode]


    def _initialize_calendar_basic_opts(self, calendar_basic_opts: dict = None):
        try:
            if calendar_basic_opts is None:
                calendar_basic_opts = {
                    "editable": "true",
                    "navLinks": "true",
                    "resources": self._calendar_resources,
                    "selectable": "true",
                }
            self._calendar_basic_opts = calendar_basic_opts
        except AttributeError:
            raise LogicError("Called _initialize_calendar_basic_opts without any _calendar_resources ")
        self._current_option = self._calendar_basic_opts

    def _initialize_calendar_resources(self, calendar_resources: list = None):
        if calendar_resources is None:
            calendar_resources = [
                {"id": "a", "building": "Building A", "title": "Room A"},
                {"id": "b", "building": "Building A", "title": "Room B"},
                {"id": "c", "building": "Building B", "title": "Room C"},
                {"id": "d", "building": "Building B", "title": "Room D"},
                {"id": "e", "building": "Building C", "title": "Room E"},
                {"id": "f", "building": "Building C", "title": "Room F"},
            ]
        self._calendar_resources = calendar_resources

    def _initialize_mode_option(self, mode_opt: set = None) -> None:
        if mode_opt is None:
            mode_opt = (
                "daygrid",
                "timegrid",
                "timeline",
                "resource-daygrid",
                "resource-timegrid",
                "resource-timeline",
                "list",
                "multimonth",
            )
        self._mode_opt = mode_opt

    def _initialize_calendar_style(self, file_path: str = None, *, style: str = None) -> None:
        if style is not None:
            self._style = style
        else:
            if file_path is None:
                current_directory = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_directory, '..', 'styles', 'calendar.css')
            with open(file_path, 'r') as file:
                self._style = file.read()

    def set_style(self, style: str) -> None:
        self._style = style

    def get_style(self) -> str:
        return self._style

    def set_events(self, events: list) -> None:
        self._events = events

    def get_events(self) -> list:
        return self._events

    def add_event(self, event) -> None:
        self._events.append(event)

    def remove_event(self, event_id: str) -> None:
        self._events = [event for event in self._events if event.get_id() != event_id]

    def get_calendar_opts(self) -> list:
        return self._calendar_opts

    def set_calendar_opts(self, options: list) -> None:
        self._calendar_opts = options

    def add_calendar_opt(self, option) -> None:
        self._calendar_opts.append(option)

    def remove_calendar_opt(self, option_id: str) -> None:
        self._calendar_opts = [option for option in self._calendar_opts if option.get_id() != option_id]

    def get_mode_opt(self) -> str:
        return self._mode_opt

    def set_mode_opt(self, mode_opt: str) -> None:
        self._mode_opt = mode_opt
