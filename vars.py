import os
from os import getenv, environ
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')
  
class Var(object):
      WARP_ID = str(getenv('WARP_ID'))
      SEND_LOG = str(getenv('SEND_LOG'))
      BOT_TOKEN = str(getenv('BOT_TOKEN'))
      CHANNEL_ID = str(getenv('CHANNEL_ID'))
      HIDE_ID = str(getenv('HIDE_ID'))
