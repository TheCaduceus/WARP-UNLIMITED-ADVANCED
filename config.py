# To get values from Environment
Get_ENV = False # or True

# Required if Get_ENV == False
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
    ""
]

import os, sys
import logging as log

# Setup Logger
log.basicConfig(
    level=log.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format="[%(asctime)s][%(levelname)s] => %(message)s",
    handlers=[log.StreamHandler(stream=sys.stdout),
              log.FileHandler("runtime-log.txt", mode="a", encoding="utf-8")],)

def check():
	py_ver = sys.version_info

	if py_ver[0] == 3 and py_ver[1] < 9:
		log.warning(f"You are using Python 3.{py_ver[1]}.{py_ver[2]}, please upgrade it to 3.10.x to avoid any error.")
	elif py_ver[0] > 3:
		log.warning(f"You are using Python {py_ver[0]}.{py_ver[1]}.{py_ver[2]}, please use 3.10.x to avoid any error.")
	else:
		log.info(f"Python Version: {py_ver[0]}.{py_ver[1]}.{py_ver[2]}")

    if not Vars[0]:
        log.error("WARP_ID not found!")
        raise ValueError('WARP_ID cannot be empty!')
    else:
        log.info("Found WARP_ID.")

    if not Vars[1]:
        log.warning("SEND_LOG value is empty, hence disabled.")
        SEND_LOG = "0"
    else:
        if SEND_LOG == "0" or SEND_LOG == "1":
        	log.info(f"SEND_LOG: {Vars[1]}")
        else:
        	log.info("Provided SEND_LOG value is invalid! hence changed to 0 (disabled).")
        	SEND_LOG = "0"

    if not Vars[2]:
    	if SEND_LOG == "1":
    		log.warning("SEND_LOG is enabled but CHAT_ID not provided! hence disabled.")
    		SEND_LOG = "0"
    	else:
    		pass
    else:
    	log.info(f"Found CHAT_ID: {Vars[2]}")

    if not Vars[3]:
        if SEND_LOG == "1":
        	log.warning("SEND_LOG is enabled but BOT_TOKEN not provided! hence disabled.")
        	SEND_LOG = "0"
        else:
        	pass
    else:
        log.info("Found BOT_TOKEN")

    if not Vars[4]:
        log.warning("HIDE_ID is not provided! hence value changed to default (0).")
    else:
        if HIDE_ID == "1" or HIDE_ID == "0":
        	log.info(f"Found HIDE_ID: {Vars[4]}")
        else:
        	log.warning("HIDE_ID value is invalid! hence changed to default (0).")
    
    if Get_ENV == False:
        log.info("Got Values from config file!")
    else:
        log.info("Got Values from System Environment!")

if Get_ENV == False:
    log.info("Getting Values from Config.py file...")
    check()
elif Get_ENV == True:
    log.info("Getting Values from System Environment...")
    WARP_ID = os.environ.get("WARP_ID","")
    SEND_LOG = os.environ.get("SEND_LOG","")
    CHAT_ID = os.environ.get("CHAT_ID","")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","")
    HIDE_ID = os.environ.get("HIDE_ID","")
    
    Vars = [
        WARP_ID,
        SEND_LOG,
        CHAT_ID,
        BOT_TOKEN,
        HIDE_ID
    ]

    check()
else:
    log.error(r"Unable to undestand from where to get values?¯\_(ツ)_/¯")
    raise ValueError("Get_ENV value is invalid & should be True or False only!")
