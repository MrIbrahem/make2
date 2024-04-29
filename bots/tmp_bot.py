"""
from  make2.bots import tmp_bot
if not sub_ar_label:
    sub_ar_label = tmp_bot.Work_Templates(category)
"""

from ..pop_format import pp_start_with, pp_ends_with, pp_ends_with_pase
from ..helps.print_bot import print_put

from ..date_bots.year_lab2 import Try_With_Years

# from make2.ma_bots.contry2_bot import Get_contry2
from ..ma_bots.contry2_lab import get_lab_for_contry2
from ..ma_bots.ye_ts_bot import yementest_with_Titose_Nmaes

Work_Templates_cash = {}


def Work_Templates(SUUS):
    # ---
    cash_key = SUUS.lower().strip()
    # ---
    if cash_key in Work_Templates_cash:
        return Work_Templates_cash[cash_key]
    # ---
    print_put(f">> ----------------- start Work_ Templates ----------------- SUUS:{SUUS}")
    PpP_lab = ""
    # pp_ends_with =  in pop_format

    # pp_ends_with_pase
    # pp_ends_with
    # merege pp_ends_with_pase and pp_ends_with
    meregd = {**pp_ends_with_pase, **pp_ends_with}

    for pri_ooo, pri_lll in meregd.items():
        if not SUUS.lower().endswith(pri_ooo.lower()):
            continue
        U_8 = SUUS[: -len(pri_ooo)]
        print_put(f'>>>><<lightblue>> Work_ Templates.endswith pri_ooo("{pri_ooo}"), U_8:"{U_8}"')

        U_lab = get_lab_for_contry2(U_8)
        if not U_lab:
            U_lab = Try_With_Years(U_8)

        if U_lab == "":
            U_lab = yementest_with_Titose_Nmaes(U_8)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{SUUS}", U_8 :"{U_8}"')
        # ---
        if U_lab:
            print_put(f'>>>><<lightblue>> Work_ Templates.endswith pri_ooo("{pri_ooo}"), U_lab:"{U_lab}"')
            PpP_lab = pri_lll.format(U_lab)
            print_put(f'>>>> PpP_lab:"{PpP_lab}"')
            # ---
            break

    # pp_ends_with
    if PpP_lab:
        return PpP_lab

    # pp_start_with
    for pri_ss, pri_lll in pp_start_with.items():
        if not SUUS.startswith(pri_ss):
            continue
        U_c = SUUS[len(pri_ss) :]

        U_lab = get_lab_for_contry2(U_c)

        if not U_lab:
            U_lab = Try_With_Years(U_c)

        if U_lab == "":
            U_lab = yementest_with_Titose_Nmaes(U_c)

        print_put(f'>>>><<lightblue>> Work_ Templates :"{SUUS}", U_c :"{U_c}"')
        if U_lab:
            print_put(f'>>>><<lightblue>> Work_ Templates.startswith pri_ss("{pri_ss}"), U_lab:"{U_lab}"')
            PpP_lab = pri_lll.format(U_lab)
            print_put(f'>>>> PpP_lab:"{PpP_lab}"')
            # ---
            break

    print_put(">> ----------------- end Work_ Templates ----------------- ")
    # ---
    return PpP_lab
