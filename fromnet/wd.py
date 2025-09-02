#!/usr/bin/python3
"""
محاولة إيجاد تسميات من ويكي بيانات
"""

import re
import json
from typing import Dict, Any
import requests
from .. import printe
import sys

# ---
pprint: Dict[int, bool] = {1: False}


def Priiint(text: Any) -> None:
    if pprint[1]:
        printe.output(text)


# ---
Cashens: Dict[str, Any] = {}
# ---
api_url: str = "https://www.wikidata.org/w/api.php"
session_wd: Dict[int, Any] = {1: False}
# ---
en_literes: str = "[abcdefghijklmnopqrstuvwxyz]"
ar_literes: str = "[ابتثجحخدذرزسشصضطظعغفقكلمنهوية]"


def find_name_from_wikidata(text: str, lang: str, Local: bool = False) -> Dict[str, str]:
    # ---
    if "nowikidata" in sys.argv or "local" in sys.argv or Local:
        return {}
    # ---
    if text in Cashens:
        return {text: Cashens[text]}
    # ---
    if not session_wd[1]:
        session_wd[1] = requests.Session()
    # ---
    params: Dict[str, Any] = {
        "action": "wbsearchentities",
        "format": "json",
        "search": text,
        "language": lang,
        "strictlanguage": 1,
        "type": "item",
        "limit": "1",
        "utf8": 1,
    }
    # ---
    json1: Dict[str, Any] = {}
    printe.output(f"find_name_from_wikidata: '{text}'")
    # ---
    try:
        check = session_wd[1].post(api_url, data=params, timeout=10)
        json1 = json.loads(check.text)
    except Exception as e:
        printe.output(f"<<lightred>> find_name_from_wikidata can't session.post. {e}")
    Priiint(json1)
    tab = json1.get("search", []) if json1 else []
    La: Dict[str, str] = {}
    # ---
    Priiint(len(tab))
    if len(tab) != 0:
        for x in tab:
            Priiint(x)
            if x.get("label") and x.get("match", {}).get("text"):
                if x.get("match", {}).get("type") != "alias":
                    La[x["match"]["text"]] = x["label"]
    # ---
    if La:
        printe.output(La)
    # ---
    Cashens[text] = La
    # ---
    La2: Dict[str, str] = {}
    # ---
    for tf, tf_lab in La.items():
        # ---
        if re.sub(en_literes, "", tf_lab, flags=re.IGNORECASE) != tf_lab:
            continue
        # ---
        if re.sub(ar_literes, "", tf_lab, flags=re.IGNORECASE) == tf_lab:
            continue
        # ---
        La2[tf] = tf_lab
    # ---
    return La2


def mainae() -> None:
    # ---
    pprint[1] = True
    # ---
    if sys.argv and "test" in sys.argv:
        Olist = sys.argv
        Olist.remove(sys.argv[0])
        Olist.remove("test")
        # ---
        Name = " ".join(Olist)
        printe.output(f'Name: "{Name}"')
        find_name_from_wikidata(Name, "en")
    # ---


if __name__ == "__main__":
    mainae()
# ---
