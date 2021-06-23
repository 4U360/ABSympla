from datetime import datetime
from enum import Enum
from decimal import Decimal


class RequestStatus(Enum):
    PENDING = 'P'
    APPROVED = 'A'
    NOT_APPROVED = 'NA'
    NOT_PAID = 'NP'
    REQUEST_FOR_REFUND = 'R'
    CANCELLED = 'C'


class RequestTransactionType(Enum):
    CREDIT_CARD = "CREDIT_CARD"
    BOLETO_BANCARIO = 'BOLETO_BANCARIO'
    DEBITO_ONLINE = 'DEBITO_ONLINE'
    DEBIT_CARD = 'DEBIT_CARD'
    FREE = 'FREE'
    MANUAL = 'MANUAL'
    PAYPAL = 'PAYPAL'
    PDV = 'PDV'


class Request(object):
    __data = {}

    def __init__(self, **kwargs):
        self.__data = {**kwargs}

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def id(self) -> str:
        return self.data.get('id', "")

    @property
    def event_id(self) -> int:
        return self.data.get("event_id")

    @property
    def order_date(self) -> datetime:
        order_date = self.data.get("order_date", "")
        assert order_date.strip() != ""
        return datetime.strptime(order_date, '%Y-%m-%d %H:%M:%S')

    @property
    def updated_date(self) -> datetime:
        updated_date = self.data.get("updated_date", "")
        assert updated_date.strip() != ""
        return datetime.strptime(updated_date, '%Y-%m-%d %H:%M:%S')

    @property
    def discount_code(self) -> str:
        return self.data.get("discount_code", "")

    @property
    def transaction_type(self) -> str:
        return self.data.get("transaction_type", "")

    @property
    def transaction_type_object(self) -> RequestTransactionType:
        return RequestTransactionType(self.transaction_type)

    @property
    def order_total_sale_price(self) -> float:
        return self.data.get("order_total_sale_price", 0)

    @property
    def order_total_sale_price_decimal(self) -> Decimal:
        return Decimal(self.order_total_sale_price)

    @property
    def buyer_first_name(self) -> str:
        return self.data.get("buyer_first_name", "")

    @property
    def buyer_last_name(self) -> str:
        return self.data.get("buyer_last_name", "")

    @property
    def buyer_email(self) -> str:
        return self.data.get("buyer_email", "")

    @property
    def invoice_info(self) -> dict:
        return self.data.get("invoice_info")

    @property
    def order_status(self) -> str:
        return self.data.get("order_status", "")

    @property
    def order_status_object(self) -> RequestStatus:
        return RequestStatus(self.order_status)
