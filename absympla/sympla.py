class ABSympla(object):
    from .core.session import SymplaSession
    from .core.events import SymplaEvents
    from .core.orders import SymplaOrders

    sympla_session = None
    __events = None
    __orders = None

    def __init__(self, api_key=None):
        self.update_session(api_key=api_key)

    def update_session(self, api_key=None):
        self.sympla_session = self.SymplaSession(api_key=api_key)
        self.__events = self.SymplaEvents(session=self.sympla_session.session)
        self.__orders = self.SymplaOrders(session=self.sympla_session.session)

    @property
    def events(self) -> SymplaEvents:
        return self.__events

    @property
    def orders(self) -> SymplaOrders:
        return self.__orders
