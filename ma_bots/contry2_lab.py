#!/usr/bin/python3
"""
python3 core8/pwb.py make2/ma_bots/contry2_bot

# from make2.ma_bots.contry2_lab import get_lab_for_contry2


"""

from . import fax
from .films_bot import test_films

from make2.bots import team_work
from make2.bots import nats
from make2.matables_bots.centries_bot import centries_years_dec

from make2.matables_bots.bot_2018 import pop_All_2018
from make2.matables_bots.table1_bot import get_KAKO

from make2.helps.print_bot import print_put, mainoutput


from make2.bots.us_stat import Work_US_State
from make2.bots.rele import Work_relations
from make2.bots.popl import Work_peoples
from make2.bots import univer

# from .ye_ts_bot import yementest_with_Titose_Nmaes


def Get_team_work_Club(s):
    lab = ""

    slab = team_work.Get_Club(s, out=mainoutput[1], return_tab=True)

    if isinstance(slab, str):
        return slab

    lab = slab.get("lab", "")

    return lab


def get_lab_for_contry2(contry, **kwargs):
    contry2_no_lower = contry.strip()
    contry2 = contry.lower().strip()
    cnt_la = pop_All_2018.get(contry2, "")

    if not cnt_la:
        cnt_la = test_films(contry2)
    if not cnt_la:
        cnt_la = nats.find_nat_others(contry2)
    if not cnt_la:
        cnt_la = fax.Get_Teams_new(contry2)
    if not cnt_la:
        cnt_la = Get_team_work_Club(contry2_no_lower)
    if not cnt_la:
        cnt_la = Work_relations(contry2)
    if not cnt_la:
        cnt_la = univer.test_Universities(contry2, print_put)
    if not cnt_la:
        cnt_la = Work_US_State(contry2)
    if not cnt_la:
        cnt_la = Work_peoples(contry2)
    if not cnt_la:
        cnt_la = get_KAKO(contry2)

    if not cnt_la:
        cnt_la = centries_years_dec.get(contry2, "")

    if cnt_la == "" and contry2.startswith("the "):
        cnt_la = pop_All_2018.get(contry2[len("the ") :], "")

    # if cnt_la == "" and yementest_with_Titose_Nmaes:
    #     cnt_la = yementest_with_Titose_Nmaes(contry2, do_Get_contry2=False)

    if cnt_la:
        print_put(f'>> get_lab_for_contry2 "{contry2}": cnt_la: {cnt_la}')

    return cnt_la
