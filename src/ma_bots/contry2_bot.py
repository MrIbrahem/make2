#!/usr/bin/python3
"""
python3 core8/pwb.py make/ma_bots/contry2_bot

# from ..ma_bots.contry2_bot import Get_contry2


from ..ma_bots import contry2_bot # contry2_bot.Get_contry2()


lab = contry2_bot.Get_contry2()

"""

import sys
from typing import Dict, List
from . import contry2_lab

from . import ye_ts_bot
from .c2_bots.contry2_tit_bt import contry_2_tit

from ..matables_bots.bot_2018 import pop_All_2018

from ..helps.print_bot import print_def_head, print_put, output_test

from ..fromnet.wd_bot import find_wikidata

Get_contry2_done: Dict[str, str] = {}
use_main_s_done: List[str] = []

use_main_s: Dict[int, bool] = {1: "usemains" in sys.argv or "use_main_s" in sys.argv}


def country_2_title_work(country: str, With_Years: bool = True) -> str:

    ti_toseslist = [
        " based in ",
        " in ",
        " by ",
        " about ",
        " to ",
        "-of ",
        " of ",
        " from ",
        " at ",
        " on ",
    ]
    resolved_label = ""
    for tat_o in ti_toseslist:
        if tat_o not in country:
            continue

        resolved_label = contry_2_tit(tat_o, country, With_Years=With_Years)

        break
    return resolved_label


def Get_contry2(contry: str, orginal: str = "", With_Years: bool = True) -> str:
    """Retrieve information related to a specified country."""

    if contry in Get_contry2_done:
        output_test(f'>>>> contry: "{contry}" in Get_contry2_done, lab:"{Get_contry2_done[contry]}"')
        return Get_contry2_done[contry]

    normalized_country = contry.lower().strip()
    print_def_head(f'>> Get_contry2 "{normalized_country}":')

    resolved_label = contry2_lab.get_lab_for_contry2(contry, with_test_ye=False)

    if not resolved_label:
        resolved_label = country_2_title_work(normalized_country, With_Years=With_Years)

    if not resolved_label:
        resolved_label = ye_ts_bot.translate_general_category(normalized_country, do_Get_contry2=False)

    if not resolved_label:
        if normalized_country in use_main_s_done:
            if use_main_s[1]:
                use_main_s_done.append(normalized_country)
                resolved_label = find_wikidata(normalized_country)

        elif pop_All_2018.get(normalized_country.lower(), "") != "":
            resolved_label = pop_All_2018.get(normalized_country.lower(), "")

    if resolved_label:
        Get_contry2_done[contry] = resolved_label
        print_put(f'>> Get_ scontry2 "{normalized_country}": resolved_label: {resolved_label}')
        return resolved_label

    Get_contry2_done[contry] = resolved_label
    return resolved_label
