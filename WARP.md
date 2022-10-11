***Without Telegram Logger***<br>
``WARP_ID`` Enter your WARP/WARP+ ID<br>
```
import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
os.system("title WARP UNLIMITED ADVANCED")
os.system('cls' if os.name == 'nt' else 'clear')

referrer = input("[#] Enter the WARP+ ID:\n")
def genString(stringLength):
  try:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
  except Exception as error:
    print(error)
def digitString(stringLength):
  try:
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))
  except Exception as error:
    print(error)
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
  try:
    install_id = genString(22)
    body = {"key": "{}=".format(genString(43)),
        "install_id": install_id,
        "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
        "referrer": referrer,
        "warp_enabled": False,
        "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
        "type": "Android",
        "locale": "es_ES"}
    data = json.dumps(body).encode('utf8')
    headers = {'Content-Type': 'application/json; charset=UTF-8',
          'Host': 'api.cloudflareclient.com',
          'Connection': 'Keep-Alive',
          'Accept-Encoding': 'gzip',
          'User-Agent': 'okhttp/3.12.1'
          }
    req         = urllib.request.Request(url, data, headers)
    response    = urllib.request.urlopen(req)
    status_code = response.getcode()
    return status_code
  except Exception as error:
    print("")
    print("[×] Error:", error)

g = 0
b = 0
while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
  for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r[∆] Progress: " + animation[i % len(animation)])
    sys.stdout.flush()
  result = run()
  if result == 200:
    g += 1
    print(f"\n[•] WARP+ ID: {referrer}")
    print(f"[✓] Added: {g} GB")
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(20,-1,-1):
      sys.stdout.write(f"\033[1K\r[!] Cooldown: {i} seconds")
      sys.stdout.flush()
      time.sleep(1)
  else:
    b += 1
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(10,-1,-1):
      sys.stdout.write(f"\033[1K\r[!] Cooldown: {i} seconds")
      sys.stdout.flush()
      time.sleep(1)
  ```
***With Telegram Logger***<br>
``WARP_ID`` Enter your WARP/WARP+ ID.<br>
``BOT_TOKEN`` Telegram Bot Token from BotFather.<br>
``CHANNEL_ID`` If  Channel or Group is public enter username example @mygroup or @mychannel. If it is private enter CHAT ID example -100XXXXX .<br>
``HIDE_ID`` To hide WARP_ID in the log message send to Telegram Channel or Group. 0 for No and 1 for Yes.
  ```
import httpx
import json
import datetime
import random
import string
import time
import os
import sys
# Variables
BOT_TOKEN = input("Enter Bot Token:\n")
CHANNEL_ID = input("Enter Channel ID:\n")
SEND_LOG = "1" # 0 to Disable
HIDE_ID = "0" # 1 to Enable
referrer = input("[#] Enter the WARP+ ID:\n")
MSG_ID = False

def genString(stringLength):
  try:
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
  except Exception as error:
    print(error)
def digitString(stringLength):
  try:
    digit = string.digits
    return ''.join((random.choice(digit) for i in range(stringLength)))
  except Exception as error:
    print(error)
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
  try:
    install_id = genString(22)
    body = {"key": "{}=".format(genString(43)),
        "install_id": install_id,
        "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
        "referrer": referrer,
        "warp_enabled": False,
        "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
        "type": "Android",
        "locale": "es_ES"}
    data = json.dumps(body).encode('utf8')
    headers = {'Content-Type': 'application/json; charset=UTF-8',
          'Host': 'api.cloudflareclient.com',
          'Connection': 'Keep-Alive',
          'Accept-Encoding': 'gzip',
          'User-Agent': 'okhttp/3.12.1'
          }
    req = httpx.post(url,headers=headers,data=data)
    status_code = req.status_code
    return status_code
  except Exception as error:
    print("")
    print("[×] Error:", error)

g = 0
b = 0
while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  animation = ["[■□□□□□□□□□] 10%","[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"] 
  for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r[∆] Progress: " + animation[i % len(animation)])
    sys.stdout.flush()
  result = run()
  if result == 200:
    g += 1
    if SEND_LOG == "1" and HIDE_ID == "1":
      if not MSG_ID:
        lol = httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
        get_stats = lol.json()
        MSG_ID = get_stats["result"]["message_id"]
      else:
        httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText?chat_id={CHANNEL_ID}&message_id={MSG_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
    else:
      if not MSG_ID:
        lol = httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHANNEL_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0AWARP%20ID:%20{referrer}%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
        get_stats = lol.json()
        MSG_ID = get_stats["result"]["message_id"]
      else:
        httpx.post(f"https://api.telegram.org/bot{BOT_TOKEN}/editMessageText?chat_id={CHANNEL_ID}&message_id={MSG_ID}&parse_mode=HTML&text=<b><u>WARP STATISTICS</u></b>%0AWARP%20ID:%20{referrer}%0ADATA%20RECEIVED:%20%0A{str(g)}GB%20%0AFAILED:%20%0A{str(b)}")
    print(f"\n[•] WARP+ ID: {referrer}")
    print(f"[✓] Added: {g} GB")
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(20,1,-1):
      sys.stdout.write(f"\033[1K\r[!] Cooldown: {i} seconds")
      sys.stdout.flush()
      time.sleep(1)

  else:
    b += 1
    print(f"[#] Total: {g} Good {b} Bad")
    for i in range(20,-1,-1):
      sys.stdout.write(f"\033[1K\r[!] Cooldown: {i} seconds")
      sys.stdout.flush()
      time.sleep(1)
  ```
<b>Made with 💗 & 🍵 by Dr.Caduceus</b>
