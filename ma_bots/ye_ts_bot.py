#!/usr/bin/python3
"""
from  make.ma_bots.ye_ts_bot import yementest_with_Titose_Nmaes

from ..ma_bots import ye_ts_bot


lab = ye_ts_bot.yementest_with_Titose_Nmaes()

"""

import re
import sys
from ..fix import fixtitle
from ..matables_bots.bot_2018 import pop_All_2018
from ..helps.print_bot import print_def_head, print_put
from ..pop_format import Tit_ose_Nmaes
from ..date_bots import year_lab

from ..ma_bots.ar_label_bot import find_ar_label


Find_f_wikidata = {1: False if "nowikidata" in sys.argv else True}

YTN_cash = {}
from ..matables_bots.bot import Films_O_TT, New_players


def find_lab(category, category_r):
    cate_low = category.lower()

    _lab = Films_O_TT.get(cate_low, "")

    if not _lab:
        _lab = pop_All_2018.get(cate_low, "")

    if not _lab:
        _lab = New_players.get(cate_low, "")
    if not _lab:
        _lab = year_lab.make_year_lab(cate_low)

    if _lab:
        _lab = fixtitle.fixlab(_lab, en=category_r)

        print_put(f'>>>> <<lightyellow>>test: cat "{category_r}", _lab:"{_lab}"')
        # NoLabb = False
        print_put(f'>>>> <<lightyellow>> cat:"{category_r}", _lab "{_lab}"')
    return _lab


def work_titose_nmaes(category_r, do_Get_contry2, category, Cate_test):
    arlabel = ""

    for tito, tito_name in Tit_ose_Nmaes.items():
        tito = " %s " % tito
        # if Keep_Work and category.find(tito) != -1:
        if category.find(tito) == -1:
            continue
        # ---
        arlabel = find_ar_label(category, tito, tito_name, Cate_test, category_r, do_Get_contry2=do_Get_contry2)
        # ---
        if arlabel:
            print_put('>>>> <<lightyellow>>arlabel "%s"' % arlabel)
        # ---
        break
    return arlabel


def yementest_with_Titose_Nmaes(category_r, do_Get_contry2=True):
    category = re.sub(r"_", " ", category_r)
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    cash_key = category.lower().strip()

    if cash_key in YTN_cash:
        return YTN_cash[cash_key]

    print_def_head(f"<<lightyellow>>>> ^^^^^^^^^ yementest start ^^^^^^^^^ ({category}) ")

    # if category == "women's universities and colleges":
    #     print(dadas)

    print_def_head(f'<<lightyellow>>>>>> yementest, category_r:"{category_r}", category:"{category}"')
    Cate_test = category.lower()

    # Keep_Work = True

    arlabel = pop_All_2018.get(category, "")

    if not arlabel:
        arlabel = find_lab(category, category_r)

    if not arlabel:
        arlabel = work_titose_nmaes(category_r, do_Get_contry2, category, Cate_test)

    if arlabel:
        arlabel = fixtitle.fixlab(arlabel, en=category_r)
        print_put('xxxxx <<lightyellow>>Cate_test: "%s" ' % Cate_test)
        print_put(f'>>>>>> <<lightyellow>>test: cat "{category_r}", arlabel:"{arlabel}"')

    print_def_head("<<lightyellow>>>> ^^^^^^^^^ yementest end ^^^^^^^^^ ")

    YTN_cash[cash_key] = arlabel

    return arlabel
