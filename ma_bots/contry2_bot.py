#!/usr/bin/python3
"""
python3 core8/pwb.py make/ma_bots/contry2_bot

# from ..ma_bots.contry2_bot import Get_contry2


from ..ma_bots import contry2_bot # contry2_bot.Get_contry2()


lab = contry2_bot.Get_contry2()

"""

import sys
import re
from .. import printe

from ..o_bots import fax
from ..media_bots.films_bot import test_films
from . import contry2_lab

from . import ye_ts_bot

# from ..ma_bots.contry_bot import Get_c_t_lab
from ..ma_bots import contry_bot
from ..sports_bots import team_work
from ..o_bots import bys
from ..p17_bots import nats
from ..ma_lists_bots import By_table
from ..pop_format import Tit_ose_Nmaes, Tabl_with_in, pp_start_with2, pop_format, pop_format2

from ..matables_bots.centries_bot import centries_years_dec
from ..matables_bots.bot import (
    Films_O_TT,
    New_players,
    typeTable,
)
from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.table1_bot import get_KAKO

from ..helps.print_bot import print_def_head, print_put, output_test, mainoutput

from ..date_bots import with_years_bot

from ..fromnet.wd_bot import find_wikidata

Get_contry2_done = {}
use_main_s_done = []

use_main_s = {1: True if "usemains" in sys.argv or "use_main_s" in sys.argv else False}


def Get_contry2(contry, orginal="", With_Years=True):
    if contry in Get_contry2_done:
        output_test(f'>>>> contry: "{contry}" in Get_contry2_done, lab:"{Get_contry2_done[contry]}"')
        return Get_contry2_done[contry]

    contry2 = contry.lower().strip()
    print_def_head(f'>> Get_contry2 "{contry2}":')

    cnt_la = ""

    if not cnt_la:
        cnt_la = contry2_lab.get_lab_for_contry2(contry, with_test_ye=False)

    if not cnt_la:
        #print("yementest_with_Titose_Nmaes 8")
        cnt_la = ye_ts_bot.yementest_with_Titose_Nmaes(contry2, do_Get_contry2=False)
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
    for tat_o in ti_toseslist:
        if contry2.find(tat_o) == -1:
            continue

        cnt_la = contry_2_tit(tat_o, contry, With_Years=With_Years)

        break

    if not cnt_la:
        if contry2 in use_main_s_done:
            if use_main_s[1]:
                use_main_s_done.append(contry2)
                cnt_la = find_wikidata(contry2)

        elif pop_All_2018.get(contry2.lower(), "") != "":
            cnt_la = pop_All_2018.get(contry2.lower(), "")
    if cnt_la:
        Get_contry2_done[contry] = cnt_la
        print_put(f'>> Get_ scontry2 "{contry2}": cnt_la: {cnt_la}')
        return cnt_la

    Get_contry2_done[contry] = cnt_la
    return cnt_la


