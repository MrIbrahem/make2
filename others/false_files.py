#!/usr/bin/python3
"""

python3 core8/pwb.py make2/false_files
"""

import re
import os
from pathlib import Path

Dir = Path(__file__).parent.parent.parent.parent
# ---
lenthes = {}
# ---
# python3 core8/pwb.py make2/read import
files_all = []
# ---
text = ""
# ---
for root, dirs, files in os.walk(Dir / "make2", topdown=True):
    for f in files:
        # ---
        if not root.endswith("make2"):
            continue
        # ---
        if not f.endswith(".py"):
            continue
        # ---
        skip = ["test_yy2.py", "len.py", "__init__.py", "false_files.py"]
        # ---
        if f in skip:
            continue
        # ---
        filepath = os.path.join(root, f)
        # ---
        with open(filepath, "r", encoding="utf-8") as f:
            fafax = f.read()
        # ---
        text += f"\n{fafax}"
        # ---
        files_all.append(f)
        # ---
# ---
# text = re.sub(r'from\s*make2\s*import\s*', 'from make2 import ', text)
# text = re.sub(r'from\s*make2\.(.*?)\s*import', 'from ..$1 import ', text)
# ---
for x in files_all:
    x = x.replace(".py", "")
    # find if text has x like from make2 import x
    test = text
    test = re.sub(r"from\s*make2\s*import\s*%s" % x, "", test)
    test = re.sub(r"from\s*make2.%s\s*import" % x, "", test)
    # ---
    if test == text:
        print(f"file:({x}.py)")
    # ---
# ---
