from absympla.log import get_logger
from requests import Session
from absympla.settings import API_KEY


class SymplaSession(object):
    """
    Base class for session control in Sympla
    """
    logger = get_logger(__name__)
    __session: Session = Session()

    def __init__(self, api_key: str = None):
        self.logger.info('Logging in from Sympla')
        self.__session.headers.update({
            's_token': API_KEY if api_key is None else api_key
        })

    @property
    def session(self) -> Session:
        return self.__session

    def __enter__(self) -> Session:
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.info('Closing Sympla session')
