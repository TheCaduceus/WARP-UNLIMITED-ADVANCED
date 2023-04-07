from config import (
  log,
  WARP_CLIENT_ID, 
  SEND_LOG, 
  HIDE_WC_ID, 
  TELEGRAM_BOT_TOKEN, 
  CHAT_ID,
  MSG_ID,
  SUCCESS_COUNT,
  FAIL_COUNT
  )
from datetime import datetime
from json import dumps
from random import choice, randint
from string import ascii_letters, digits
from time import sleep
import httpx

def genString(stringLength):
  try:
    letters = ascii_letters + digits
    return ''.join(choice(letters) for _ in range(stringLength))
  except Exception as error_code:
    log.error(error_code)

def digitString(stringLength):
  try:
    digit = digits
    return ''.join(choice(digit) for _ in range(stringLength))
  except Exception as error_code:
    log.error(error_code)

url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"

while True:
  try:
    install_id = genString(22)
    body = {
      "key": f"{genString(43)}=",
      "install_id": install_id,
      "fcm_token": f"{install_id}:APA91b{genString(134)}",
      "referrer": WARP_CLIENT_ID,
      "warp_enabled": False,
      "tos": f"{datetime.now().isoformat()[:-3]}+02:00",
      "type": "Android",
      "locale": "es_ES"
    }
    data = dumps(body).encode("utf8")
    headers = {
      "Content-Type": "application/json; charset=UTF-8",
      "Host": "api.cloudflareclient.com",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip",
      "User-Agent": "okhttp/3.12.1"
    }
    response = httpx.post(url, data=data, headers=headers).status_code
  except Exception as error_code:
    log.error(error_code)

  if response == 200:
    SUCCESS_COUNT += 1
    log.info(f"PASSED: +1GB (total: {SUCCESS_COUNT}GB, failed: {FAIL_COUNT})")
    if SEND_LOG and HIDE_WC_ID:
      if not MSG_ID:
        api_resp = httpx.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0ADATA%20RECEIVED:%20%0A{SUCCESS_COUNT}GB%20%0AFAILED:%20%0A{FAIL_COUNT}")
        get_stats = api_resp.json()
        try:
          MSG_ID = get_stats["result"]["message_id"]
        except KeyError:
          log.error(f"API Response:\n{get_stats}")
          raise
      else:
        httpx.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/editMessageText?chat_id={CHAT_ID}&message_id={MSG_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0ADATA%20RECEIVED:%20%0A{SUCCESS_COUNT}GB%20%0AFAILED:%20%0A{FAIL_COUNT}")
    elif SEND_LOG and not HIDE_WC_ID:
      if not MSG_ID:
        api_resp = httpx.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0AWARP%20ID:%20{WARP_CLIENT_ID}%0ADATA%20RECEIVED:%20%0A{SUCCESS_COUNT}GB%20%0AFAILED:%20%0A{FAIL_COUNT}")
        get_stats = api_resp.json()
        try:
          MSG_ID = get_stats["result"]["message_id"]
        except KeyError:
          log.error(f"API Response: {get_stats}")
          raise
      else:
        httpx.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/editMessageText?chat_id={CHAT_ID}&message_id={MSG_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0AWARP%20ID:%20{WARP_CLIENT_ID}%0ADATA%20RECEIVED:%20%0A{SUCCESS_COUNT}GB%20%0AFAILED:%20%0A{FAIL_COUNT}")
  else:
    log.info(f"FAILED: {response}")
    FAIL_COUNT += 1
  
  # Cooldown
  cooldown_time = randint(30,50)
  log.info(f"Sleep: {cooldown_time} seconds.")
  sleep(cooldown_time)
