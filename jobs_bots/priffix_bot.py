#!/usr/bin/python3
"""
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
"""
# from ma_lists.test_4_list import New_2018_For_kkk, New_2018_men_Keys_with_all, New_2018_men_Keys_without_all, New_2018_for_women_Keys_with_all, New_2018_for_women_without_al_Keys, change_male_to_female, priffix_lab_for_2018, Main_priffix, Main_priffix_to, Multi_sport_for_Jobs

from ma_lists.Nationality import Nat_mens
from ma_lists.Jobs import (
    Jobs_key_mens,
    Jobs_key_womens,
    womens_Jobs_2017,
    Female_Jobs,
)
from ma_lists.by_type import By_table
from ma_lists.test_4_list import replace_labels_2022, change_male_to_female, Mens_suffix, Mens_priffix, Women_s_priffix

from ..matables_bots.bot_2018 import pop_All_2018
from ..helps.print_bot import output_test4

priffix_Mens_work_cash = {}
priffix_woMens_work_cash = {}


def priffix_Mens_work(con_33):
    # ---
    cash_key = con_33.lower().strip()
    # ---
    if cash_key in priffix_Mens_work_cash:
        return priffix_Mens_work_cash[cash_key]
    # ---
    output_test4(f'<<lightblue>> --- start: priffix_Mens_work :"{con_33}"')
    con_33_lab = ""
    # ---
    if not con_33_lab:
        con_33_lab = By_table.get(con_33, "")
        if con_33_lab:
            priffix_Mens_work_cash[cash_key] = con_33_lab
            # ---
            return con_33_lab
        # ---
        # ينتج تصنيفات مثل : tab[Category:American research food] = "تصنيف:طعام بحثي أمريكيون"
        # con_33_lab = New_male_keys.get(con_33 , "")
        # if con_33_lab : return con_33_lab
    # ---
    if not con_33_lab:
        con_33_lab = Jobs_key_mens.get(con_33, "")
        if con_33_lab:
            output_test4(f'<<lightblue>> Jobs_key_mens: con_33_lab:"{con_33_lab}"')
    # ---
    for priff, priff_lab in Mens_priffix.items():
        if con_33_lab:
            break
        # ---
        pri = f"{priff} "

        if not con_33.startswith(pri):
            continue
        # ---
        con_8 = con_33[len(pri) :]
        con_88 = con_8
        # ---
        if con_8.endswith(" people"):
            con_nat = con_8[: -len(" people")]
            if Nat_mens.get(con_nat):
                con_88 = con_nat
        con_88 = con_88.strip()
        # ---
        output_test4(f'<<lightblue>> con_8:{con_8}, con_88:"{con_88}"')
        # ---
        output_test4(f'<<lightblue>> con_33.startswith pri ("{pri}"), con_88:"{con_88}"')
        # ---
        con_8_lab = Jobs_key_mens.get(con_88, "")
        if not con_8_lab:
            con_8_lab = Nat_mens.get(con_88, "")
        # ---
        # stoped at: 24-02-2022.
        if con_88 in Female_Jobs and priff_lab in change_male_to_female:
            priff_lab = change_male_to_female[priff_lab]
        # ---
        if con_8_lab:
            output_test4(f'<<lightblue>> priffix_Mens_work: pri("{pri}"), con_88:{con_88}, con_8_lab:"{con_8_lab}"')
            con_33_lab = priff_lab.format(con_8_lab)
            # ---
            # TAJO = Men_Womens_with_nato.get(con_8 , False )
            # if TAJO and TAJO["mens"].find("{nato}")  != -1 :
            # con_33_lab = priff_lab.format(TAJO["mens"]) #TAJO["womens"]#.format(nato = con_8_lab )
            # output_test4('<<lightblue>> TAJO["womens"]: has {nato} "%s"' %   TAJO["womens"])
            # ---
            if con_33_lab in replace_labels_2022:
                con_33_lab = replace_labels_2022[con_33_lab]
                output_test4(f'<<lightgreen>> change con_33_lab to "{con_33_lab}" replace_labels_2022.')
            # ---
            output_test4(f'<<lightblue>> con_33_lab: "{con_33_lab}"')
    # ---
    for suffix, suf_lab in Mens_suffix.items():
        if con_33_lab:
            break
        # ---
        suffix2 = f" {suffix}"
        if not con_33.endswith(suffix2):
            continue
        # ---
        con_8 = con_33[: -len(suffix2)]
        con_88 = con_8
        # ---
        if con_8.endswith(" people"):
            con_nat = con_8[: -len(" people")]
            if Nat_mens.get(con_nat):
                con_88 = con_nat
        con_88 = con_88.strip()
        # ---
        output_test4(f'<<lightblue>> con_33.endswith suffix2("{suffix2}"), con 88:"{con_88}"')
        # ---
        # con_88_lab = Jobs_key_mens.get(con_88,"")
        # if not con_88_lab:
        con_88_lab = Nat_mens.get(con_88, "")
        # ---
        if not con_88_lab:
            con_88_lab = pop_All_2018.get(con_88) or pop_All_2018.get(con_8) or ""
        # ---
        if con_88_lab:
            output_test4(f'<<lightblue>> con_33.startswith_suffix2("{suffix2}"), con_88_lab:"{con_88_lab}"')
            con_33_lab = suf_lab.format(con_88_lab)
            # ---
            output_test4(f'<<lightblue>> con_33_lab "{con_33_lab}"')
    # ---
    output_test4(f'<<lightblue>> ----- end: priffix_Mens_work :con_33_lab:"{con_33_lab}",con_33:"{con_33}"..')
    # ---
    priffix_Mens_work_cash[cash_key] = con_33_lab
    # ---
    return con_33_lab


def Women_s_priffix_work(con_3):
    # ---
    cash_key = con_3.lower().strip()
    # ---
    if cash_key in priffix_woMens_work_cash:
        return priffix_woMens_work_cash[cash_key]
    # ---
    f_lab = ""
    # output_test4('<<lightblue>> Womens priffix work :"%s"' % con_3)
    # ---
    if not f_lab:
        f_lab = Jobs_key_womens.get(con_3, "")
    # ---
    con_33 = con_3
    if con_3.endswith(" women"):
        con_33 = con_3[: len(" women")]
    # ---
    for wriff, wrifflab in Women_s_priffix.items():
        if f_lab:
            break
        Wriff2 = f"{wriff} "
        if wriff == "women's":
            Wriff2 = "women's-"
        if con_33.startswith(Wriff2):
            con_4 = con_33[len(Wriff2) :]
            con_8_Wb = womens_Jobs_2017.get(con_4, "")
            output_test4(f'<<lightblue>> con_33.startswith_Wriff2("{Wriff2}"),con_4:"{con_4}", con_8_Wb:"{con_8_Wb}"')
            if con_8_Wb:
                f_lab = wrifflab.format(con_8_Wb)
                # ---
                # TAJO = Men_Womens_with_nato.get(con_4 , False )
                # if TAJO and TAJO["womens"].find("{nato}")  != -1 :
                # f_lab = TAJO["womens"]#.format(nato = f_lab )
                # f_lab = wrifflab.format(TAJO["womens"])
                # output_test4('<<lightblue>> TAJO["womens"]: has {nato} "%s"' %   TAJO["womens"])
                # ---
    # ---
    priffix_woMens_work_cash[cash_key] = f_lab
    # ---
    return f_lab
