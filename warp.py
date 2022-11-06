import asyncio
import os
import urllib.request
from datetime import datetime
from json import dumps
from random import choice
from string import ascii_letters, digits
from sys import stdout
from time import sleep
from warnings import filterwarnings

from nest_asyncio import apply

apply()
filterwarnings("ignore", category=DeprecationWarning)
os.system("title WARP UNLIMITED ADVANCED")
os.system("cls" if os.name == "nt" else "clear")

referrer = input("[#] Enter the WARP+ ID:\n")

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
    print(f"\n[•] WARP+ ID: {referrer}")
    print(f"[✓] Added: {g} GB")
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(20,-1,-1):
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
