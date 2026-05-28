#!/usr/bin/env python3
import os, sys, shutil
BASE = os.path.join(os.path.expanduser('~'), 'Desktop', 'spectre-tools')
def w(rel, content):
    p = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
if os.path.exists(BASE):
    shutil.rmtree(BASE)
w('Core/__init__.py', '')
w('Core/Settings.py', 'TOOL_NAME = "Spectre"\nVERSION   = \'5.0\'\nAUTHOR    = "SpectreTeam"\nPLATFORM  = "Linux & Windows"\n')
print("Core created. Now run: python3 ~/spectre/build_full.py")
