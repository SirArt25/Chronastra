import json
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List
from event_management.event import Event
import os

class EventsImporter:
    @staticmethod
    def from_json(json_file: str) -> List[Event]:
        if not os.path.exists(json_file):
            return []
        
        if os.path.getsize(json_file) == 0:
            return []

        try:
            events = []
            with open(json_file, 'r') as f:
                data = json.load(f)
                for events_raw in data:
                    for event in events_raw['events']:
                        print(event)
                        print(event['id'])
            return events
        except Exception as e:
            return []

         

    @staticmethod
    def from_xml(xml_file: str) -> List[Event]:
        events = []
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for event_elem in root.findall('event'):
            event = Event(
                is_all_day=bool(event_elem.find('is_all_day').text),
                start_date=datetime.fromisoformat(event_elem.find('start_date').text),
                end_date=datetime.fromisoformat(event_elem.find('end_date').text),
                title=event_elem.find('title').text,
                url=event_elem.find('url').text,
                group_id=event_elem.find('group_id').text if event_elem.find('group_id') is not None else None,
                resource_id=event_elem.find('resource_id').text if event_elem.find('resource_id') is not None else None
            )
            events.append(event)
        return events
