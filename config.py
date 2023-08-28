import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEB_SITE = os.getenv('WEB_SITE')
NGROK_TUNNEL_URL = os.getenv('NGROK_TUNNEL_URL')
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND')
DB_URL = os.getenv('DB_URL')

