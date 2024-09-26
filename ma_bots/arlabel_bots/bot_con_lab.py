#!/usr/bin/python3
"""
from .arlabel_bots.bot_con_lab import get_con_lab

"""

import sys

from .. import contry2_lab
from ...sports_bots import team_work
from ...date_bots import year_lab

from ...bots import tmp_bot
from ...o_bots import bys
from ...p17_bots import nats

from ...media_bots.films_bot import test_films

from ...ma_lists_bots import pop_final_all_keys2
from ...ma_lists_bots import New_P17_Finall
from ...ma_lists_bots import New_female_keys

from ...fromnet.wd_bot import find_wikidata
from ...fromnet import kooora
from ...pop_format_bot import for_table

from ...matables_bots.bot_2018 import pop_All_2018


from ...helps.print_bot import print_put

from ..contry_bot import Get_contry, Get_c_t_lab

Find_f_wikidata = {1: False if "nowikidata" in sys.argv else True}


def get_con_lab(tito, do_Get_contry2, tito2, contry, contry_lower):
    """Retrieve the corresponding label for a given country.

    This function attempts to find a label associated with the specified
    country by checking various data sources in a specific order. It first
    checks if a label exists in predefined dictionaries and makes
    adjustments to the country name if necessary. If no label is found, it
    tries to derive a label based on the country name's structure or related
    information. The function also handles specific cases such as names
    starting with "by" or containing "kingdom-of".

    Args:
        tito (str): A parameter used in label retrieval.
        do_Get_contry2 (bool): A flag indicating whether to perform a secondary
            country lookup.
        tito2 (str): A parameter that influences the retrieval process.
        contry (str): The original country name.
        contry_lower (str): The lowercase version of the country name for
            consistent lookup.

    Returns:
        str: The label corresponding to the provided country name, or an
            empty string if no label is found.
    """

    con_lab = ""

    if not con_lab:
        con_lab = New_P17_Finall.get(contry_lower, "")
    if not con_lab:
        con_lab = pop_final_all_keys2.get(contry_lower, "")
    if not con_lab:
        con_lab = pop_All_2018.get(contry_lower, "")
    if not con_lab:
        con_lab = pop_All_2018.get(contry_lower.replace("-", " "), "")
    if not con_lab:
        con_lab = New_female_keys.get(contry_lower.replace("-", " "), "")

    if con_lab == "" and contry_lower.find("kingdom-of") != -1:
        con_lab = pop_All_2018.get(contry_lower.replace("kingdom-of", "kingdom of"), "")

    if con_lab == "" and contry_lower.startswith("by "):
        con_lab = bys.Make_By_lab(contry_lower)

    if con_lab == "" and contry_lower.find(" by ") != -1:
        con_lab = bys.Get_by_label(contry_lower)

    if tito2 == "for":
        con_lab = for_table.get(contry_lower, "")

    if con_lab == "" and contry_lower.strip().startswith("in "):
        cco2 = contry_lower.strip()[len("in ") :].strip()

        cco2_ = Get_contry(cco2)

        if not cco2_:
            cco2_ = contry2_lab.get_lab_for_contry2(cco2)

        if cco2_:
            con_lab = "في " + cco2_

    if not con_lab:
        con_lab = year_lab.make_month_lab(contry_lower)
    if not con_lab:
        con_lab = test_films(contry)
    if not con_lab:
        con_lab = nats.find_nat_others(contry)
    if not con_lab:
        con_lab = team_work.Get_team_work_Club(contry.strip())

    if not con_lab:
        con_lab = Get_c_t_lab(contry_lower, tito, do_Get_contry2=do_Get_contry2)

    if not con_lab:
        con_lab = tmp_bot.Work_Templates(contry_lower)

    if not con_lab:
        con_lab = contry2_lab.get_lab_for_contry2(contry_lower)

    if not con_lab:
        con_lab = find_wikidata(contry_lower)
    if not con_lab:
        con_lab = kooora.kooora_team(contry_lower, Local=Find_f_wikidata[1])

    print_put(f"?????? get_con_lab: {contry_lower=}, {con_lab=}")

    return con_lab
