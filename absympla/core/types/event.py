from datetime import datetime


class Event(object):
    __data = {}

    def __init__(self, **kwargs):
        self.__data = {**kwargs}

    @property
    def id(self) -> int:
        return self.__data.get("id", -1)

    @property
    def start_date(self) -> datetime:
        start_date = self.__data.get("start_date", "")
        assert start_date.strip() != ""
        return datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')

    @property
    def end_date(self) -> datetime:
        end_date = self.__data.get("end_date", "")
        assert end_date.strip() != ""
        return datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

    @property
    def name(self) -> str:
        return self.__data.get("name", "")

    @property
    def detail(self) -> str:
        return self.__data.get("detail", "")

    @property
    def private_event(self) -> bool:
        return self.__data.get("private_event", True)

    @property
    def published(self) -> bool:
        return self.__data.get("published", True)

    @property
    def cancelled(self) -> bool:
        return self.__data.get("cancelled", False)

    @property
    def image(self) -> str:
        return self.__data.get("image","")

    @property
    def url(self) -> str:
        return self.__data.get("url","")

    @property
    def address(self) -> dict:
        return self.__data.get("address", {})

    @property
    def host(self) -> dict:
        return self.__data.get("host", {})

    @property
    def category_prim(self) -> dict:
        return self.__data.get("category_prim", {})

    @property
    def category_sec(self) -> dict:
        return self.__data.get("category_sec", {})

    @property
    def data(self) -> dict:
        return self.__data