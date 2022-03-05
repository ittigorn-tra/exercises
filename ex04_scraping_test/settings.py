import os
from logging import getLogger

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(env_path):
    raise Exception('.env file cannot be found! Please contact the author to get a copy of the file.')
load_dotenv(env_path)

logger = getLogger()
STAGE = os.getenv("STAGE")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_USER_SHOW_ENDPOINT = os.getenv("TWITTER_USER_SHOW_ENDPOINT")
