#!/usr/bin/env python
import sys
import os

# Basic dispatcher
scripts = {
    "dir": "loraDir.py",
    "mulbs": "loraDirMulBS.py",
    "intf": "directionalLoraIntf.py",
    "oneintf": "oneDirectionalLoraIntf.py"
}

if len(sys.argv) < 2 or sys.argv[1] not in scripts:
    print("Usage: python main.py [dir|mulbs|intf|oneintf] <args...>")
    sys.exit(1)

script = scripts[sys.argv[1]]
args = sys.argv[2:]

os.execvp("python", ["python", script] + args)
