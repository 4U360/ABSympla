from decimal import Decimal
from collections import namedtuple
from typing import Iterator

CustomForm = namedtuple('CustomForm', ["id", "name", "value"])

class Participant(object):
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
    def order_id(self) -> str:
        return self.data.get("order_id")

    @property
    def first_name(self) -> str:
        return self.data.get("first_name", "")

    @property
    def last_name(self) -> str:
        return self.data.get("last_name", "")

    @property
    def email(self) -> str:
        return self.data.get("email", "")

    @property
    def ticket_number(self) -> str:
        return self.data.get("ticket_number", "")

    @property
    def ticket_num_qr_code(self) -> str:
        return self.data.get("ticket_num_qr_code", "")

    @property
    def ticket_name(self) -> str:
        return self.data.get("ticket_name", "")

    @property
    def pdv_user(self) -> str:
        return self.data.get("pdv_user", "")

    @property
    def ticket_sale_price(self) -> float:
        return self.data.get("ticket_sale_price", 0)

    @property
    def ticket_sale_price_decimal(self) -> Decimal:
        return Decimal(self.ticket_sale_price)

    @property
    def checkin(self) -> dict:
        return self.data.get("checkin", {})

    @property
    def custom_form(self) -> Iterator[CustomForm]:
        for form in self.data.get("custom_form", []):
            yield CustomForm(**form)