import streamlit as st

from streamlit_calendar import calendar

st.set_page_config(page_title="calendar App", page_icon="📆")
#
#mode = st.selectbox(
#    "calendar Mode:",
#    (
#        "daygrid",
#        "timegrid",
#        "timeline",
#        "resource-daygrid",
#        "resource-timegrid",
#        "resource-timeline",
#        "list",
#        "multimonth",
#    ),
#)
#
#events = [
#    {
#        "title": "Event 1",
#        "color": "#FF6C6C",
#        "start": "2024-03-03",
#        "end": "2024-03-05",
#        "resourceId": "a",
#    },
#    {
#        "title": "Event 2",
#        "color": "#FFBD45",
#        "start": "2024-03-01",
#        "end": "2024-03-10",
#        "resourceId": "b",
#    },
#    {
#        "title": "Event 3",
#        "color": "#FF4B4B",
#        "start": "2024-03-20",
#        "end": "2024-03-20",
#        "resourceId": "c",
#    },
#    {
#        "title": "Event 4",
#        "color": "#FF6C6C",
#        "start": "2024-03-23",
#        "end": "2024-03-25",
#        "resourceId": "d",
#    },
#    {
#        "title": "Event 5",
#        "color": "#FFBD45",
#        "start": "2024-03-29",
#        "end": "2024-03-30",
#        "resourceId": "e",
#    },
#    {
#        "title": "Event 6",
#        "color": "#FF4B4B",
#        "start": "2024-03-28",
#        "end": "2024-03-20",
#        "resourceId": "f",
#    },
#    {
#        "title": "Event 7",
#        "color": "#FF4B4B",
#        "start": "2024-03-01T08:30:00",
#        "end": "2024-03-01T10:30:00",
#        "resourceId": "a",
#    },
#    {
#        "title": "Event 8",
#        "color": "#3D9DF3",
#        "start": "2024-03-01T07:30:00",
#        "end": "2024-03-01T10:30:00",
#        "resourceId": "b",
#    },
#    {
#        "title": "Event 9",
#        "color": "#3DD56D",
#        "start": "2024-03-02T10:40:00",
#        "end": "2024-03-02T12:30:00",
#        "resourceId": "c",
#    },
#    {
#        "title": "Event 10",
#        "color": "#FF4B4B",
#        "start": "2024-03-15T08:30:00",
#        "end": "2024-03-15T10:30:00",
#        "resourceId": "d",
#    },
#    {
#        "title": "Event 11",
#        "color": "#3DD56D",
#        "start": "2024-03-15T07:30:00",
#        "end": "2024-03-15T10:30:00",
#        "resourceId": "e",
#    },
#    {
#        "title": "Event 12",
#        "color": "#3D9DF3",
#        "start": "2024-03-21T10:40:00",
#        "end": "2024-03-21T12:30:00",
#        "resourceId": "f",
#    },
#    {
#        "title": "Event 13",
#        "color": "#FF4B4B",
#        "start": "2024-03-17T08:30:00",
#        "end": "2024-03-17T10:30:00",
#        "resourceId": "a",
#    },
#    {
#        "title": "Event 14",
#        "color": "#3D9DF3",
#        "start": "2024-03-17T09:30:00",
#        "end": "2024-03-17T11:30:00",
#        "resourceId": "b",
#    },
#    {
#        "title": "Event 15",
#        "color": "#3DD56D",
#        "start": "2024-03-17T10:30:00",
#        "end": "2024-03-17T12:30:00",
#        "resourceId": "c",
#    },
#    {
#        "title": "Event 16",
#        "color": "#FF6C6C",
#        "start": "2024-03-17T13:30:00",
#        "end": "2024-03-17T14:30:00",
#        "resourceId": "d",
#    },
#    {
#        "title": "Event 17",
#        "color": "#FFBD45",
#        "start": "2024-03-17T15:30:00",
#        "end": "2024-03-17T16:30:00",
#        "resourceId": "e",
#    },
#]
#calendar_resources = [
#    {"id": "a", "building": "Building A", "title": "Room A"},
#    {"id": "b", "building": "Building A", "title": "Room B"},
#    {"id": "c", "building": "Building B", "title": "Room C"},
#    {"id": "d", "building": "Building B", "title": "Room D"},
#    {"id": "e", "building": "Building C", "title": "Room E"},
#    {"id": "f", "building": "Building C", "title": "Room F"},
#]
#
#calendar_options = {
#    "editable": "true",
#    "navLinks": "true",
#    "resources": calendar_resources,
#    "selectable": "true",
#}
#
#if "resource" in mode:
#    if mode == "resource-daygrid":
#        calendar_options = {
#            **calendar_options,
#            "initialDate": "2024-03-01",
#            "initialView": "resourceDayGridDay",
#            "resourceGroupField": "building",
#        }
#    elif mode == "resource-timeline":
#        calendar_options = {
#            **calendar_options,
#            "headerToolbar": {
#                "left": "today prev,next",
#                "center": "title",
#                "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
#            },
#            "initialDate": "2024-03-01",
#            "initialView": "resourceTimelineDay",
#            "resourceGroupField": "building",
#        }
#    elif mode == "resource-timegrid":
#        calendar_options = {
#            **calendar_options,
#            "initialDate": "2024-03-01",
#            "initialView": "resourceTimeGridDay",
#            "resourceGroupField": "building",
#        }
#else:
#    if mode == "daygrid":
#        calendar_options = {
#            **calendar_options,
#            "headerToolbar": {
#                "left": "today prev,next",
#                "center": "title",
#                "right": "dayGridDay,dayGridWeek,dayGridMonth",
#            },
#            "initialDate": "2024-03-01",
#            "initialView": "dayGridMonth",
#        }
#    elif mode == "timegrid":
#        calendar_options = {
#            **calendar_options,
#            "initialView": "timeGridWeek",
#        }
#    elif mode == "timeline":
#        calendar_options = {
#            **calendar_options,
#            "headerToolbar": {
#                "left": "today prev,next",
#                "center": "title",
#                "right": "timelineDay,timelineWeek,timelineMonth",
#            },
#            "initialDate": "2024-03-01",
#            "initialView": "timelineMonth",
#        }
#    elif mode == "list":
#        calendar_options = {
#            **calendar_options,
#            "initialDate": "2024-03-01",
#            "initialView": "listMonth",
#        }
#    elif mode == "multimonth":
#        calendar_options = {
#            **calendar_options,
#            "initialView": "multiMonthYear",
#        }
#
#state = calendar(
#    events=st.session_state.get("events", events),
#    options=calendar_options,
#    custom_css="""
#    .fc-event_management-past {
#        opacity: 0.8;
#    }
#    .fc-event_management-time {
#        font-style: italic;
#    }
#    .fc-event_management-title {
#        font-weight: 700;
#    }
#    .fc-toolbar-title {
#        font-size: 2rem;
#    }
#    """,
#    key=mode,
#)
#
#if state.get("eventsSet") is not None:
#    st.session_state["events"] = state["eventsSet"]

#st.write(state)

#st.markdown("## API reference")
#st.help(calendar)