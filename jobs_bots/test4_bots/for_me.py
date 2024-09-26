#!/usr/bin/python3
"""
from .test4_bots.for_me import Work_for_me
"""

import re
from ...ma_lists_bots import NN_table
from ...ma_lists_bots import (
    Nat_women,
    Nat_men,
    All_contry_with_nat_ar,
)
from ...ma_lists_bots import New_female_keys, New_male_keys

from ...ma_lists_bots import New_2018_For_kkk, New_2018_men_Keys_with_all, New_2018_men_Keys_without_all, New_2018_for_women_Keys_with_all, New_2018_for_women_without_al_Keys

# ---
from ...o_bots import ethnic_bot
from ...helps.print_bot import output_test4

wo_2018_cash = {}
Work_for_me_cash = {}


def Work_for_New_2018_men_Keys_with_all(cate, nat, con_3):
    # ---
    cash_key = f"{cate}, {nat}, {con_3}".lower().strip()
    # ---
    if cash_key in wo_2018_cash:
        return wo_2018_cash[cash_key]
    # ---
    # women_nat_lab = Nat_women.get(nat, "")
    men_nat_lab = Nat_men.get(nat, "")
    # nat_lab = Nat_women[nat]
    # ---
    # output_test4('<<lightblue>>>> Work_for_me >> %s .nat:(%s), con_3:"%s", nat_lab:"%s"' % (cate , nat , con_3,nat_lab))
    # contry = nat
    contry_lab = ""
    con_3_lab = ""
    # cco_lab = ""
    # ---
    # رجالية بألف ولام التعريف
    if not con_3_lab and not contry_lab:
        con_3_lab = New_2018_men_Keys_with_all.get(con_3.strip(), "")
        # ---
        if con_3_lab:
            if nat in NN_table:
                men_nat_lab = NN_table[nat]["men"]
            men_nat_lab_no_al = re.sub(r" ", " ال", men_nat_lab)
            men_nat_lab = f"ال{men_nat_lab_no_al}"
            contry_lab = con_3_lab.format(men_nat_lab)
            output_test4(f'<<lightblue>> test_4:New_2018_men_Keys_with_all new contry_lab  "{contry_lab}" ')
    # ---
    # output_test4('<<lightblue>>>> Work_for_me >> contry_lab:"%s"' % contry_lab)
    # ---
    wo_2018_cash[cash_key] = contry_lab
    # ---
    return contry_lab


def Work_for_me(cate, nat, con_3):
    # ---
    cash_key = f"{cate}, {nat}, {con_3}".lower().strip()
    # ---
    if cash_key in Work_for_me_cash:
        return Work_for_me_cash[cash_key]
    # ---
    women_nat_lab = Nat_women.get(nat, "")
    men_nat_lab = Nat_men.get(nat, "")
    nat_lab = Nat_women[nat]
    # ---
    output_test4(f'<<lightblue>>>> Work_for_me >> {cate} .nat:({nat}), con_3:"{con_3}", nat_lab:"{nat_lab}"')
    # contry = nat
    contry_lab = ""
    con_3_lab = ""
    cco_lab = ""
    # ---
    # الإنجليزي جنسية والعربي اسم البلد
    if not con_3_lab and not contry_lab:
        con_3_lab = New_2018_For_kkk.get(con_3.strip(), "")
        if nat.strip() in All_contry_with_nat_ar:
            cco_lab = All_contry_with_nat_ar[nat.strip()].get("ar", "")
        # ---
        if con_3_lab:
            output_test4(f'<<lightblue>> Work_for_me:con_3_lab: "{con_3_lab}" ')
            if cco_lab:
                contry_lab = con_3_lab.format(cco_lab)
                output_test4(f'<<lightblue>> test_4:New_2018_for_women_without_al_Keys new contry_lab   "{contry_lab}" ')
    # ---
    # نسائية بدون ألف ولام التعريف
    if con_3_lab == "" and contry_lab == "":
        contry_lab = ethnic_bot.Ethnic(cate, nat, con_3)
    # ---
    # en_is_P17_ar_is_mens
    # mens_nat_lab = Nat_mens.get(nat, "")
    # con_3_lab = Nat_mens.get(con_3 , "")
    # if con_3_lab:
    # if Nat_mens.get(contry,""):
    # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
    # contry_lab = con_3_lab + " " + Nat_mens.get(contry,"")
    # output_test4('<<lightblue>> test Work_for_me: new contry_lab  "%s" ' % contry_lab)
    # ---
    # نسائية بدون ألف ولام التعريف
    if con_3_lab == "" and contry_lab == "":
        con_3_lab = New_2018_for_women_without_al_Keys.get(con_3.strip(), "")
        # ---
        # new 24-02-2022
        if not con_3_lab:
            con_3_lab = New_female_keys.get(con_3.strip(), "")
            if con_3_lab:
                con_3_lab += " {}"
        # ---
        if con_3_lab:
            contry_lab = con_3_lab.format(women_nat_lab)
            output_test4(f'<<lightblue>> test44:New_2018_for_women_without_al_Keys new contry_lab   "{contry_lab}" ')
    # ---
    # نسائية بألف ولام التعريف
    if con_3_lab == "" and contry_lab == "":
        con_3_lab = New_2018_for_women_Keys_with_all.get(con_3.strip(), "")
        # ---
        if con_3_lab:
            # ---
            if nat in NN_table:
                women_nat_lab = NN_table[nat]["women"]
            women_nat_lab_no_al = re.sub(r" ", " ال", women_nat_lab)
            women_nat_lab = f"ال{women_nat_lab_no_al}"
            # ---
            if con_3_lab.find("{nat}") != -1:
                contry_lab = con_3_lab.format(nat=women_nat_lab)
            else:
                contry_lab = con_3_lab.format(women_nat_lab)
            # ---
            output_test4(f'<<lightblue>> test_4:New_2018_for_women_Keys_with_all new contry_lab  "{contry_lab}" ')
    # ---
    # رجالية بدون ألف ولام التعريف
    if con_3_lab == "" and contry_lab == "":
        con_3_lab = New_2018_men_Keys_without_all.get(con_3.strip(), "")
        # ---
        # new 24-02-2022
        if not con_3_lab:
            con_3_lab = New_male_keys.get(con_3.strip(), "")
            if con_3_lab:
                con_3_lab += " {}"
        # ---
        if con_3_lab:
            contry_lab = con_3_lab.format(men_nat_lab)
            output_test4(f'<<lightblue>> test_4:New_2018_men_Keys_without_all new contry_lab    "{contry_lab}" ')
    # ---
    # رجالية بألف ولام التعريف
    if con_3_lab == "" and contry_lab == "":
        contry_lab = Work_for_New_2018_men_Keys_with_all(cate, nat, con_3)
    # ---
    # output_test4('<<lightblue>>>> Work_for_me >> contry_lab:"%s"' % contry_lab)
    # ---
    Work_for_me_cash[cash_key] = contry_lab
    # ---
    return contry_lab
