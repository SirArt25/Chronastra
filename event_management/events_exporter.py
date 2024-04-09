import json
import os
import xml.etree.ElementTree as ET
from typing import List
from event_management.event import Event


class EventsExporter:
    @staticmethod
    def to_json(events: List[Event]) -> None:
        event_list = []
        for event in events:
            event_dict = {
                'id': event.get_id(),
                'is_all_day': event.is_all_day(),
                'start_date': event.get_start_date().isoformat(),
                'end_date': event.get_end_date().isoformat(),
                'title': event.get_title(),
                'url': event.get_url(),
                'group_id': event.get_group_id(),
                'resource_id': event.get_resource_id()
            }
            event_list.append(event_dict)
        with open('events.json', 'w') as json_file:
            json.dump(event_list, json_file, indent=4)

    @staticmethod
    def fill_fields_of_raw_events(raw_events_json):
        # add it before
        return raw_events_json

    @staticmethod
    def from_raw_text_to_json(raw_data, directory, existing_file_name, new_file_name):
        if not os.path.exists(directory):
            os.makedirs(directory)

        existing_file_path = os.path.join(directory, existing_file_name)
        new_file_path = os.path.join(directory, new_file_name)

        if os.path.exists(existing_file_path):
            with open(existing_file_path, 'r') as f:
                existing_data = json.loads(f.read())
        else:
            existing_data = []

        json_data = EventsExporter.fill_fields_of_raw_events(json.loads(raw_data))
        existing_data.append(json_data)

        with open(new_file_path, 'w') as file:
            file.write(json.dumps(existing_data, indent=4))

    @staticmethod
    def to_xml(events: List[Event]) -> None:
        root = ET.Element("events")
        for event in events:
            event_elem = ET.SubElement(root, "event")
            ET.SubElement(event_elem, "id").text = event.get_id()
            ET.SubElement(event_elem, "is_all_day").text = str(event.is_all_day())
            ET.SubElement(event_elem, "start_date").text = event.get_start_date().isoformat()
            ET.SubElement(event_elem, "end_date").text = event.get_end_date().isoformat()
            ET.SubElement(event_elem, "title").text = event.get_title()
            ET.SubElement(event_elem, "url").text = event.get_url()
            ET.SubElement(event_elem, "group_id").text = event.get_group_id() if event.get_group_id() else ""
            ET.SubElement(event_elem, "resource_id").text = event.get_resource_id() if event.get_resource_id() else ""

        tree = ET.ElementTree(root)
        tree.write("events.xml", encoding='utf-8', xml_declaration=True)
