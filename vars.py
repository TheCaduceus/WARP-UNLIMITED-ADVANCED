import os
from os import getenv, environ
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')
  
class Var(object):
      referrer = str(getenv('warp_id'))