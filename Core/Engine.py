
import colorama, os, sys, time, datetime, requests, random, json, subprocess
from .Settings import *

colorama.init()
C = colorama.Fore
G = C.GREEN; W = C.WHITE; R = C.RED; RS = C.RESET; Y = C.YELLOW; CY = C.CYAN

OS_NAME = "Windows" if sys.platform.startswith("win") else "Linux"
ROOT = os.path.dirname(os.path.abspath(__file__)).rsplit("Core",1)[0].rstrip("/\\")
OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "Desktop", "spectre_output")

def now(): return datetime.datetime.now().strftime("%H:%M:%S")

PR = f"{G}[{W}"; SF = f"{G}]"
PM = f"{PR}>{SF}"; IN = f"{PR}!{SF}"; ER = f"{PR}x{SF}"; OK = f"{PR}+{SF}"; WA = f"{PR}~{SF}"

def set_title(t):
    if OS_NAME == "Windows":
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(f"{TOOL_NAME}|{t}")
    else:
        sys.stdout.write(f"\x1b]2;{TOOL_NAME}|{t}\x07")

def clear(): os.system("cls" if OS_NAME == "Windows" else "clear")
def restart(): subprocess.run([sys.executable, os.path.join(ROOT, "Spectre.py")])
def launch(tool): subprocess.run([sys.executable, os.path.join(ROOT, "Tools", tool)])
def pause(): input("\n" + PR + now() + SF + " " + IN + " Press Enter to return -> " + RS)

def die(msg=""):
    if msg: print("\n" + PR + now() + SF + " " + ER + " " + R + msg + RS)
    pause(); restart()

def bad():
    print("\n" + PR + now() + SF + " " + ER + " Invalid!" + RS)
    time.sleep(2); restart()

LOGO = """
\033[32m
   ███████╗██████╗ ███████╗ ██████╗████████╗██████╗ ███████╗
   ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝
   ███████╗██████╔╝█████╗  ██║        ██║   ██████╔╝█████╗
   ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══██╗██╔══╝
   ███████║██║     ███████╗╚██████╗   ██║   ██║  ██║███████╗
   ╚══════╝╚═╝     ╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
\033[0m"""
