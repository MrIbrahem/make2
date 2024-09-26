#!/usr/bin/python3
"""

from .langs_w import Lang_work

"""

# ---
from ...ma_lists_bots import (
    All_Nat,
    Jobs_key_mens,
    languages_key,
    lang_key_m,
)
from ...helps.print_bot import output_test4, print_put

Lang_work_cash = {}


def Lang_work(con_3):
    """Process and retrieve language-related information based on input.

    This function takes a string input representing a language or a related
    term, processes it to determine the appropriate language label, and
    returns the corresponding label. It checks against predefined
    dictionaries to find matches and formats the output accordingly. The
    function also caches results for efficiency.

    Args:
        con_3 (str): A string representing a language or related term.

    Returns:
        str: The corresponding language label or an empty string if no match is
            found.
    """

    output_test4(f'<<lightblue>> Lang_work :"{con_3}"')
    lang_lab = ""
    # ---
    cash_key = con_3.lower().strip()
    # ---
    if cash_key in Lang_work_cash:
        return Lang_work_cash[cash_key]
    # ---
    if not lang_lab:
        lang_lab = languages_key.get(con_3, "")
    # ---
    tta = {"romanization of": "رومنة {}"}
    # ---
    for wriff, Wriff_lab in tta.items():
        if con_3.startswith(wriff) and lang_lab == "":
            con_43 = con_3[len(wriff) :].strip()
            lang_lac = languages_key.get(f"{con_43} language", "")
            print_put(con_43)
            if lang_lac:
                lang_lab = Wriff_lab.format(lang_lac)
                break
    # ---
    for lang, l_lab in languages_key.items():
        # ---
        if lang_lab:
            break
        # ---
        lang2 = f"{lang} "
        # ---
        lang3 = f"{lang.replace('-language', '')} films"
        if lang3 == con_3:
            lang_lab = f"أفلام ب{l_lab}"
            break
        # ---
        if con_3.startswith(lang2):
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            # ---
            if All_Nat.get(lang, False):
                nat_labe = All_Nat[lang]["mens"]
                output_test4(f'<<lightred>> skip lang:"{lang}" in All_Nat,l_lab:"{l_lab}",nat_labe:"{nat_labe}" ')
            else:
                con_8 = con_3[len(lang2) :]
                con_78_lab = Jobs_key_mens.get(con_8, "")
                if con_78_lab:
                    lang_lab = f"{con_78_lab} ب{languages_key[lang]}"  # languages_key[lang].format(con_78_lab)
                    output_test4(f'<<lightblue>> con_3.startswith_priff2("{lang2}"), lang_lab:"{lang_lab}"')
                # ---
                else:
                    con_78_lab = lang_key_m.get(con_8, "")
                    # ---
                    if con_78_lab:
                        output_test4(f'<<lightblue>> con_3.startswith_lang("{lang}"), con_78_lab:"{con_78_lab}"')
                        lang_lab = lang_key_m[con_8].format(languages_key[lang])
    # ---
    Lang_work_cash[cash_key] = lang_lab
    # ---
    return lang_lab
