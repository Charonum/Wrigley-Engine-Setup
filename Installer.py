import getpass
import sys
import subprocess
import os
import zipfile
import shutil
import wget


try:
    os.mkdir(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine")
except:
    pass

subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

url = "https://github.com/Charonum/WE_Startup/archive/refs/heads/main.zip"
wget.download(url, rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine")

with zipfile.ZipFile(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine\WE_Startup-main.zip", 'r') as zipObj:
    zipObj.extractall(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine")

for file in os.listdir(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine\WE_Startup-main"):
    shutil.move(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine\WE_Startup-main\{file}", rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine")

os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine\WE_Startup-main.zip")
os.remove(rf"C:\Users\{getpass.getuser()}\Charonum\Wrigley Engine\WE_Startup-main")