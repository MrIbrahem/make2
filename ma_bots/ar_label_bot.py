#!/usr/bin/python3
"""
from ..ma_bots.ar_label_bot import find_ar_label

"""


import re
import sys

try:
    from .contry_bot import Get_contry, Get_c_t_lab
except:
    Get_contry = False
    Get_c_t_lab = False
from ..ma_bots.contry2_lab import get_lab_for_contry2
from ..fix import fixtitle
from ..o_bots.popl import make_people_lab
from ..sports_bots import team_work
from ..date_bots import year_lab
from ..bots import tmp_bot
from ..o_bots import bys
from ..p17_bots import nats
from ..jobs_bots.test_4 import test4_2018_Jobs

from ..media_bots.films_bot import test_films
from . import event2bot

from ma_lists.all_keys2 import pop_final_all_keys2, pop_of_without_in
from ma_lists.Labels_Contry import New_P17_Finall
from ma_lists.jobs_defs import religious_keys_PP
from ma_lists.male_keys import New_female_keys

from ..fromnet.wd_bot import find_wikidata
from ..fromnet import kooora
from ..pop_format import Tit_ose_Nmaes, for_table, Tabl_with_in, pop_format33, pop_format, pop_format2, tito_list_s, Dont_Add_min

from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.bot import (
    New_players,
    Table_for_frist_word,
    Add_ar_in,
    Keep_it_last,
    Keep_it_frist,
)

from ..helps.print_bot import print_def_head, print_put, output_test, mainoutput

en_literes = "[abcdefghijklmnopqrstuvwxyz]"

Find_f_wikidata = {1: False if "nowikidata" in sys.argv else True}


