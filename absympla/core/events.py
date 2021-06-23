from .api_router import SymplaAPIRouter
from .types.event import Event
from ..log import get_logger
from typing import Iterator


class SymplaEvents(SymplaAPIRouter):
    ROUTES = {
        "list_events": "/public/v3/events",
        "get_event": "/public/v3/events/{}"
    }
    logger = get_logger(__name__)

    def get_event(self, event_id: str) -> Event:
        self.logger.info(f'Reading event ({event_id}) info')
        handler = self.get(url=self.ROUTES["get_event"].format(event_id))
        handler.raise_for_status()
        response = handler.json()
        return Event(**response.get("data"))

    def list_events(self) -> Iterator[Event]:
        has_next = True
        page = 1

        while has_next:
            self.logger.info(f'Reading list_events page ({page})')

            handler = self.get(url=self.ROUTES["list_events"], params={
                "page": page
            })
            handler.raise_for_status()

            response = handler.json()

            sorting_field = response.get("sort", {}).get("field_sort", "unknown")
            sorting_method = response.get("sort", {}).get("sort", "ASC")
            self.logger.info(f'Sorting by: {sorting_field} ({sorting_method})')

            has_next = response.get("pagination", {}).get("has_next", False)

            self.logger.info(f"Has next: {'yes' if has_next else 'no'}")

            for event_info in response.get("data"):
                yield Event(**event_info)

            page += 1

        self.logger.info(f'list_of_events has come to an end')
