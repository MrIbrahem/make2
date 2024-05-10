#!/usr/bin/python3
"""
Usage:
from ..ma_bots import event2bot
# category_lab = event2bot.event2(category_r)

"""


import re
from .. import printe
import sys

from pathlib import Path

Dir_ma = Path(__file__).parent.parent
from ..fix import fixtitle
from ..bots import tmp_bot
from ..date_bots import year_lab
from ..date_bots import with_years_bot
from .lab_seoo_bot import event_Lab_seoo
from ..o_bots import univer  # univer.test_Universities(cate, print_def=printo)

from ..pop_format import Tit_ose_Nmaes, NewFormat, ar_lab_before_year_to_add_in, contry_before_year
from ma_lists.Nationality import Nat_mens
from ..matables_bots.bot import Add_to_main2_tab  # Add_to_main2_tab()
from ..matables_bots.bot import (
    New_Lan,
    Films_O_TT,
    New_players,
    typeTable,
    Table_for_frist_word,
    Add_in_table,
    Keep_it_frist,
    safo,
    titttto,
    add_in_to_contry,
    type_after_contry,
)
from ..matables_bots.bot_2018 import pop_All_2018
from ..helps.print_bot import print_put, output_test
from .contry_bot import Get_contry

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
event2_cash = {}

Find_stubs = {1: True if "-stubs" in sys.argv else False}


def work_2019(category3, year, year_labe):
    print_put(f'<<lightyellow>>>> ============ start work_2019 :"{category3}", year:"{year}" ============ ')
    cat_4 = re.sub(year + r"\s*(.*)$", r"\g<1>", category3)
    cat_4 = cat_4.strip()
    print_put('<<lightgreen>>>>>> 2019: NoLab and year, cat_4="%s"' % cat_4)
    cat4_lab = pop_All_2018.get(cat_4, "")
    if not cat4_lab:
        cat4_lab = Get_contry(cat_4)

    arlabel = ""
    if cat4_lab:
        print_put('<<lightgreen>>>>>> cat4_lab = "%s"' % cat4_lab)
        # cat_4_in_Table = False
        for table, ta_t in Table_for_frist_word.items():
            if cat_4 in ta_t:
                # cat_4_in_Table = True
                print_put(f'X:<<lightpurple>>>>>> cat_4 "{cat_4}" in {table}.')

        if cat_4 in New_players:
            arlabel = cat4_lab + " في " + year_labe
        elif cat4_lab.endswith(" في"):
            arlabel = cat4_lab + " " + year_labe
        else:
            arlabel = year_labe + " " + cat4_lab

        print_put('<<lightgreen>>>>>> 2019: New arlabel :"%s" ' % arlabel)
        print_put("<<lightyellow>>>> ^^^^^^^^^ end work_2019 ^^^^^^^^^ ")
    # ---
    return arlabel


