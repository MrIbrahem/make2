#!/usr/bin/python3
"""

# from ..ma_bots.contry_bot import Get_contry, Get_c_t_lab


from ..ma_bots import contry_bot


lab = contry_bot.Get_contry()

"""
import sys
import re

from . import ye_ts_bot

from ..date_bots import with_years_bot
from ..p17_bots import nats
from ..sports_bots import team_work

from ..media_bots.films_bot import test_films

from . import contry2_bot  # contry2_bot.Get_contry2()

from . import contry2_lab
from ..ma_lists_bots import Sports_Keys_For_Label
from ..ma_lists_bots import Nat_mens
from ..ma_lists_bots import New_female_keys

from ..matables_bots.bot import Add_to_main2_tab
from ..helps.print_bot import print_put, output_test

from ..fromnet.wd_bot import find_wikidata
from ..matables_bots.centries_bot import centries_years_dec
from ..ma_lists_bots import pop_of_without_in
from ..ma_lists_bots import Jobs_key
from ..matables_bots.bot_2018 import pop_All_2018

Get_contry_done = {}


def Get_contry(contry, do_Get_contry2=True):
    """Retrieve the label for a given country name.

    This function takes a country name as input and attempts to retrieve its
    corresponding label from various sources. It first checks if the country
    has already been processed and stored in a cache. If not, it attempts to
    derive the label through several methods, including checking against
    predefined keys, utilizing helper functions, and applying specific
    prefixes. The function also handles cases where the country name may
    contain additional descriptors or is formatted in a certain way.

    Args:
        contry (str): The name of the country to retrieve the label for.
        do_Get_contry2 (bool): A flag indicating whether to attempt a secondary retrieval method
            if the initial attempts fail. Defaults to True.

    Returns:
        str: The label corresponding to the input country name, or an empty string if
            no label
            could be found.
    """

    contry_no_lower = contry
    contry = contry.lower()

    if contry in Get_contry_done:
        output_test(f'>>>> Get_contry: "{contry}" in Get_contry_done, lab:"{Get_contry_done[contry]}"')
        return Get_contry_done[contry]

    output_test(">> ----------------- Get_contry start ----------------- ")
    print_put(f'>>>> Get contry for "{contry}"')
    cnt_la = contry if contry.strip().isdigit() else ""
    if not cnt_la:
        cnt_la = New_female_keys.get(contry, "")
    if not cnt_la:
        cnt_la = test_films(contry_no_lower)
    if not cnt_la:
        cnt_la = nats.find_nat_others(contry_no_lower)
    if not cnt_la:
        cnt_la = team_work.Get_team_work_Club(contry_no_lower)

    if cnt_la == "" and do_Get_contry2:
        # cnt_la = contry2_lab.get_lab_for_contry2(contry)
        cnt_la = contry2_bot.Get_contry2(contry)
    # جديدة!
    # if cnt_la == "":
    #     cnt_la = ye_ts_bot.translate_general_category(contry)

    if not cnt_la:
        Preffix = {
            "women's ": "نسائية",
            "men's ": "رجالية",
            "fasa ": "فاسااا",
            "non-combat ": "غير قتالية",
            # "expatriate " : "مغتربون",
        }

        for prif, prif_lab in Preffix.items():
            if not contry.startswith(prif):
                continue
            print(f">>> contry.startswith({prif})")
            con_3 = contry[len(prif):]
            Add_to_main2_tab(prif, prif_lab)
            con_3_lab = contry2_bot.Get_contry2(con_3)

            if con_3_lab == "":
                con_3_lab = contry2_lab.get_lab_for_contry2(con_3)

            if con_3_lab == "":
                # print("translate_general_category 6")
                con_3_lab = ye_ts_bot.translate_general_category(con_3)

            if con_3_lab:
                Add_to_main2_tab(con_3, con_3_lab)
                cnt_la = f"{con_3_lab} {prif_lab}"
                print_put(f'>>>>>> xxx new cnt_la  "{cnt_la}" ')
                break

    OKay = True

    if cnt_la == "" and OKay:
        ti_toseslist = [
            " by ",
            " based in ",
            " in ",
            " about ",
            "-of ",
            " of ",
            " from ",
            " to ",
            " at ",
            " on ",
        ]

        for ttt in ti_toseslist:
            if contry.find(ttt) != -1:
                OKay = False
                break

    if cnt_la == "" and OKay:
        Preffix2 = {
            "defunct national ": "{} وطنية سابقة",
            # "defunct " : "{} سابقة",
        }

        for prif, prif_lab in Preffix2.items():
            if not contry.startswith(prif):
                continue
            print(f">>> contry.startswith({prif})")
            con_3 = contry[len(prif):]
            con_3_lab = contry2_bot.Get_contry2(con_3)

            if con_3_lab == "":
                con_3_lab = contry2_lab.get_lab_for_contry2(con_3)

            if con_3_lab == "":
                # print("translate_general_category 7")
                con_3_lab = ye_ts_bot.translate_general_category(con_3)

            if con_3_lab:
                Add_to_main2_tab(con_3, con_3_lab)
                cnt_la = prif_lab.format(con_3_lab)
                if con_3_lab.strip().endswith(" في") and prif == "defunct ":
                    cnt_la = f'{con_3_lab.strip()[:-len(" في")]} سابقة في'
                print_put(f'>>>>>> cdcdc new cnt_la  "{cnt_la}" ')
                break

    if cnt_la:
        if cnt_la.find("سنوات في القرن") != -1:
            cnt_la = re.sub(r"سنوات في القرن", "سنوات القرن", cnt_la)

    if not cnt_la:
        RE1 = re.match(r"^(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d).*", contry)
        RE2 = re.match(r"^.*?\s*(\d+\-\d+|\d+\–\d+|\d+\−\d+|\d\d\d\d)$", contry)
        RE3 = re.match(r"^.*?\s*\((\d+\-\d+|\d+\–\d+|\d+\–present|\d+\−\d+|\d\d\d\d)\)$", contry)

        if RE1 or RE2 or RE3:
            cnt_la = with_years_bot.Try_With_Years(contry)

    if cnt_la == "" and contry.endswith(" members of"):
        contry2 = contry.replace(" members of", "")
        cnt_la = Nat_mens.get(contry2, "")
        if cnt_la:
            cnt_la = f"{cnt_la} أعضاء في  "
            print_put(f"a<<lightblue>>>2021 Get_contry lab = {cnt_la}")

    if not cnt_la:
        cnt_la = Sports_Keys_For_Label.get(contry, "")

    Get_contry_done[contry] = cnt_la
    output_test(f'>>>> Get contry "{cnt_la}"')
    output_test(">> ----------------- end Get_contry ----------------- ")
    return cnt_la


