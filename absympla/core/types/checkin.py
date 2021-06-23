from datetime import datetime


class Checkin(object):
    __data = {}

    def __init__(self, **kwargs):
        self.__data = {**kwargs}

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def id(self) -> int:
        return self.data.get("id")

    @property
    def checkin_in(self) -> bool:
        return self.data.get("check_in", True)

    @property
    def check_in_date(self) -> datetime:
        check_in_date = self.data.get("check_in_date")
        assert check_in_date.strip() != ""
        return datetime.fromisoformat(check_in_date)