def find_ar_label(category, tito, tito_name, Cate_test, category_r, do_Get_contry2=True):
    # Keep_Work = False
    # NoLabb = True
    CAO = True

    print_put(f'<<lightblue>>>>>> yementest: category.find(tito:"{tito_name}":"{tito}") != -1 ')
    tito2 = tito.lower()
    Type, contry = get_type_country(category, tito)

    arlabel = ""
    Type_lower = Type.strip().lower()
    contry_lower = contry.strip().lower()

    Type_lower_in = Type_lower.strip()

    if not Type_lower_in.endswith(" " + tito2):
        Type_lower_in = Type_lower.strip() + " " + tito2

    Type_lab, Add_in_lab = get_Type_lab(tito, Type, Type_lower, contry_lower, Type_lower_in)

    if Type_lab:
        Cate_test = Cate_test.replace(Type_lower, "")

    con_lab = get_con_lab(tito, do_Get_contry2, tito2, contry, contry_lower)

    if con_lab:
        Cate_test = Cate_test.replace(contry_lower, "")

    if not Type_lab:
        print_put('>>>> Type_lower "%s" not in pop_of_in' % Type_lower)
        CAO = False
    else:
        Cate_test = Cate_test.replace(Type_lower, "")

    if not con_lab:
        print_put('>>>> contry_lower not in pop new "%s"' % contry_lower)
        CAO = False
    else:
        Cate_test = Cate_test.replace(contry_lower, "")

    if Type_lab or con_lab:
        print_put(f'<<lightgreen>>>>>> ------------- contry_lower:"{contry_lower}", con_lab:"{con_lab}"')
        print_put(f'<<lightgreen>>>>>> ------------- Type_lower:"{Type_lower}", Type_lab:"{Type_lab}"')

    # Add_In_Done = False
    if not CAO:
        return ""
    # ---
    print_put('<<lightblue>> CAO: cat:"%s":' % category)
    # ---
    if not Type_lab or not con_lab:
        return ""
    # ---
    if tito2 in tito_list_s and Add_in_lab:
        if tito2 == "in" or Type_lower.find(" in") != -1:
            if Type_lower in pop_of_without_in:
                print_put(f'>>-- Skip aAdd في to Type_lab:"{Type_lab}", "{Type_lower}"')

            else:
                if Type_lab.find(" في") == -1 and Type_lower.find(" in") != -1:
                    print_put(f'>>-- aAdd في to Type_lab:in"{Type_lab}", for "{Type_lower}"')
                    Type_lab = Type_lab + " في"
                    # Add_In_Done = True

                elif tito2 == "in" and Type_lower.find(" in") != -1:
                    print_put(f'>>>> aAdd في to Type_lab:in"{Type_lab}", for "{Type_lower}"')
                    Type_lab = Type_lab + " في"
                    # Add_In_Done = True

        elif (tito2 == "at" or Type_lower.find(" at") != -1) and (Type_lab.find(" في") == -1):
            print_put('>>>> Add في to Type_lab:at"%s"' % Type_lab)
            Type_lab = Type_lab + " في"
            # Add_In_Done = True
    # ---
    Type_lower2 = Type_lower
    # ---
    if Add_in_lab:
        ty_in18 = pop_All_2018.get(Type_lower)

        if Type_lower not in Dont_Add_min:
            if Type_lower.endswith(" of") and ty_in18:
                Type_lower2 = Type_lower[: -len(" of")]
                if Type_lab.find(" في") == -1:
                    if (Type_lower in New_players) or (Type_lower2 in New_players):
                        print_put('>>>> nAdd من to Type_lab"%s" line:1853' % Type_lab)
                        Type_lab = Type_lab + " من "

            elif tito2 == "from":
                if not Type_lab.strip().endswith(" من"):
                    print_put('>>>> nAdd من to Type_lab:from"%s" line:1858' % Type_lab)
                    Type_lab = Type_lab + " من "
        else:
            print_put('>>>> Type_lower "%s" in Dont_Add_min ' % Type_lower)

    # ---
    contry_in_Table = False
    Type_in_Table = False

    # ---
    for table, ta_t in Table_for_frist_word.items():
        if contry_lower in ta_t:
            contry_in_Table = True
            print_put(f'>>>> X:<<lightpurple>> contry_lower "{contry_lower}" in {table}.')

        if Type_lower in ta_t:
            Type_in_Table = True
            print_put(f'>>>>xX:<<lightpurple>> Type_lower "{Type_lower}" in {table}.')

    # ---
    sps = " "
    if tito2 == "in":
        sps = " في "

    if contry_in_Table and Add_in_lab:
        if (tito2 == "in" or tito2 == "at") and (con_lab.find(" في") == -1 or Type_lower in Add_ar_in):
            sps = " في "
            print_put("ssps:%s" % sps)
    else:
        if (tito2 == "in" or tito2 == "at") and (Type_lab.find(" في") == -1 or Type_lower in Add_ar_in):
            Type_lab = Type_lab + " في"

    # ---
    if Add_in_lab:
        if tito2 in Tit_ose_Nmaes and tito2 not in tito_list_s:
            tatl = Tit_ose_Nmaes[tito2]
            print_put(">>>>> > (%s): tito2 in Tit_ose_Nmaes and tito2 not in tito_list_s" % tito2)

            if tito2 == "to" and Type_lower.strip().startswith("ambassadors of"):
                tatl = "لدى"

            if con_lab == "لعضوية البرلمان":
                tatl = ""

            if tito2 == "for" and contry_lower.startswith("for "):
                p18lab = pop_All_2018.get(contry_lower)
                if p18lab and p18lab == con_lab:
                    tatl = ""

            if contry_lower in for_table:
                tatl = ""

            sps = f" {tatl} "
            print_put("sps:%s" % sps)
            Cate_test = Cate_test.replace(tito, "")

    if contry_lower in New_players and Type_lower in New_players:
        print_put(">>>> ================ ")
        print_put(">>>>> > X:<<lightred>> Type_lower and contry_lower in New_players.")
        print_put(">>>> ================ ")

    Keep_Type_last = False
    keep_Type_first = False

    t_to = f"{Type_lower} {tito2}"

    if Type_lower in Keep_it_last:
        print_put('>>>>> > X:<<lightred>> Keep_Type_last = True, Type_lower:"%s" in Keep_it_last' % Type_lower)
        Keep_Type_last = True

    elif Type_lower in Keep_it_frist:
        print_put('>>>>> > X:<<lightred>> keep_Type_first = True, Type_lower:"%s" in Keep_it_frist' % Type_lower)
        keep_Type_first = True

    elif t_to in Keep_it_frist:
        print_put('>>>>> > X:<<lightred>> keep_Type_first = True, t_to:"%s" in Keep_it_frist' % t_to)
        keep_Type_first = True

    if Type_in_Table and contry_in_Table:
        print_put(">>> > X:<<lightpurple>> Type_lower and contry_lower in Table_for_frist_word.")
        if not keep_Type_first and contry_lower in New_players:
            arlabel = con_lab + sps + Type_lab
        else:
            arlabel = Type_lab + sps + con_lab
    else:
        if keep_Type_first and contry_in_Table:
            arlabel = con_lab + sps + Type_lab
        else:
            arlabel = Type_lab + sps + con_lab

    if Keep_Type_last:
        print_put('>>>>> > X:<<lightred>> Keep_Type_last = True, Type_lower:"%s" in Keep_it_last' % Type_lower)
        arlabel = con_lab + sps + Type_lab

    elif keep_Type_first:
        print_put('>>>>> > X:<<lightred>> keep_Type_first = True, Type_lower:"%s" in Keep_it_frist' % Type_lower)
        arlabel = Type_lab + sps + con_lab

    if tito2 == "about" or (tito2 not in tito_list_s):
        arlabel = Type_lab + sps + con_lab

    if Type_lower == "years" and tito2 == "in":
        arlabel = Type_lab + sps + con_lab

    output_test('>>>> sps "%s"' % sps)
    output_test('>>>> arlabel "%s"' % arlabel)
    vr = re.sub(contry_lower, "{}", category.lower())
    if vr in pop_format2:
        print_put('<<lightblue>>>>>> vr in pop_format2 "%s":' % pop_format2[vr])
        print_put('<<lightblue>>>>>>> vr: "%s":' % vr)
        arlabel = pop_format2[vr].format(con_lab)
    elif Type_lower in pop_format:
        if not con_lab.startswith("حسب"):
            print_put('>>>> <<lightblue>> Type_lower in pop_format "%s":' % pop_format[Type_lower])
            arlabel = pop_format[Type_lower].format(con_lab)
        else:
            print_put('>>>> <<lightblue>> Type_lower in pop_format "%s" and con_lab.startswith("حسب") ' % pop_format[Type_lower])

    elif tito2 in pop_format33:
        print_put('>>>> <<lightblue>> tito in pop_format33 "%s":' % pop_format33[tito2])
        arlabel = pop_format33[tito2].format(Type_lab, con_lab)

    arlabel = arlabel.replace("  ", " ")
    maren = re.match(r"\d\d\d\d", contry_lower.strip())
    if Type_lower.lower() == "the war of" and maren and arlabel == f"الحرب في {contry_lower}":
        arlabel = f"حرب {contry_lower}"
        print_put('<<lightpurple>> >>>> change arlabel to "%s".' % arlabel)

    if re.sub(en_literes, "", arlabel, flags=re.IGNORECASE) != arlabel:
        return ""
    # ---
    arlabel = fixtitle.fixlab(arlabel, en=category_r)
    print_put('>>>>>> <<lightyellow>>Cate_test: "%s" ' % Cate_test)
    print_put(f'>>>>>> <<lightyellow>>test: cat "{category_r}", arlabel:"{arlabel}"')
    # NoLabb = False

    print_put('>>>> <<lightblue>>Cate_test :"%s"' % Cate_test)
    return arlabel


