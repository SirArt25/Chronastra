from typing import Dict
from datetime import datetime
from event import Event
class EventFormatter:
    @staticmethod
    def to_skit_lean(event: Event) -> Dict:
        return {
            'title': event.get_title(),
            'start_time': event.get_start_date().strftime("%Y-%m-%d %H:%M:%S"),
            'end_time': event.get_end_date().strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def to_outlook(event: Event):
        # Implementation for Outlook format conversion goes here
        pass  # Placeholder implementation, adjust as needed
