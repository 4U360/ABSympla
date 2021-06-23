from os import getenv
from dotenv import load_dotenv
load_dotenv()

DEBUG = bool(getenv('DEBUG', 0))
API_HOST = getenv('SYMPLA_API_HOST', 'https://api.sympla.com.br')
API_KEY = getenv('SYMPLA_API_KEY', "")