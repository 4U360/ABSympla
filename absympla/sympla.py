class ABSympla(object):
    from .core.session import SymplaSession
    from .core.events import SymplaEvents
    from .core._requests import SymplaRequests

    sympla_session = None
    __events = None
    __requests = None

    def __init__(self, api_key=None):
        self.update_session(api_key=api_key)

    def update_session(self, api_key=None):
        self.sympla_session = self.SymplaSession(api_key=api_key)
        self.__events = self.SymplaEvents(session=self.sympla_session.session)
        self.__requests = self.SymplaRequests(session=self.sympla_session.session)

    @property
    def events(self) -> SymplaEvents:
        return self.__events

    @property
    def requests(self) -> SymplaRequests:
        return self.__requests
