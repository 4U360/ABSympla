from .api_router import SymplaAPIRouter
from ..log import get_logger
from .types.order import Order
from .types.participant import Participant
from typing import Iterator


class SymplaOrders(SymplaAPIRouter):
    ROUTES = {
        "order_by_event": "/public/v3/events/{}/orders",
        "get_order": "/public/v3/events/{}/orders/{}",
        "order_participants": "/public/v3/events/{}/orders/{}/participants"
    }

    logger = get_logger(__name__)

    def event_orders(self, event_id) -> Iterator[Order]:
        self.logger.info(f'Reading event ({event_id}) orders')
        has_next = True
        page = 1

        while has_next:

            handler = self.get(url=self.ROUTES["order_by_event"].format(event_id), params={
                "page": page
            })

            handler.raise_for_status()
            response = handler.json()
            sorting_field = response.get("sort", {}).get("field_sort", "unknown")
            sorting_method = response.get("sort", {}).get("sort", "ASC")
            self.logger.info(f'Sorting by: {sorting_field} ({sorting_method})')

            has_next = response.get("pagination", {}).get("has_next", False)

            self.logger.info(f"Has next: {'yes' if has_next else 'no'}")

            for request_info in response.get("data"):
                yield Order(**request_info)
            page += 1

        self.logger.info(f'event_orders has come to an end')

    def get_request(self, event_id, order_id) -> Order:
        self.logger.info(f'Reading event ({event_id}) order ({order_id})')
        handler = self.get(url=self.ROUTES["get_order"].format(event_id, order_id))
        handler.raise_for_status()
        response = handler.json()
        return Order(**response.get("data"))

    def order_participants(self, event_id, order_id) -> Iterator[Participant]:
        self.logger.info(f'Reading event ({event_id}) order ({order_id}) participants')
        has_next = True
        page = 1

        while has_next:

            handler = self.get(url=self.ROUTES["order_participants"].format(event_id, order_id), params={
                "page": page
            })

            handler.raise_for_status()

            response = handler.json()
            sorting_field = response.get("sort", {}).get("field_sort", "unknown")
            sorting_method = response.get("sort", {}).get("sort", "ASC")
            self.logger.info(f'Sorting by: {sorting_field} ({sorting_method})')

            has_next = response.get("pagination", {}).get("has_next", False)

            self.logger.info(f"Has next: {'yes' if has_next else 'no'}")

            for participant in response.get("data"):
                yield Participant(**participant)

            page += 1

        self.logger.info(f'order_participants has come to an end')
