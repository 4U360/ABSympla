from absympla.core.api_router import SymplaAPIRouter
from absympla.log import get_logger
from absympla.core.types.participant import Participant
from typing import Iterator


class SymplaParticipants(SymplaAPIRouter):
    ROUTES = {
        "event_participants": "/public/v3/events/{}/participants"
    }

    logger = get_logger(__name__)

    def event_participants(self, event_id) -> Iterator[Participant]:
        self.logger.info(f'Reading event ({event_id}) participants')
        has_next = True
        page = 1

        while has_next:

            handler = self.get(url=self.ROUTES["event_participants"].format(event_id), params={
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

        self.logger.info(f'event_participants has come to an end')