def contry_2_tit(tat_o, contry, With_Years=True):
    contry2_no_lower = contry.strip()
    contry2 = contry.lower().strip()

    print_put(f'>>>> <<lightblue>> Get_contry2: <<lightyellow>> New Way to find lab for "{contry2}".')

    cnt_la = ""
    cnt_test = contry2

    con_1 = contry2.split(tat_o)[0]
    con_2 = contry2.split(tat_o)[1]

    Mash = f"^(.*?)(?:{tat_o}?)(.*?)$"

    Type_t = re.sub(Mash, r"\g<1>", contry2_no_lower, flags=re.IGNORECASE)
    contry_t = re.sub(Mash, r"\g<2>", contry2_no_lower, flags=re.IGNORECASE)

    test_N = contry2.lower().replace(con_1.strip().lower(), "")
    try:
        test_N = test_N.strip().replace(con_2.strip().lower(), "")
    except Exception:
        printe.output(f'<<lightblue>> >>>> <<lightblue>> except, test_N:"{test_N}",con_2:"{con_2}",con_1:"{con_1}"')
        test_N = re.sub(con_2.strip().lower(), "", test_N)
        test_N = test_N.replace(con_2.strip().lower(), "")

    if tat_o.strip() == "by":
        con_2 = f"by {con_2}"
        contry_t = f"by {contry_t}"

    if tat_o.strip() in ["of", "-of"]:
        Type_t = f"{Type_t} of"
        con_1 = f"{con_1} of"

    print_put(f'>>>> con_1:"{con_1.strip()}",test_N:"{test_N.strip()}",con 2:"{con_2.strip()}"')

    if test_N and test_N.strip() != tat_o.strip():
        print_put(f'>>>> <<lightblue>> test_N != "",Type_t:"{Type_t}",tat_o:"{tat_o}",contry_t:"{contry_t}"')
        con_1 = Type_t
        con_2 = contry_t

    con_1_no_lower = con_1.strip()
    con_2_no_lower = con_2.strip()

    con_1 = con_1.strip().lower()
    con_2 = con_2.strip().lower()

    print_put(f'2060 con_1:"{con_1}",con_2:"{con_2}",tat_o:"{tat_o}"')
    #
    c_1_l = pop_All_2018.get(con_1, "")

    if not c_1_l:
        c_1_l = test_films(con_1)
    if not c_1_l:
        c_1_l = nats.find_nat_others(con_1)
    if not c_1_l:
        c_1_l = fax.Get_Teams_new(con_1)
    if not c_1_l:
        c_1_l = team_work.Get_team_work_Club(con_1_no_lower)

    c_2_l = pop_All_2018.get(con_2, "")
    if c_2_l == "" and con_2.find(" by ") != -1:
        c_2_l = bys.Get_by_label(con_2)
    if not c_2_l:
        c_2_l = test_films(con_2)
    if not c_2_l:
        c_2_l = nats.find_nat_others(con_2)
    if not c_2_l:
        c_2_l = fax.Get_Teams_new(con_2)
    if c_2_l == "" and con_2.find(" and ") != -1:
        c_2_l = bys.Get_and_label(con_2)
    if not c_2_l:
        c_2_l = team_work.Get_team_work_Club(con_2_no_lower)

    if con_1 == "women" and tat_o.strip() == "from":
        c_1_l = "نساء"
        print_put(f'>> >> >> Make con_1 "{con_1}".')

    con_1_in = f"{con_1.strip()} {tat_o.strip()}"
    if not c_1_l:
        c_1_l = Tabl_with_in.get(con_1_in, "")
        if c_1_l:
            print_put(f'<<<< con_1_in "{con_1_in}", c_1_l : "{c_1_l}"')

    if not c_1_l:
        c_1_l = centries_years_dec.get(con_1, "")

    if not c_1_l:
        tst3 = re.sub(r"\d+", "", con_1.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            c_1_l = con_1

    for pri_ss, pri_lab in pp_start_with2.items():
        if not c_1_l:
            if con_1.startswith(pri_ss):
                U_c = con_1[len(pri_ss) :]
                print_put(f' pp_start_with2 <<lightblue>> con_1 :"{con_1}", U_c :"{U_c}", tat_o:"{tat_o}" ')
                U_lab = contry2_lab.get_lab_for_contry2(U_c)

                if U_lab == "" and With_Years:
                    U_lab = with_years_bot.Try_With_Years(U_c)

                if U_lab:
                    print_put(f'>>>><<lightblue>> dddd.startswith pri_ss("{pri_ss}"),U_c:"{U_c}", U_lab:"{U_lab}"')
                    c_1_l = pri_lab.format(U_lab)
                    print_put(f'>>>> c_1_l:"{c_1_l}"')

    # #pop_format
    if con_1 in pop_format:
        c_1_l = pop_format[con_1]

    # add in 4-10-2019
    if not c_1_l:
        c_1_l = contry_bot.Get_c_t_lab(con_1, "", Type="Type_lab")
    if not c_1_l:
        c_1_l = get_KAKO(con_1)
    if not c_2_l:
        c_2_l = get_KAKO(con_2)

    if not c_2_l:
        tst3 = re.sub(r"\d+", "", con_2.strip())
        test3_results = ["", "-", "–", "−"]
        if tst3 in test3_results:
            c_2_l = con_2

    if not c_2_l:
        c_2_l = test_films(con_2)
    if not c_2_l:
        c_2_l = nats.find_nat_others(con_2)
    if not c_2_l:
        c_2_l = centries_years_dec.get(con_2, "")
    if c_2_l == "" and With_Years:
        c_2_l = with_years_bot.Try_With_Years(con_2)
    if not c_2_l:
        c_2_l = contry_bot.Get_c_t_lab(con_2, "")
    # if not c_2_l:       c_2_l = pop_All_2018.get( con_2, "")
    if not c_1_l:
        output_test(f'>>>> XX--== c_1_l =  "{c_1_l}" con_1:"{con_1}" not in pop_new')

    fAAA = '>>>> XX--== <<lightgreen>> Ccon_1:"%s", lab"%s", con_2:"%s", lab"%s", cnt_test: "%s"'

    if c_2_l == "" or c_1_l == "":
        print_put(fAAA % (con_1, c_1_l, con_2, c_2_l, cnt_test))
        return ""

    cnt_test = cnt_test.replace(con_1, "").replace(con_2, "").replace(tat_o.strip(), "").strip()

    if (tat_o.strip() == "in" or con_1.endswith(" in")) and (not con_1.endswith(" في")):
        output_test(f'>>>> Add في to c_1_l : "{c_1_l}"')
        c_1_l = f"{c_1_l} في"

    elif (tat_o.strip() == "from" or con_2.endswith(" from")) and (not c_2_l.endswith(" من")):
        output_test(f'>>>> Add من to c_2_l : "{c_2_l}"')
        c_2_l = f"من {c_2_l}"

    print_put(fAAA % (con_1, c_1_l, con_2, c_2_l, cnt_test))

    sps = " "
    if tat_o.strip() == "to" and con_1.strip() == "ambassadors of":
        sps = " لدى "
    elif tat_o.strip() == "to":
        sps = " إلى "
    elif tat_o.strip() == "on":
        sps = " على "
    elif tat_o.strip() == "about":
        sps = " عن "
    elif tat_o.strip() in Tit_ose_Nmaes:
        if tat_o.strip() != "by":
            sps = f" {Tit_ose_Nmaes[tat_o.strip()]} "
    elif tat_o.strip() == "based in":
        sps = " مقرها في "

    if tat_o.strip() == "to" and c_1_l.startswith("سفراء "):
        sps = " لدى "

    if cnt_test:
        print_put(f'>>>> cnt_test:"{cnt_test}" != "" ')

    cnt_la = c_1_l + sps + c_2_l

    if con_1 in typeTable or con_1 in Films_O_TT or con_1.lower() in New_players:
        if con_1.lower() in New_players:
            if c_2_l.startswith("أصل "):
                print_put(f'>>>>>> Add من to con_1:"{con_1}" con_1 in New_players:')
                cnt_la = f"{(c_1_l + sps)}من {c_2_l}"
            else:
                print_put(f'>>>>>> Add في to con_1:"{con_1}" con_1 in New_players:')
                cnt_la += " في "
        if con_2 not in By_table:
            Films_O_TT[contry2] = cnt_la
        else:
            print_put("<<lightblue>>>>>> con_2 in By_table")

    if c_2_l:
        faxos = ""
        if not con_2.startswith("by "):
            tashr = f"{con_1} {tat_o.strip()}"
            if con_1 in pop_format:
                faxos = pop_format[con_1]
            elif tashr in pop_format:
                faxos = pop_format[tashr]
            if faxos:
                print_put(f'<<lightblue>>>>>> con_1 in pop_format "{faxos}":')
                cnt_la = faxos.format(c_2_l)

        if con_1 in pop_format2:
            print_put(f'<<lightblue>>>>>> con_1 in pop_format2 "{pop_format2[con_1]}":')
            cnt_la = pop_format2[con_1].format(c_2_l)

    print_put(f'<<lightpurple>> >>>> contry_2_tit "{contry2}": cnt_la: {cnt_la}')
    cnt_la = cnt_la.replace("  ", " ")

    maren = re.match(r"\d\d\d\d", con_2)

    if maren:
        if con_1 == "war of" and cnt_la == f"الحرب في {con_2}":
            cnt_la = f"حرب {con_2}"
            print_put(f'<<lightpurple>> >>>> change cnt_la to "{cnt_la}".')

    if cnt_la.endswith(" في "):
        cnt_la = cnt_la[: -len(" في ")]

    return cnt_la
