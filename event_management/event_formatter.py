from typing import Dict
from datetime import datetime
from event_management.event import Event


class EventFormatter:
    @staticmethod
    def to_skit_lean(event: Event) -> Dict:
        return {
            'title': event.get_title(),
            'start': event.get_start_date(),
            'end': event.get_end_date()
        }

    @staticmethod
    def to_outlook(event: Event):
        # Implementation for Outlook format conversion goes here
        pass  # Placeholder implementation, adjust as needed