def get_con_lab(tito, do_Get_contry2, tito2, contry, contry_lower):
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

        cco2_ = get_lab_for_contry2(cco2)

        if not cco2_ and Get_contry:
            cco2_ = Get_contry(cco2)

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
        con_lab = tmp_bot.Work_Templates(contry_lower)

    if not con_lab:
        con_lab = get_lab_for_contry2(contry_lower)

    if not con_lab and Get_c_t_lab:
        con_lab = Get_c_t_lab(contry_lower, tito, do_Get_contry2=do_Get_contry2)

    if not con_lab:
        con_lab = find_wikidata(contry_lower)
    if not con_lab:
        con_lab = kooora.kooora_team(contry_lower, Local=Find_f_wikidata[1])

    print_put(f"?????? get_con_lab: {contry_lower=}, {con_lab=}")

    return con_lab


def get_Type_lab(tito, Type, Type_lower, contry_lower, Type_lower_in):
    tito2 = tito.lower()

    Type_lab = ""
    if Type_lower == "women" and tito2 == "from":
        Type_lab = "نساء"
        print_put('>> >> >> Make Type_lab "%s".' % Type_lab)

    elif Type_lower == "women of":
        Type_lab = "نساء من"
        print_put('>> >> >> Make Type_lab "%s".' % Type_lab)

    Add_in_lab = True
    if not Type_lab:
        Type_lab = Tabl_with_in.get(Type_lower_in, "")
        if Type_lab:
            Add_in_lab = False
            print_put(f'<<<< Type_lower_in "{Type_lower_in}",Type_lab : "{Type_lab}"')

    if not Type_lab:
        Type_lab = New_P17_Finall.get(Type_lower, "")
        if Type_lab:
            output_test(f'<< Type_lower_in "{Type_lower_in}", Type_lab : "{Type_lab}"')

    if Type_lab == "" and Type_lower.startswith("the "):
        Type_lower2 = Type_lower[len("the ") :]

        Type_lab = New_P17_Finall.get(Type_lower2, "")
        if Type_lab:
            output_test(f'<<< Type_lower_in "{Type_lower_in}", Type_lab : "{Type_lab}"')
    if Type_lower == "sport" and contry_lower.startswith("by "):
        Type_lab = "رياضة"

    if Type_lab == "" and Type_lower.strip().endswith(" people"):
        Type_lab = make_people_lab(Type_lower)

    if not Type_lab:
        Type_lab = religious_keys_PP.get(Type_lower, {}).get("mens", "")
    if not Type_lab:
        Type_lab = New_female_keys.get(Type_lower, "")
    if not Type_lab:
        Type_lab = test_films(Type_lower)
    if not Type_lab:
        Type_lab = nats.find_nat_others(Type_lower)
    if not Type_lab:
        Type_lab = team_work.Get_team_work_Club(Type.strip())
    if not Type_lab:
        Type_lab = tmp_bot.Work_Templates(Type_lower)

    if not Type_lab:
        Type_lab = get_lab_for_contry2(Type_lower)

    if not Type_lab and Get_c_t_lab:
        Type_lab = Get_c_t_lab(Type_lower, tito, Type="Type_lab", make_yementest=False)

    if not Type_lab:
        Type_lab = event2bot.event2(Type_lower)
    if not Type_lab:
        Type_lab = test4_2018_Jobs(Type_lower, out=mainoutput[1])

    print_put(f"?????? get_Type_lab: {Type_lower=}, {Type_lab=}")

    return Type_lab, Add_in_lab