def Get_c_t_lab(c_t_lower, tito, Type="", do_Get_contry2=True):
    """Retrieve the corresponding label for a given country or term.

    This function attempts to find a label associated with the input
    `c_t_lower`, which may represent a country or other geographical term.
    It utilizes various lookup mechanisms, including predefined dictionaries
    and regular expressions, to derive the appropriate label. The function
    also considers the context provided by the `tito` parameter and the
    `Type` argument to refine its search. If no label is found, it may
    recursively call itself to handle specific cases.

    Args:
        c_t_lower (str): The input string representing a country or term.
        tito (str): Contextual information that may influence the label retrieval.
        Type (str?): Specifies the type of label to retrieve. Defaults to an empty string.
        do_Get_contry2 (bool?): A flag indicating whether to perform additional country lookups.
            Defaults to True.

    Returns:
        str: The label corresponding to the input term, or an empty string if no
            label is found.
    """

    print_put(f'Get_c_t_lab Type:"{Type}", tito:"{tito}", c_ct_lower:"{c_t_lower}" ')
    if "makeerr" in sys.argv:
        do_Get_contry2 = True

    test_3 = re.sub(r"\d+", "", c_t_lower.strip())
    test3_results = ["", "-", "–", "−"]
    c_t_lab = c_t_lower if test_3 in test3_results else ""
    if not c_t_lab:
        c_t_lab = New_female_keys.get(c_t_lower, "")
    if not c_t_lab:
        c_t_lab = centries_years_dec.get(c_t_lower, "")

    if c_t_lab == "" and Type != "Type_lab":
        if c_t_lower.startswith("the "):
            print_put(f'>>>> c_t_lower:"{c_t_lower}" startswith("the ")')
            LLL = c_t_lower[len("the "):]

            c_t_lab = pop_All_2018.get(LLL, "")

            if not c_t_lab:
                c_t_lab = Get_contry(LLL, do_Get_contry2=do_Get_contry2)

    if not c_t_lab:
        if re.sub(r"\d+", "", c_t_lower) == "":
            c_t_lab = c_t_lower
        else:
            c_t_lab = centries_years_dec.get(c_t_lower, "")

    if c_t_lab == "":
        c_t_lab = Get_contry(c_t_lower, do_Get_contry2=do_Get_contry2)

    if c_t_lab == "" and Type == "Type_lab":
        tatos = [" of", " in", " at"]

        for tat in tatos:
            if c_t_lab:
                break

            if not c_t_lower.endswith(tat):
                continue

            tti = c_t_lower[:-len(tat)]

            tto = Jobs_key.get(tti, "")

            print_put(f'tti:"{tti}", tto:"{tto}", c_t_lower:"{c_t_lower}" ')

            if c_t_lab == "" and tto:
                c_t_lab = f"{tto} من "
                print_put(f"Jobs_key:: add من to c_t_lab:{c_t_lab}, line:1583.")

            if not tto:
                tto = pop_All_2018.get(tti, "")

            if not tto:
                tto = Get_contry(tti, do_Get_contry2=do_Get_contry2)

            if c_t_lab == "" and tto:
                if c_t_lower in pop_of_without_in:
                    c_t_lab = tto
                    print_put("skip add في to pop_of_without_in")
                else:
                    c_t_lab = f"{tto} في "
                    print_put(f"XX add في to c_t_lab:{c_t_lab}, line:1596.")
                break
        if c_t_lab == "" and tito.strip() == "in":
            c_t_lab = pop_All_2018.get(f"{c_t_lower} in", "")

        if not c_t_lab:
            c_t_lab = Get_contry(c_t_lower, do_Get_contry2=do_Get_contry2)

    if not c_t_lab:
        c_t_lab = find_wikidata(c_t_lower)

    if c_t_lab:
        print_put(f'Get_c_t_lab c_t_lab:"{c_t_lab}" ')

    elif tito.strip() == "for" and c_t_lower.startswith("for "):
        return Get_c_t_lab(c_t_lower[len("for "):], "", Type=Type)

    return c_t_lab
