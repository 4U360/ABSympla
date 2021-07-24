from absympla.core.api_router import SymplaAPIRouter
from absympla.log import get_logger
from absympla.core.types.participant import Participant
from typing import Iterator


class SymplaParticipants(SymplaAPIRouter):
    ROUTES = {
        "event_participants": "/public/v3/events/{}/participants",
        "participant_by_id": '/public/v3/events/{}/participants/{}',
        "participant_by_ticket": '/public/v3/events/{}/participants/ticketNumber/{}',
    }

    logger = get_logger(__name__)

    def participant_by_ticker(self, event_id, ticket_number) -> Participant:
        self.logger.info(f'Reading ticket ({ticket_number}) info')
        handler = self.get(url=self.ROUTES["participant_by_ticket"].format(event_id, ticket_number))
        handler.raise_for_status()
        response = handler.json()
        return Participant(**response.get("data"))

    def participant_by_id(self, event_id, participant_id) -> Participant:
        self.logger.info(f'Reading participant ({participant_id}) info')
        handler = self.get(url=self.ROUTES["participant_by_id"].format(event_id, participant_id))
        handler.raise_for_status()
        response = handler.json()
        return Participant(**response.get("data"))

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
