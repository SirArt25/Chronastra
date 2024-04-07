import json
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List
from event import Event


class EventsImporter:
    @staticmethod
    def from_json(json_file: str) -> List[Event]:
        events = []
        with open(json_file, 'r') as file:
            data = json.load(file)
            for event_data in data:
                event = Event(
                    is_all_day=event_data['is_all_day'],
                    start_date=datetime.fromisoformat(event_data['start_date']),
                    end_date=datetime.fromisoformat(event_data['end_date']),
                    title=event_data['title'],
                    url=event_data['url'],
                    group_id=event_data.get('group_id'),
                    resource_id=event_data.get('resource_id')
                )
                events.append(event)
        return events

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
