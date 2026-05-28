import sys, os, sqlite3, shutil, tempfile
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("History Grab")
print(LOGO)
if OS_NAME != "Windows":
    die("Windows only")
browsers = [
    ("Chrome", os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")),
    ("Edge", os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data"))
]
out = os.path.join(ROOT, "1-Output")
os.makedirs(out, exist_ok=True)
all_h = []
for bn, bp in browsers:
    if not os.path.exists(bp): continue
    for item in os.listdir(bp):
        prof = os.path.join(bp, item)
        if not os.path.isdir(prof) or (item != "Default" and not item.startswith("Profile")): continue
        db = os.path.join(prof, "History")
        if not os.path.exists(db): continue
        tmp = tempfile.mktemp(suffix=".db")
        try: shutil.copy2(db, tmp)
        except: continue
        try:
            conn = sqlite3.connect(tmp)
            c = conn.cursor()
            c.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 100")
            for row in c.fetchall():
                all_h.append(f"{bn}|{row[0]}|{row[1]}")
            conn.close()
        except: pass
        try: os.remove(tmp)
        except: pass
if all_h:
    fp = os.path.join(out, "history.txt")
    with open(fp, "w", encoding="utf-8") as f:
        f.write("\n".join(all_h))
    print(f"{OK} {len(all_h)} entries -> {fp}")
else:
    print(f"{IN} No history found")
pause()
restart()
