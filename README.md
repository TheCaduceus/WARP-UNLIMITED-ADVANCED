<div align="center">
<a name="warp-unlimited-new-methods"></a>

# ♻️ WARP UNLIMITED ADVANCED
**Get unlimited amount of data in Cloudflare's WARP, most versatile code written in our beloved Python! ethically of course.**
</div>

## **📑 INDEX**
#### **Easily navigate through out the guide and pick the best method that suits you and your requirements!**
+ [**♻️ WARP UNLIMITED ADVANCED**](#warp-unlimited-new-methods)
+ [**📑 Features**](#features)
+ [**🪧 Before you proceed**](#before-you-proceed)
+ [**⚙️ How to use ? 😅 How to get WARP CLIENT ID ?**](#how-to-use)
+ [**→ 🕹️ Run on Google Colab**](#run-on-google-colab)
+ <b><a href="#deploy-to-koyeb">→ <img src="https://user-images.githubusercontent.com/87380104/205833766-633843a2-d802-4c72-8732-70d826d5c144.png" height="15" width="15">  Deploy on Koyeb (24x7)</a></b>
+ [**→ ⚡ Host on Heroku (24×7)**](#host-on-heroku)
+ [**→ 🧿 Host on Railway (24×7)**](#host-on-railway)
+ [**→ 🪬 Host on Okteto (24×7)**](#host-on-okteto)
+ [**→ 🖥️ Run on Computer/VPS**](#run-on-computer)
+ [**→ 🧫 Deploy through GitHub Actions**](#deploy-using-github-actions)
+ [**→ 📲 Run on Mobile Phone**](#run-on-mobile-phone)
+ [**→ 🎲 Run on Replit**](#run-on-replit)
+ [**→ 🧰 Run on Jupyter Server**](#run-on-jupyter-server)
+ [**→ 📈 Update Values (📲 For Mobile & 🖥️ For Windows/Linux)**](#update-values)
+ [**📥 Download Cloudflare WARP (1.1.1.1)**](#download-cloudflare-warp-1111)
+ [**❓FAQ**](#faq)
+ [**🖥️ How to use this data on PC ?**](#how-to-use-this-data-on-pc)
+ [**⛑ Contact Us**](#contact-us)
+ [**❤️ Credits & Thanks**](#credits-thanks)

<a name="features"></a>

## **📑 Features**
#### **1.Get 1GB per 30-50 seconds ! 🔥**
#### **2.Run this almost everywhere ! 🤗**
#### **3.Get notification on Telegram. 🔔**

<a name="before-you-proceed"></a>

## **🪧 Before you proceed** 
**1.It doesn't matter if you have WARP or WARP+, this program works for both.** <br>
**2.We are not hacking or gaining access to any Cloudflare system or their servers nor we are changing any official records illegally. We are just using official Cloudflare's API.**<br>
**3.Avoid hosting this program on platforms involving shared IPs to prevent response code 429 [Too many requests]. Prefer running this on your personal devices.**<br>
**4.Recommended Python Version: `3.7.x`...`3.11.x`.**

<a name="how-to-use"></a>

## **⚙️ How to use ?**
#### **0.First get your WARP Client ID by navigating to *App > Settings > Advanced > Diagnostics* and copy the ID under *CLIENT CONFIGURATION* section *(note that you can get that ID only in the mobile app, not in the desktop app)***
<img src="Img/1.jpg" height="70%" width="40%" alt="1">

<a name="variables"></a>
## **✏️ Variables**
**Below given variables should be filled in `config.py` file or can be passed as environment variables (ENVs), added to this you can also enable `INTERACTIVE_MODE` to enter new values during each run.**
- **`ENV`: Set it to `True` to let program get values from system environment or `False` if you are filling it in `config.py` itself or in case of `INTERACTIVE_MODE`. `bool`**
- **`INTERACTIVE_MODE`: Set it to `True` if you want program to ask for new values during each run or simply `False`. `bool`**
- **`WARP_CLIENT_ID`: Enter your WARP Client ID. [How to get?](#how-to-use). `str`**
- **`SEND_LOG`: Get notification on Telegram regarding total data generated, total attempts & failed attempts. Value can be  `True` or `False` only. `bool`**
- **`TELEGRAM_BOT_TOKEN`: Enter Telegram Bot Token from [@BotFather](https://botfather.t.me/). Required if `SEND_LOG` is `True`. `str`**
- **`CHAT_ID`: Enter chat id of chat (channel or group) where you want to get log message from your bot like `-1234567890` (for private chats) or @mychannel and @mygroup (for public chats). You can also pass ID of a particular user to get log message as personal message by bot but make sure to send /start command to bot as personal message (in order to authorize the bot). `str`**
- **`HIDE_WC_ID`: To hide your WARP Client ID from log message. Value can be `True` or `False` only. `bool`**

<a name="run-on-google-colab"></a>

## **🕹️ Run on Google Colab**
#### **1.Open code on Google Colab: [Open NoteBook](https://colab.research.google.com/github/TheCaduceus/WARP-UNLIMITED-ADVANCED/blob/main/ipynb/Colab.ipynb)**  
#### **2.Now enter your WARP Client ID and run The WARP (1.1.1.1) code as shown in the image *(click on the Play button on top-left corner)***
![3](./Img/3.jpg)

<a name="deploy-to-koyeb"></a>

<h2> <b><img src="https://user-images.githubusercontent.com/87380104/205833766-633843a2-d802-4c72-8732-70d826d5c144.png" height="20" width="20">  Deploy on Koyeb</b> </h2>

<b>Run program totally for free on Koyeb with single click deployment button!</b>
#### **1.Click the following one-click deployment button:**
[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/apps/deploy?type=docker&image=ghcr.io/thecaduceus/warp-unlimited-docker:koyeb&name=warpunlimitedadvanced&ports=8080;http;/&env[WARP_CLIENT_ID]=Enter-WARP-ID&env[SEND_LOG]=False&env[CHAT_ID]=Enter-CHAT-ID&env[TELEGRAM_BOT_TOKEN]=Enter--TOKEN&env[HIDE_WC_ID]=Enter-Value)
#### **2.Fill the given variables as [discussed above](#variables) and click 'Deploy'.**
![image](https://user-images.githubusercontent.com/87380104/230634974-b846bf74-f424-49c6-b790-d19957f00315.png)
#### **3.While deployment, you can choose 'Nano' instance type since it requires <256 RAM.**
![image](https://user-images.githubusercontent.com/87380104/205841570-6a43c020-eecf-4574-8c53-41f9454b5d79.png)
#### **⛔NOTE: This method uses ready-to-use Docker image made specially for Koyeb, hence any change requires building of new image with NPM's 'http-server' or 'Flask' to listen on port `8000` & `8080`.**

<a name="host-on-heroku"></a>

## **⚡Host on Heroku**
#### **1.First click the following deploy button.**
[![Deploy on Heroku](./Img/Heroku%20Deployment%20Button.png)](https://heroku.com/deploy?template=https://github.com/TheCaduceus/WARP-UNLIMITED-ADVANCED/tree/sys-env)
#### **2.Now, enter the values as discussed above and click 'Deploy' button.**
![image](https://user-images.githubusercontent.com/87380104/230636731-f0ababe9-be29-46c5-813c-35ff34dc24db.png)
#### **3.After deployment, click "Manage App" button and then click "Resources Tab" and enable the dyno.**
![5](./Img/5.png)

#### **4.Done! now you can check logs.**

<a name="host-on-railway"></a>

## **🧿 Host on Railway**
#### **1.First, create account or login on [Railway](https://railway.app/)**
![](./Img/3.1.png)

#### **2.Now click the following Railway deployment button:**
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/e0er7k?referralCode=PFHpF8)

#### **3.Enter the values as [discussed above](#variables) and click 'Deploy' button.**

<a name="host-on-okteto"></a>

## **🪬 Host on Okteto**
#### **1.First create your Okteto account. You need one GitHub account as Okteto support only one Method to either create or login: [Create Account](https://cloud.okteto.com/#/login)**
![](./Img/1.1.png)

#### **2.Now [import](https://github.com/new/import) this repository and deploy it on Okteto.**
#### **3.After that, carefully add the values as discussed above in Okteto deployment page.**
#### **4.Once done, click on Launch button to deploy your repository.**
#### **5.Additionally, you can setup cron-job using [Cron-Job.org](https://cron-job.org) to automatically restart your program once it sleeps after 24 hours.**

<a name="run-on-computer"></a>

## **🖥️ Run on Computer/VPS**
#### **1.If your PC not have python & git installed, then install them first:**
**For Windows: (WinGet)**
```
winget install python3.10
winget install Git.Git
```
**For Linux: (APT)**
```
sudo apt-get update && sudo apt-get install -y python3.10 git pip
```
**For Mac: (HomeBrew)**
```
brew install python@3.10 git
```
#### **2.Download Repository:**
```
git clone https://github.com/TheCaduceus/WARP-UNLIMITED-ADVANCED.git
```
#### **3.Install requirements:**
```
pip install -r requirements.txt
```
#### **4.Fill `config.py` as [discussed here](#variables).**
```
nano config.py
```
#### **5.Run the program:**
```
py warp-plus.py
```
#### **6.Logs can be accessed in `runtime-log.txt` file:**
```
cat runtime-log.txt
```

<a name="deploy-using-github-actions"></a>

## **🧫 Deploy using GitHub Actions**
#### **1.First fork this Repository.**
![](./Img/3.2.jpeg)
#### **2.Now open the settings of your forked repository and click Secrets → Actions.**
![](./Img/2.0.jpeg)
#### **3.After doing that, create following values as secret + values [discussed here](#variables):**
+ `HEROKU_API_KEY` - Enter your Heroku API key as value.
+ `HEROKU_APP_NAME` - A unique app name in small letters only.
+ `HEROKU_EMAIL` - Your Heroku Email ID.

#### **4.Go to Actions Tab then click "Deploy on Heroku" and "Run Workflow". Now it will automatically get deployed on given Heroku Account.**
#### **5.It will take maximum 10 seconds to start the workflow and minimum 1-2 minutes to get deployed !**

<a name="run-on-mobile-phone"></a>

## **📲 Run on Mobile Phone**
#### **1.First Download the Termux app [from here](https://github.com/termux/termux-app/releases/latest) *(Play Store version is deprecated)*.**
#### **2.Now run the following commands in it one by one:**
1.Download Python:
```
pkg install python
```
2.Download Git:
```
pkg install git
```
3.Update all dependencies:
```
termux-setup-storage && pkg update -y && pkg i git python wget
```
4.Download Repository:
```
git clone https://github.com/TheCaduceus/WARP-UNLIMITED-ADVANCED.git
```
5.Install requirements:
```
pip install -r requirements.txt
```
6.Change directory:
```
cd WARP-UNLIMITED-ADVANCED
```
7.Run the program:
```
python warp.py
```
#### **3. After doing above steps, enter your WARP Client ID.**

<a name="run-on-replit"></a>

## **🎲 Run on Replit**
#### **1.Open repl: [Open it](https://replit.com/@TheCaduceus/WARP-UNLIMITED-PROGRAM)**
#### **2.Enter your WARP Client ID and press enter to run the program.**
![image](https://user-images.githubusercontent.com/87380104/230643695-40c8775a-6216-4d0f-a436-6dab863da6c5.png)
#### **3.Additionally, you can fork the repl & edit `config.py` to enable / disable required features.**

<a name="run-on-jupyter-server"></a>

## **🧰 Run on Jupyter Server**
##### **Setting up the Jupyter Server:**
#### **1.First install Python with PIP: [from here](https://www.python.org/downloads/)**
#### **2.Now run the CMD / Powershell as Administrator and execute following commands one-by-one:**
1.To install Jupyter:
```
pip install jupyter
```
2.To install Notebook:
```
pip install notebook
```
3.Start Jupyter Server:
```
python -m notebook
```
#### **3.Once you started your Server, Jupyter will give you its link (as shown in Image), just open it in your Browser.**
![](./Img/jp-1.png)
![](./Img/jp-2.png)
#### **4.Now Download the "Server.ipynb" file: [from here only](https://github.com/TheCaduceus/WARP-UNLIMITED-ADVANCED/blob/main/ipynb/Server.ipynb)**
#### **5.After downloading it, locate that file through your Jupyter server and open it as shown in the image and click Run.**
![](./Img/jupyter-server-pre.png)
#### **6.Now enter your WARP Client ID and press Enter to continue.**

<a name="update-values"></a>

## **📈 Update Values**
#### **After deploying or running this program, you have to update the "Data Remaining" value in your App.**
### **📲 For Mobile:**
#### **Go to *Settings → Advanced → Connection Options → Press Reset Security Keys***
### **🖥️ For Windows:**
#### **Just again enter your activation key!**
### **🐧 For Linux:**
#### **Get activation key in the mobile app, then open terminal and execute:**
```
warp-cli set-license $KEY_HERE
```

<a name="download-cloudflare-warp-1111"></a>

## **📥 Download Cloudflare WARP (1.1.1.1)**
**Cloudflare's WARP which is based on 1.1.1.1, world's fastest DNS resolver helps you to encrypt your Network traffic and surf the web faster and available for major Operating-Systems (OS):**  
**📱Android: [Download](https://play.google.com/store/apps/details?id=com.cloudflare.onedotonedotonedotone)**  
**📟iOS: [Download](https://itunes.apple.com/us/app/1-1-1-1-faster-internet/id1423538627)**  
**🖥️Windows: [Download](https://1111-releases.cloudflareclient.com/windows/Cloudflare_WARP_Release-x64.msi)**  
**🍎Mac: [Download](https://1111-releases.cloudflareclient.com/mac/Cloudflare_WARP.zip)**  
**💻Linux: [Download](https://pkg.cloudflareclient.com/)**

<a name="faq"></a>

## **❓FAQ**
#### **1.How many instances of the program I can run simultaneously for same account?**
I will recommend to host/run 3 or less than 3 (< 3) instances for each account because Cloudflare's API have request limits. Hosting/Running too many instances can cause "429" error which indicates that API is getting too many requestes from the same account or IP and that's why there is a cooldown timer of 30-50 seconds to prevent this.
#### **2.How to resolve "429" error?**
First make sure you are running 3 or less than 3 (<3) instances of this program for same account and if this error still persist then possible reason can be that you or platform where you hosted this program is making use of shared IPs, prefer using dedicated IPs. Try running this in your personal devices.
#### **3.Will this program cause any kind of ban from Cloudflare?**
No, this program NOT cause ban because it just use the API provided by Cloudflare for referral system. Neither this program create any type of load or bypass any limit set by Cloudflare for their API nor it hacks anything or changes any official record illegally.
#### **4.I deployed it on a platform that allow setting environment variables, but program not accepting it?**
Before deploying it on any platform which allow users to set variables in system environment, just make sure you enable `ENV` mode & disable `INTERACTIVE_MODE`.
#### **5.Why use this program? we can simply use any mod of WARP app?**
WARP+ is for lifting the speed cap imposed by Cloudflare on free users which is server-side limit and it can't be bypassed by just modifying client-side code. So, availabe mods of WARP is fake? yes, they are just showing premium branding while doing nothing in reality.

<a name="how-to-use-this-data-on-pc"></a>

## **🖥️ How to use this data on PC?**
#### **Open the WARP app in your phone and go to *Settings > Account > Key* and copy the license key, now enter that key in WARP app on Windows or MacOS or Linux.**

<a name="contact-us"></a>

## **⛑ Contact Us**
#### **Join update channel at Telegram: [@TheCaduceusOfficial](https://t.me/TheCaduceusOfficial)**
#### **Directly contact the developer using [Telegram](https://telegram.me/TheCaduceusHere).**

<a name="credits-thanks"></a>

## **❤️Credits & Thanks**
**[Dr.Caduceus](https://github.com/TheCaduceus): For rewriting the script with httpx, adding Telegram notification, Docker & adding major PAAS platforms support.**<br>
**[ALI-B](https://github.com/ALIILAPRO): For base repository (now disabled by GitHub).**
