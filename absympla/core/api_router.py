from ..settings import API_HOST
from requests import Session


class SymplaAPIRouter:
    ROUTES = {}

    __session: Session

    @property
    def session(self) -> Session:
        return self.__session

    def __init__(self, session: Session):
        self.__session = session
        assert isinstance(self.session, Session)

    def get(self, url, *args, **kwargs):
        return self.session.get(url=f"{API_HOST}/{url}", *args, **kwargs)

    def post(self, url, *args, **kwargs):
        return self.session.post(url=f"{API_HOST}/{url}", *args, **kwargs)

    def __get_route(self, key) -> str:
        route = self.ROUTES.get(key, None)
        assert isinstance(route, str)
        return route
