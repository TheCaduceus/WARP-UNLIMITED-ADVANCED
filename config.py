ENV = True # or False
INTERACTIVE_MODE = False # or True
WARP_CLIENT_ID = ""
SEND_LOG = False # or True
HIDE_WC_ID = True # or False
TELEGRAM_BOT_TOKEN = ""
CHAT_ID = ""
LOG_FILE = "runtime-log.txt" # rename if required

# Defaults
MSG_ID, SUCCESS_COUNT, FAIL_COUNT = False, 0, 0

from os import environ
from sys import stdout, version_info as py_ver
import logging as log

log.basicConfig(
  level=log.INFO,
  datefmt="%d/%m/%Y %H:%M:%S",
  format="[%(asctime)s][%(levelname)s] => %(message)s",
  handlers=[
    log.StreamHandler(stream=stdout),
    log.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
  ],
)

log.info("--STARTED--")
log.info(f"Current log file: {LOG_FILE}")
log.info(f"Python: {py_ver[0]}.{py_ver[1]}.{py_ver[2]}")

if ENV:
  log.info("ENV mode in ENABLED.")
  WARP_CLIENT_ID = str(environ.get("WARP_CLIENT_ID", ""))
  SEND_LOG = str(environ.get("SEND_LOG", False).lower()) in {"true", "t", "1"}
  if SEND_LOG:
    TELEGRAM_BOT_TOKEN = environ.get("TELEGRAM_BOT_TOKEN", "")
    CHAT_ID = environ.get("CHAT_ID", "")
    HIDE_WC_ID = str(environ.get("HIDE_WC_ID", True)) in {"true", "t", "1"}
elif INTERACTIVE_MODE:
  log.info("Interactive mode is ENABLED.")
  WARP_CLIENT_ID = input("Enter your WARP Client ID:\n")
  SEND_LOG = input("Do you want to get log message? True or False:\n").lower() in {"true", "t", "1"}
  if SEND_LOG:
    TELEGRAM_BOT_TOKEN = input("Enter Telegram Bot Token:\n")
    CHAT_ID = input("Enter Chat ID to get log on:\n")
    HIDE_WC_ID = input("Do you want to hide WARP Client ID from log message? True or False:\n").lower() in {"true", "t", "1"}

if not WARP_CLIENT_ID:
  log.error("WARP Client ID not found!")
  raise ValueError("WARP Client ID not provided!")
elif SEND_LOG:
  if not TELEGRAM_BOT_TOKEN:
    log.error("Telegram Bot token not found!")
    raise ValueError("Telegram Bot token not provided!")
  elif not CHAT_ID:
    log.error("Chat ID not found!")
    raise ValueError("Chat ID not provided!")
  elif not HIDE_WC_ID:
    log.info("WARP Client ID is NOT hidden from log message.")
  else:
    log.info("WARP Client ID is hidden from log message.")
