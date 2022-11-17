# To get values from Environment
ENV = True  # or True

# Ask for values during each run
INTERACTIVE_MODE = False  # or True

# Required if ENV == False
Vars = [
  # WARP_ID
  "",
  # SEND_LOG, Want to receive log on Telegram?
  # 1 = Yes or 0 = No
  "",
  # CHAT_ID, required if SEND_LOG is 1
  # Can be Channel/Group username or ID
  "",
  # BOT_TOKEN, required if SEND_LOG is 1
  # Get from https://t.me/BotFather
  "",
  # HIDE_ID, Do you want to hide WARP_ID from log msg?
  # 1 = Yes or 0 = No
  "",
  # DON'T EDIT THIS
  INTERACTIVE_MODE
]

import os, sys
import logging as log

Log_file = 'runtime-log.txt'

if os.path.exists(Log_file):
  os.remove(Log_file)
else:
  pass

# Setup Logger
log.basicConfig(
  level=log.INFO,
  datefmt="%d/%m/%Y %H:%M:%S",
  format="[%(asctime)s][%(levelname)s] => %(message)s",
  handlers=[
    log.StreamHandler(stream=sys.stdout),
    log.FileHandler(Log_file, mode="a", encoding="utf-8")
  ],
)
log.info("---Starting---")
log.info(f"Current Log file: {Log_file}")


def check():
  py_ver = sys.version_info

  if py_ver[0] == 3 and py_ver[1] < 8:
    log.warning(
      f"You are using Python 3.{py_ver[1]}.{py_ver[2]}, please upgrade it to 3.10.x to avoid any error."
    )
  elif py_ver[0] > 3:
    log.warning(
      f"You are using Python {py_ver[0]}.{py_ver[1]}.{py_ver[2]}, please use 3.10.x to avoid any error."
    )
  else:
    log.info(f"Python Version: {py_ver[0]}.{py_ver[1]}.{py_ver[2]}")

  if not Vars[0]:
    log.error("WARP_ID not found!")
    raise ValueError('WARP_ID cannot be empty!')
  else:
    key_length = len(Vars[0])
    final_length = key_length - 11
    hidden_key = "*" * final_length + Vars[0][-11:]
    log.info(f"Found WARP_CLIENT_ID: {hidden_key}")

  if not Vars[1]:
    log.warning("SEND_LOG value is empty, hence disabled.")
    Vars[1] = "0"
  else:
    if Vars[1] == "0" or Vars[1] == "1":
      log.info(f"SEND_LOG: {Vars[1]}")
    else:
      log.info(
        "Provided SEND_LOG value is invalid! hence changed to 0 (disabled).")
      Vars[1] = "0"

  if not Vars[2] and Vars[1] == "1":
    log.warning(
      "SEND_LOG is enabled but CHAT_ID not provided! hence disabled.")
    Vars[1] = "0"
  elif not Vars[2] and Vars[1] == "0":
    pass
  else:
    log.info(f"Found CHAT_ID: {Vars[2]}")

  if not Vars[3] and Vars[1] == "1":
    log.warning(
      "SEND_LOG is enabled but BOT_TOKEN not provided! hence disabled.")
    Vars[1] = "0"
  elif not Vars[3] and Vars[1] == "0":
    pass
  else:
    log.info("Found BOT_TOKEN")

  if not Vars[4] and Vars[1] == "1":
    log.warning(
      "HIDE_ID value  not provided! hence value changed to default (0).")
  else:
    if Vars[4] == "1" or Vars[4] == "0":
      log.info(f"Found HIDE_ID: {Vars[4]}")
    elif Vars[4] and SEND_LOG == "1":
      log.warning("HIDE_ID value is invalid! hence changed to default (0).")
    else:
      pass

  if ENV == False:
    log.info("Got Values from config.py file!")
  else:
    log.info("Got Values from System Environment!")


if ENV == False and INTERACTIVE_MODE == False:
  log.info("Getting Values from config.py file...")
  check()
elif ENV == True and INTERACTIVE_MODE == True:
  log.info("ENV & INTERACTIVE MODE both are active, hence disabled ENV MODE.")
  ENV = False
elif ENV == False and INTERACTIVE_MODE == True:
  log.info("INTERACTIVE MODE is active!")
elif ENV == True and INTERACTIVE_MODE == False:
  log.info("Getting Values from System Environment...")
  WARP_ID = os.environ.get("WARP_ID", "")
  SEND_LOG = os.environ.get("SEND_LOG", "")
  CHAT_ID = os.environ.get("CHAT_ID", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  HIDE_ID = os.environ.get("HIDE_ID", "")
  INTERACTIVE_MODE = os.environ.get("INTERACTIVE_MODE", False)

  Vars = [WARP_ID, SEND_LOG, CHAT_ID, BOT_TOKEN, HIDE_ID, INTERACTIVE_MODE]

  check()
else:
  if ENV != True and ENV != False:
    log.warning(
      "Given ENV value is invalid, it can be True or False (bool) only!")
    log.info(f"{ENV}: {type(ENV)}")
    raise ValueError(
      "ENV value is invalid! should be True or False (bool) only!")
  elif INTERACTIVE_MODE != True and INTERACTIVE_MODE != False:
    log.warning(
      "Given INTERACTIVE_MODE value in invalid, it can be True or False (bool) only!"
    )
    log.info(f"{INTERACTIVE_MODE}: {type(INTERACTIVE_MODE)}")
    raise ValueError(
      "INTERACTIVE_MODE value is invalid! should be True or False (bool) only")
  else:
    log.warning("Something went wrong!") # 0.1% still XD
