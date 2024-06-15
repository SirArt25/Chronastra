from datetime import datetime
import uuid


class Event:
    def __init__(self,*, is_all_day: bool, start_date: datetime, end_date: datetime, title: str,
                 url: str = None, group_id: str = None, resource_id: str = None):
        self._id = str(uuid.uuid4())
        self._is_all_day = is_all_day
        self._start_date = start_date
        self._end_date = end_date
        self._title = title
        self._url = url
        self._group_id = group_id
        self._resource_id = resource_id

    def set_all_day(self, is_all_day: bool):
        self._is_all_day = is_all_day

    def is_all_day(self) -> bool:
        return self._is_all_day

    def set_start_date(self, start_date: datetime):
        self._start_date = start_date

    def get_start_date(self) -> datetime:
        return self._start_date

    def set_end_date(self, end_date: datetime):
        self._end_date = end_date

    def get_end_date(self) -> datetime:
        return self._end_date

    def set_title(self, title: str):
        self._title = title

    def get_title(self) -> str:
        return self._title

    def set_url(self, url: str):
        self._url = url

    def get_url(self) -> str:
        return self._url

    def get_id(self) -> str:
        return self._id

    def set_group_id(self, group_id: str):
        self._group_id = group_id

    def get_group_id(self) -> str:
        return self._group_id

    def set_resource_id(self, resource_id: str):
        self._resource_id = resource_id

    def get_resource_id(self) -> str:
        return self._resource_id