def event2(category_r):
    cash_key = category_r.replace("category:", "").lower().strip()

    if cash_key in event2_cash:
        return event2_cash[cash_key]
    print_put("<<lightblue>>>> vvvvvvvvvvvv event2 start vvvvvvvvvvvv ")
    print_put('<<lightyellow>>>>>> event2 :"%s"' % category_r)
    yy = (
        r"\d+th century BCE|\d+th millennium BCE|\d+th century BC|\d+th millennium BC|\d+th century|\d+th millennium"
        + r"|\d+st century BCE|\d+st millennium BCE|\d+st century BC|\d+st millennium BC|\d+st century|\d+st millennium"
        + r"|\d+rd century BCE|\d+rd millennium BCE|\d+rd century BC|\d+rd millennium BC|\d+rd century|\d+rd millennium"
        + r"|\d+nd century BCE|\d+nd millennium BCE|\d+nd century BC|\d+nd millennium BC|\d+nd century|\d+nd millennium"
        + r"|\d+ century BCE|\d+ millennium BCE|\d+ century BC|\d+ millennium BC"
        + r"|\d+ century|\d+ millennium|\d+s BCE|\d+ BCE|\d+s BC|\d+ BC"
    )
    en_dash = r"|\d+\–\d+"
    MINUS = r"|\d+\−\d+"
    keybord = r"|\d+\-\d+"
    yy += en_dash
    yy += MINUS
    yy += keybord
    yy += r"|\d+s"
    yy += r"|\d+"
    # yyx = r"(\w+\s*\d+|\d+(th|st|rd)|\d+s\s*|\d+|)(\s*BCE|\s*BC|)(\s*century|\s*millennium)"
    MONTHSTR2 = "(january |february |march |april |may |june |july |august |september |october |november |december |)"
    tita_year = r"Category\:" + MONTHSTR2 + "(" + yy + "|).*"
    tita_year = tita_year.lower()
    tita_other = r"\s*(" + safo + r"|)\s*(" + titttto + r"|)\s*(.*|).*"
    tita = r"Category\:" + MONTHSTR2 + "(" + yy.lower() + "|)" + tita_other
    tita = tita.lower()
    # tit = {}
    NoLab_list = {}
    ar_label = ""
    ar_label = univer.test_Universities(category_r, print_put)
    if category_r and ar_label == "":
        Add_In_Done = False
        NoLab = False

        category = category_r
        category = category.replace("−century", " century")
        category = category.replace("–century", " century")
        if not category.lower().startswith("category:"):
            category = "Category:" + category

        Tita_year = tita_year
        test_month = re.sub(
            r"category\:(january|february|march|april|may|june|july|august|september|october|november|december|)\s*",
            "",
            category.lower(),
        )

        if test_month == category:
            Tita_year = r"category\:(|)\s*(" + yy + ").*"
        Tita_year = Tita_year.lower()

        _category_ = category
        category2 = category.lower()
        if category2.startswith("category:"):
            category2 = category2[len("category:") :]
        _category_ = re.sub(r"-century", " century", _category_)
        _category_ = re.sub(r"-millennium", " millennium", _category_)

        category3_not_lower = re.sub(r"category:", "", _category_, flags=re.IGNORECASE)

        _category_ = _category_.lower()
        category3 = re.sub(r"category:", "", _category_, flags=re.IGNORECASE)
        cat_test = category3

        print_put('<<lightred>>>>>> category33:"%s" ' % category3)
        category_lab = ""

        cat3 = category3
        if not category_lab:
            if cat3.find(" in ") == -1 and cat3.find(" of ") == -1 and cat3.find(" from ") == -1:
                if cat3.find(" by ") == -1 and cat3.find(" at ") == -1:
                    if re.sub(r"^\d", "", cat3) == cat3:
                        category_lab = Get_contry(category3_not_lower)

                    else:
                        category_lab = with_years_bot.Try_With_Years(category3)
                        if category_lab:
                            category_lab = "تصنيف:" + category_lab

        if category_lab:
            if re.sub(en_literes, "", category_lab, flags=re.IGNORECASE) == category_lab:
                category_lab = fixtitle.fixlab(category_lab, en=category_r)
                print_put(f'>>>> <<lightyellow>> cat:"{_category_}", category_lab "{category_lab}"')
                print_put("<<lightblue>>>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
                event2_cash[cash_key] = category_lab
                return category_lab
        else:
            year = re.sub(Tita_year, r"\g<1>\g<2>", _category_)
            typeo = re.sub(tita, r"\g<3>", _category_)
            if year == _category_ or year == category3:
                year = ""
            elif year and _category_.startswith("category:" + year):
                cat_test = cat_test.replace(year.lower(), "")
                tita_n = "category:" + year + tita_other

                typeo = re.sub(tita_n, r"\g<1>", _category_)

            if typeo == _category_ or typeo == category3:
                typeo = ""
            In = re.sub(tita, r"\g<4>", _category_)
            if In == _category_ or In == category3:
                In = ""
            contry = re.sub(tita, r"\g<5>", _category_)
            if contry == _category_ or contry == category3:
                contry = ""

            if In.strip() == "by":
                contry = f"by {contry}"

            contry_not_lower = contry
            contry = contry.lower()
            print_put(f'>>>> year:"{year}", typeo:"{typeo}", In:"{In}", contry:"{contry}"')
            arlabel = ""
            year_labe = ""
            suf = ""
            typeo_lab = ""

            Add_In = True
            if typeo:
                # typeolower = typeo.lower()
                if typeo in typeTable:
                    print_put('a<<lightblue>>>>>> typeo "{}" in typeTable "{}"'.format(typeo, typeTable[typeo]["ar"]))
                    cat_test = cat_test.replace(typeo.lower(), "")
                    typeo_lab = typeTable[typeo]["ar"]
                    if (typeo == "sports events" or typeo == "sorts-events") and year:
                        typeo_lab = "أحداث"
                    arlabel = arlabel + typeo_lab
                    Add_to_main2_tab(typeo, typeo_lab)

                    print_put("a<<lightblue>>>typeo_lab : %s" % typeo_lab)
                    if "s" in typeTable[typeo]:
                        suf = typeTable[typeo]["s"]
                else:
                    print_put('a<<lightblue>>>>>> typeo "%s" not in typeTable' % typeo)

            cnt_la = ""

            if contry:
                cnt_la = ""

                if not cnt_la:
                    cnt_la = pop_All_2018.get(contry, "")

                if not cnt_la:
                    cnt_la = Get_contry(contry_not_lower)

                if cnt_la == "" and category3 == year + " " + contry:
                    cnt_la = Nat_mens.get(contry, "")
                    if cnt_la:
                        cnt_la = cnt_la + " في"
                        print_put("a<<lightblue>>>2021 cnt_la == %s" % cnt_la)

                if cnt_la:
                    Add_to_main2_tab(contry, cnt_la)
                    cat_test = cat_test.lower()
                    cat_test = cat_test.replace(contry.lower(), "")
                    print_put("a<<lightblue>>>cnt_la : %s" % cnt_la)

            # ar_label_b = arlabel.strip()

            if year:
                year_labe = year_lab.make_year_lab(year)
                if year_labe:
                    Add_to_main2_tab(year, year_labe)
                    cat_test = cat_test.lower().replace(year.lower(), "")

                    arlabel = arlabel + " " + year_labe
                    print_put(f'year != "" arlabel:"{arlabel}",In.strip() == "{In.strip()}"')

                    if (In.strip() == "in" or In.strip() == "at") and suf.strip() == "":
                        print_put('Add في to arlabel:in,at"%s"' % arlabel)
                        arlabel = arlabel + " في "
                        cat_test = cat_test.replace(In, "")
                        Add_In = False
                        Add_In_Done = True

            if not (contry != "" and cnt_la == "") and not (year != "" and year_labe == ""):
                if not (typeo != "" and typeo_lab == ""):
                    if In.strip():
                        if In.strip() in Tit_ose_Nmaes and arlabel.find(Tit_ose_Nmaes[In.strip()].strip()) != -1:
                            cat_test = cat_test.replace(In.strip(), "")
                        else:
                            print_put('<<lightred>>>>>> In in Tit_ose_Nmaes, and arlabel wothout "%s" ' % Tit_ose_Nmaes[In.strip()])
                    else:
                        cat_test = cat_test.replace(In.strip(), "")

            cat_test = re.sub(r"category:", "", cat_test)
            output_test('<<lightblue>>>>>> cat_test, : "%s" ' % cat_test)
            cat_test3 = cat_test

            if (year == "" or year_labe == "") and cat_test.strip():
                NoLab = True
                print_put("year == " ' or year_labe == ""')
            elif contry == '" and In == "':
                print_put('a<<lightblue>>>>>> contry == "" and In ==  "" ')
                arlabel = re.sub(r" ", " ", arlabel)
                if suf:
                    arlabel = arlabel + " " + suf
                arlabel = re.sub(r"\s+", " ", arlabel)
                output_test("a<<lightblue>>>>>> No contry.")

            elif contry:
                if cnt_la:
                    Add_to_main2_tab(contry, cnt_la)
                    cat_test = cat_test.replace(contry, "")
                    arlabel = re.sub(r" ", " ", arlabel)
                    con_lab = cnt_la
                    Contry_In_Table = False
                    for table in Table_for_frist_word.keys():
                        if contry in Table_for_frist_word[table]:
                            Contry_In_Table = True
                            output_test(f'>> >> dX:<<lightpurple>> Contry_In_Table "{contry}" in {table}.')

                    if contry in contry_before_year:
                        Contry_In_Table = True
                        output_test('>> >> X:<<lightpurple>> Contry_In_Table "%s" in contry_before_year.' % contry)

                    if suf:
                        suf = " %s " % suf.strip()
                    else:
                        suf = " "

                    arlabel2 = arlabel

                    if Contry_In_Table and typeo not in Keep_it_frist:
                        if (In.strip() == "in" or In.strip() == "at") or (contry.lower() in New_players) and not con_lab.startswith("حسب"):
                            if year_labe:
                                con_lab = con_lab + " في "
                                Add_In_Done = True
                                output_test(">>> Add في line: 1010")
                                cat_test = cat_test.replace(In, "")

                        arlabel = con_lab + suf + arlabel
                        if arlabel.startswith("حسب"):
                            arlabel = arlabel2 + suf + con_lab
                        Add_to_main2_tab(In.strip(), "في")
                    else:
                        if In.strip() == "in" or In.strip() == "at":
                            con_lab = "في " + con_lab

                            cat_test = cat_test.replace(In, "")
                            Add_to_main2_tab(In.strip(), "في")
                            Add_In_Done = True

                        arlabel = arlabel + suf + con_lab
                        # ---
                        arlabel = re.sub(r"\s+", " ", arlabel)
                        # ---
                        arlabel = arlabel.replace(" في في ", " في ")
                        # ---
                        print_put(">3252 arlabel: " + arlabel)

                    if (typeo == '" and In == "') and (contry and year != ""):
                        print_put("a<<lightblue>>>>>> Add year before")
                        if (suf.strip() == "" and con_lab.startswith("ال")) or contry in Add_in_table or (contry and year and In == "" and typeo == "" and contry in add_in_to_contry) or contry in Films_O_TT:
                            suf = " في "
                            print_put("a<<lightblue>>>>>> Add في to suf")
                        print_put(f'a<<lightblue>>>>>> con_lab:{con_lab},suf:{suf}:,arlabel2:"{arlabel2}"')

                        if In.strip() == "" and Add_In and not Add_In_Done and year_labe.strip() == arlabel2.strip() and suf.strip() == "" and con_lab.strip() in ar_lab_before_year_to_add_in:
                            print_put("ar_lab_before_year_to_add_in Add في to arlabel")
                            suf = " في "
                            Add_In = False
                            Add_In_Done = True

                        arlabel = con_lab + suf + arlabel2
                        print_put("a<<lightblue>>>3265>>>arlabel = con_lab + suf +  arlabel2")
                        print_put("a<<lightblue>>>3265>>>" + arlabel)
                    print_put(f'a<<lightblue>>>>>> p:{cnt_la},year_labe: {year_labe}:, cat:"{category}"')
                    print_put('a<<lightblue>>>>>> arlabel  "%s"' % arlabel)
                else:
                    print_put('a<<lightblue>>>>>> Cant id contry : "%s" ' % contry)
                    # Cant_Find_Contry = True
            else:
                print_put("a<<lightblue>>>>>> No label.")
                NoLab = True

            if NoLab and cat_test == "":
                if cnt_la and typeo_lab and year == "" and In == "":
                    if typeo in type_after_contry:
                        ar = f"{cnt_la} {typeo_lab}"
                    elif (typeo in typeTable) or (typeo in Films_O_TT) or (typeo.lower() in New_players):
                        ar = f"{typeo_lab} {cnt_la}"
                    else:
                        ar = f"{cnt_la} {typeo_lab}"
                    New_Lan[category_r] = ar
                    print_put(f'>>>> <<lightyellow>> typeo_lab:"{typeo_lab}", cnt_la "{cnt_la}"')
                    print_put(f'>>>> <<lightyellow>> New_Lan[{category_r}] = "{ar}" ')

            if cat_test != cat_test3:
                output_test('<<lightgreen>>>>>> cat_test : "%s" ' % cat_test)
                output_test("<<lightgreen>>>>>> arlabel " + arlabel)
            if not cat_test.strip():
                output_test("<<lightgreen>>>>>> arlabel " + arlabel)
            elif cat_test == contry.lower() or (cat_test == "in " + contry.lower()):
                output_test("<<lightgreen>>>>>> cat_test False.. ")
                output_test('<<lightblue>>>>>> cat_test = contry : "%s" ' % contry)
                NoLab = True
            elif cat_test.lower() == category2.lower():
                output_test("<<lightblue>>>>>> cat_test = category2 ")
            else:
                output_test("<<lightgreen>>>> >> cat_test False.. ")
                output_test(' cat_test : "%s" ' % cat_test)
                output_test("<<lightgreen>>>>>> arlabel " + arlabel)
                NoLab_list[category_r] = ""
                NoLab = True

            # arlabel = arlabel

            if NoLab and year and year_labe:
                formatt = category.lower()
                formatt = re.sub(r"category:", "", formatt)
                formatt = re.sub(r"_", " ", formatt)
                formatt = re.sub(year, "###", formatt)

                if formatt in NewFormat:
                    print_put('<<lightgreen>>>>>> formatt:"%s" in NewFormat. ' % formatt)
                    NoLab = False
                    arlabel = re.sub(r"###", year_labe, NewFormat[formatt])
                    print_put('<<lightgreen>>>>>> New formatt lab :"%s" ' % arlabel)

            if NoLab and year and year_labe:
                cat4_lab = work_2019(category3, year, year_labe)
                if cat4_lab:
                    New_Lan[category_r] = cat4_lab

            if not NoLab:
                if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) == arlabel:
                    arlabel = fixtitle.fixlab(arlabel, en=category_r)
                    print_put("a<<lightred>>>>>> arlabel ppoi:%s" % arlabel)
                    print_put(f'>>>> <<lightyellow>> cat:"{category_r}", category_lab "{arlabel}"')
                    print_put("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
                    event2_cash[cash_key] = arlabel
                    return arlabel
    if not ar_label:
        sub_ar_label = ""
        list_of_cat = ""

        category = category_r
        category = category.replace("−century", " century")
        category = category.replace("–century", " century")
        if not category.lower().startswith("category:"):
            category = "Category:" + category

        if category.endswith(" stubs") and Find_stubs[1]:
            list_of_cat = "بذرة {}"
            category = category.replace(" stubs", "", 1)

            sub_ar_label = event_Lab_seoo("", category)

            if not sub_ar_label:
                sub_ar_label = tmp_bot.Work_Templates(category)

            if sub_ar_label and list_of_cat:
                ar_label = list_of_cat.format(sub_ar_label)
                printe.output(f'<<lightblue>> event2 add list_of_cat, ar_label:"{ar_label}", category:{category} ')
    print_put("<<lightblue>>>> ^^^^^^^^^ event2 end 3 ^^^^^^^^^ ")
    event2_cash[cash_key] = ar_label
    return ar_label
