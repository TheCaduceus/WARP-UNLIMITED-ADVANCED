import asyncio
import os
import urllib.request
import httpx

from config import Vars
from datetime import datetime
from json import dumps
from random import choice
from string import ascii_letters, digits
from sys import stdout
from time import sleep
from warnings import filterwarnings
from nest_asyncio import apply

if Vars[5] == True:
  while True:
    referrer = input("Enter WARP CLIENT ID:\n")
    resp = input(f"ID:{referrer}\nDo you want to continue with this ID? 1 = Yes or 0 = No")
    if resp == "1":
      break
    else:
      pass
  SEND_LOG = input("Do you want to get log on Telegram?\n1 = Yes or 0 = No")
  if SEND_LOG == "1":
    CHANNEL_ID = input("Enter CHAT ID, in which you want log message to be sent:\n")
    BOT_TOKEN = input("Enter BOT_TOKEN, through which log message will be sent:\n")
    HIDE_ID = input("Do you want to hide WARP CLIENT ID in log message? 1 = Yes or 0 = No:\n")
else:
  referrer = Vars[0]
  SEND_LOG = Vars[1]
  CHANNEL_ID = Vars[2]
  BOT_TOKEN = Vars[3]
  HIDE_ID = Vars[4]

MSG_ID = False

apply()
filterwarnings("ignore", category=DeprecationWarning)
g = 0
b = 0

def genString(stringLength):
  try:
    letters = ascii_letters + digits
    return ''.join(choice(letters) for i in range(stringLength))
  except Exception as error:
    print(error)

def digitString(stringLength):
  try:
    digit = digits
    return ''.join((choice(digit) for i in range(stringLength)))
  except Exception as error:
    print(error)

url = f"https://api.cloudflareclient.com/v0a{digitString(3)}/reg"

async def run():
  try:
    install_id = genString(22)
    body = {
      "key": "{}=".format(genString(43)),
      "install_id": install_id,
      "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
      "referrer": referrer,
      "warp_enabled": False,
      "tos": datetime.now().isoformat()[:-3] + "+02:00",
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
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req)
    status_code = response.getcode()
    return status_code
  except Exception as error:
    return error

async def animation():
  cooldown = 0.3
  os.system("cls" if os.name == "nt" else "clear")
  animation = ["[□□□□□□□□□□] 0%", "[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
  for i in range(len(animation)):
    stdout.write("\r[∆] Progress: " + animation[i % len(animation)])
    stdout.flush()
    if i == 2:
      result = await run()
      if result != 200:
        cooldown = 0.1
    await asyncio.sleep(cooldown)
  return result

while True:
  anim = asyncio.get_event_loop()
  anim_coroutine = animation()
  result = anim.run_until_complete(anim_coroutine)
  if result == 200:
    g += 1
    if SEND_LOG == "1" and HIDE_ID == "1":
      if not MSG_ID:
        lol = httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
        get_stats = lol.json()
        MSG_ID = get_stats["result"]["message_id"]
      else:
        httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText?chat_id={CHANNEL_ID}&message_id={MSG_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
    elif SEND_LOG == "1" and HIDE_ID =="0":
      if not MSG_ID:
        lol = httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0AWARP%20ID:%20{referrer}%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
        get_stats = lol.json()
        MSG_ID = get_stats["result"]["message_id"]
      else:
        httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText?chat_id={CHANNEL_ID}&message_id={MSG_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0AWARP%20ID:%20{referrer}%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
    else:
      pass
    print(f"\n[•] WARP+ ID: {referrer}")
    print(f"[✓] Added: {g} GB")
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(20,1,-1):
      stdout.write(f"\033[1K\r[!] Cooldown: {i} seconds")
      stdout.flush()
      sleep(1)
  else:
    b += 1
    print("\n[×] Error:", result)
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(30,-1,-1):
      stdout.write(f"\033[1K\r[!] Cooldown: {i} seconds")
      stdout.flush()
      sleep(1)
