import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
WEB_SITE = os.getenv('WEB_SITE')
NGROK_TUNNEL_URL = os.getenv('NGROK_TUNNEL_URL')