def get_type_country(category, tito):
    Type = category.split(tito)[0]
    contry = category.split(tito)[1]
    contry = contry.lower()
    Mash = "^(.*?)(?:%s?)(.*?)$" % tito
    Type_t = re.sub(Mash, r"\g<1>", category.lower())
    contry_t = re.sub(Mash, r"\g<2>", category.lower())

    test_N = category.lower()
    try:
        test_N = re.sub(Type.lower(), "", test_N)
        test_N = re.sub(contry.lower(), "", test_N)

    except Exception:
        print_put("<<lightred>>>>>> except test_N ")
    test_N = test_N.strip()

    tito2 = tito.strip()

    if tito2 == "in" and Type.endswith(" playerss"):
        Type = Type.replace(" playerss", " players")

    titoends = f" {tito2}"
    titostarts = f"{tito2} "

    if tito2 == "of" and not Type.endswith(titoends):
        Type = f"{Type} of"
    elif tito2 == "spies for" and not Type.endswith(" spies"):
        Type = f"{Type} spies"

    elif tito2 == "by" and not contry.startswith(titostarts):
        contry = f"by {contry}"
    elif tito2 == "for" and not contry.startswith(titostarts):
        contry = f"for {contry}"

    print_def_head(f'>xx>>> Type: "{Type.strip()}", contry: "{contry.strip()}", tito: "{tito}" ')

    if test_N and test_N != tito2:
        print_put(f'>>>> test_N != "", Type_t:"{Type_t}", tito:"{tito}", contry_t:"{contry_t}" ')

        if tito2 == "of" and not Type_t.endswith(titoends):
            Type_t = f"{Type_t} of"
        elif tito2 == "by" and not contry_t.startswith(titostarts):
            contry_t = f"by {contry_t}"
        elif tito2 == "for" and not contry_t.startswith(titostarts):
            contry_t = f"for {contry_t}"
        Type = Type_t
        contry = contry_t

        print_put(f'>>>> yementest: Type_t:"{Type_t}", contry_t:"{contry_t}"')
    else:
        print_put('>>>> test_N:"%s" == tito' % test_N)

    return Type, contry
