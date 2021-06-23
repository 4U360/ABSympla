from absympla.core.api_router import SymplaAPIRouter
from absympla.log import get_logger
from absympla.core.types.participant import Participant
from typing import Iterator


class SymplaAffiliates(SymplaAPIRouter):
    ROUTES = {
        "event_affiliates": "/public/v3/events/{}/affiliates"
    }

    logger = get_logger(__name__)

    def event_affiliates(self, event_id) -> Iterator[Participant]:
        self.logger.info(f'Reading event ({event_id}) affiliates')
        handler = self.get(url=self.ROUTES["event_affiliates"].format(event_id))
        handler.raise_for_status()
        response = handler.json()
        return response