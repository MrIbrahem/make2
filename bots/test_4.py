#!/usr/bin/python3
r"""
# ---
^(\s+),(".*?"\s*)$
$1$2,
# ---
,("[^\[\]]+"\s*)(\s*#[^\[\]]+|)$
,\s*("[^\[\]]+"\s*)(\s*#[^\[\]]+|)$

$1,$2

# ---
^(\s+#*\s*),(\s*".*?")(\s*#.*?|)$
$1$2,$3

# ---
(['"])\s+?$
$1
# ---
"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import sys

# ---
from ma_lists.Nationality import (
    All_Nat,
    Nat_women,
    Nat_men,
    Nat_mens,
    Nat_Womens,
    All_contry_with_nat_ar,
)
from ma_lists.all_keys3 import NN_table
from ma_lists.Jobs import (
    Jobs_key_mens,
    Jobs_key_womens,
    womens_Jobs_2017,
    Female_Jobs,
    Nat_Before_Occ,
    Men_Womens_with_nato,
)
from ma_lists.films_mslslat import (
    Films_key_CAO,
    Films_key_For_nat,
    Films_key_CAO_new_format,
    television_keys_female,
    Films_key_333,
)
from ma_lists.peoples import People_key
from ma_lists.languages import (
    languages_key,
    lang_key_m,
)
from ma_lists.by_type import By_table
from ma_lists.male_keys import New_female_keys, New_male_keys
from make2.matables_bots.bot_2018 import pop_All_2018
from ma_lists.test_4_list import replace_labels_2022, New_2018_For_kkk, New_2018_men_Keys_with_all, New_2018_men_Keys_without_all, New_2018_for_women_Keys_with_all, New_2018_for_women_without_al_Keys, change_male_to_female, Mens_suffix, priffix_lab_for_2018, Mens_priffix, Women_s_priffix, Main_priffix, Main_priffix_to, Multi_sport_for_Jobs
from ma_lists.jobs_defs import religious_keys_PP

# ---
from . import test_5
from make2.helps.print_bot import output_test4

get_Films_key_CAO_cash = {}
Films_cash = {}
try_relegins_jobs_cash = {}
get_con_cash = {}
Lang_work_cash = {}
priffix_Mens_work_cash = {}
priffix_woMens_work_cash = {}
Jobs_cash = {}
Jobs_in_Multi_Sports_cash = {}
test4_2018_Jobs_cash = {}
wo_2018_cash = {}
Work_for_me_cash = {}
test4_2018_with_nat_cash = {}


def get_con_3(cate, keys, Type):
    # ---
    T_uple = cate, Type
    # ---
    if T_uple in get_con_cash:
        return get_con_cash[T_uple]
    # ---
    fo_3 = ""
    contry_start = ""
    # ---
    for key in keys:
        tables = {}
        if not fo_3:
            # ---
            tables[2] = f"{key.lower()} "
            # ---
            # tables[1] = key.lower().strip() + " people "
            if Type == "nat":
                tables[1] = f"{key.lower().strip()} people "
            # ---
            if key.startswith("the "):
                tables[3] = key[len("the ") :]  #
                # output_test4('<<lightblue>>>>>> get_con_3 startswith "the ", key3:"%s" changed to %s' % ( key , tables[3]) )
            # ---
            # sorted_list = [ x for x in tables ]
            # sorted_list.sort()
            # ---
            for key_d in [1, 2, 3, 4]:
                if fo_3 == "" and tables.get(key_d):
                    if cate.lower().startswith(tables[key_d].lower()):
                        contry_start = key
                        fo_3 = cate[len(tables[key_d]) :].strip()
                        output_test4(f'<<lightyellow>>>>>> get_con_3 start_th key_:{int(key_d)} ("{tables[key_d]}"), fo_3:"{fo_3}",contry_start:"{contry_start}"')
                        break
    # ---
    get_con_cash[T_uple] = fo_3, contry_start
    # ---
    if fo_3 and contry_start:
        output_test4(f'<<lightpurple>>>>>> test_4.py contry_start:"{contry_start}",get_con_3 fo_3:"{fo_3}",Type:{Type}')
    # ---
    return fo_3, contry_start


def Jobs2(cate, Start, con_3):
    # ---
    contry = Start
    contry_lab = ""
    # ---
    con_3_lab = Jobs_key_mens.get(con_3, "")
    if con_3_lab:
        if Nat_mens.get(contry, "") != "":
            # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
            contry_lab = f"{con_3_lab} {Nat_mens.get(contry, '')}"
            output_test4(f'<<lightblue>> test Jobs: new contry_lab  "{contry_lab}" ')
    # ---
    return contry_lab


def Lang_work(con_3):
    output_test4(f'<<lightblue>> Lang_work :"{con_3}"')
    lang_lab = ""
    # ---
    cash_key = con_3.lower().strip()
    # ---
    if cash_key in Lang_work_cash:
        return Lang_work_cash[cash_key]
    # ---
    if not lang_lab:
        lang_lab = languages_key.get(con_3, "")
    # ---
    tta = {"romanization of": "رومنة {}"}
    # ---
    for wriff, Wriff_lab in tta.items():
        if con_3.startswith(wriff) and lang_lab == "":
            con_43 = con_3[len(wriff) :].strip()
            lang_lac = languages_key.get(f"{con_43} language", "")
            print(con_43)
            if lang_lac:
                lang_lab = Wriff_lab.format(lang_lac)
                break
    # ---
    for lang, l_lab in languages_key.items():
        # ---
        if lang_lab:
            break
        # ---
        lang2 = f"{lang} "
        # ---
        lang3 = f"{lang.replace('-language', '')} films"
        if lang3 == con_3:
            lang_lab = f"أفلام ب{l_lab}"
            break
        # ---
        if con_3.startswith(lang2):
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            output_test4(f"<<lightblue>> con_3.startswith(lang:{lang2})")
            # ---
            if All_Nat.get(lang, False):
                nat_labe = All_Nat[lang]["mens"]
                output_test4(f'<<lightred>> skip lang:"{lang}" in All_Nat,l_lab:"{l_lab}",nat_labe:"{nat_labe}" ')
            else:
                con_8 = con_3[len(lang2) :]
                con_78_lab = Jobs_key_mens.get(con_8, "")
                if con_78_lab:
                    lang_lab = f"{con_78_lab} ب{languages_key[lang]}"  # languages_key[lang].format(con_78_lab)
                    output_test4(f'<<lightblue>> con_3.startswith_priff2("{lang2}"), lang_lab:"{lang_lab}"')
                # ---
                else:
                    con_78_lab = lang_key_m.get(con_8, "")
                    # ---
                    if con_78_lab:
                        output_test4(f'<<lightblue>> con_3.startswith_lang("{lang}"), con_78_lab:"{con_78_lab}"')
                        lang_lab = lang_key_m[con_8].format(languages_key[lang])
    # ---
    Lang_work_cash[cash_key] = lang_lab
    # ---
    return lang_lab


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


def Jobs(cate, Start, con_3, Type="", tab=None):
    # ---
    if not tab:
        tab = {}
    # ---
    cash_key = f"{cate}, {Start}, {Type}, {con_3}".lower().strip()
    # ---
    if cash_key in Jobs_cash:
        return Jobs_cash[cash_key]
    # ---
    output_test4(f'<<lightblue>> test_4.py Jobs: cate: "{cate}", Start: "{Start}", con_3: "{con_3}" ')
    contry = Start
    contry_lab = ""
    # ---
    con_3_lab = Jobs_key_mens.get(con_3, "")
    # ---
    con_4 = con_3
    if con_3.startswith("people "):
        con_4 = con_3[len("people ") :]
    # ---
    pkjn = [" مغتربون", " مغتربات"]
    # ---
    # mens Jobs
    mens_nat_lab = tab.get("mens") or Nat_mens.get(contry, "")
    # ---
    if mens_nat_lab:
        # ---
        if con_3.strip() == "people":
            contry_lab = mens_nat_lab
        # ---
        if not contry_lab:
            con_3_lab = priffix_Mens_work(con_3)
        # ---
        if con_3_lab:
            # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
            # ---
            contry_lab = f"{con_3_lab} {mens_nat_lab}"
            if con_3_lab.startswith("حسب"):
                contry_lab = f"{mens_nat_lab} {con_3_lab}"

            # ---
            if con_3.strip() in Nat_Before_Occ or con_4.strip() in Nat_Before_Occ:
                contry_lab = f"{mens_nat_lab} {con_3_lab}"
            # ---
            # if con_3_lab.find("{nato}")  != -1 :
            # contry_lab = con_3_lab.format(nato = Nat_Womens.get(contry,"") )
            # output_test4('<<lightblue>> con_3_lab: has {nato} "%s"' %  con_3_lab)
            # ---
            TAJO = Men_Womens_with_nato.get(con_3, False)
            if TAJO and TAJO["mens"].find("{nato}") != -1:
                contry_lab = TAJO["mens"].format(nato=mens_nat_lab)
                output_test4('<<lightblue>> TAJO["mens"]: has {nato} "%s"' % TAJO["mens"])
            # ---
            for kjn in pkjn:
                if con_3_lab.endswith(kjn):
                    contry_lab = f"{con_3_lab[:-len(kjn)]} {mens_nat_lab}{kjn}"
                    break
            # ---
            output_test4(f'\t<<lightblue>> con_3: "{con_3}" ')
            output_test4(f'\t<<lightblue>> test mens Jobs: new lab: "{contry_lab}" ')
    # ---#
    # Womens Jobs
    # ---
    if not contry_lab:
        women_nat_lab = tab.get("womens") or Nat_Womens.get(contry, "")
        if women_nat_lab:
            # ---
            if con_3.strip() in ["women", "female", "women's"]:
                contry_lab = women_nat_lab
            # ---
            if not contry_lab:
                f_lab = Jobs_key_womens.get(con_3, "")
                # ---
                if not f_lab:
                    f_lab = Women_s_priffix_work(con_3)
                # ---
                if f_lab:
                    # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
                    contry_lab = f"{f_lab} {women_nat_lab}"
                    # ---
                    if f_lab.find("{nato}") != -1:
                        contry_lab = f_lab.format(nato=women_nat_lab)
                        output_test4('<<lightblue>> TAJO["womens"]: has {nato} "%s"' % f_lab)
                # ---
                for kjn in pkjn:
                    if f_lab.endswith(kjn):
                        contry_lab = f"{f_lab[:-len(kjn)]} {women_nat_lab}{kjn}"
                        break
        # ---
        output_test4(f'\t<<lightblue>> test Womens Jobs: new lab: "{contry_lab}" ')
    # ---
    Jobs_cash[cash_key] = contry_lab
    # ---
    return contry_lab


def get_Films_key_CAO(con_3):
    # ---
    if con_3 in get_Films_key_CAO_cash:
        return get_Films_key_CAO_cash[con_3]
    # ---
    output_test4(f'<<lightblue>> get_Films_key_CAO : con_3 "{con_3}" ')
    con_33 = con_3.lower().strip()
    cas_lab = ""
    labr = ""
    for tyty, cas_lab in television_keys_female.items():
        # ---
        if con_33.endswith(tyty.lower()):
            cc = con_33[: -len(tyty)].strip()
            output_test4(f'<<lightblue>> cc:"{cc}", endswith:"{tyty}" ')
            # ---
            con_3_lab = Films_key_333.get(cc.strip(), "")
            # ---
            if con_3_lab:
                output_test4(f'<<lightblue>> get_Films_key_CAO : cc "{cc}" ')
                if con_3_lab.find("{}") != -1:
                    labr = con_3_lab.format(tyty=cas_lab)
                else:
                    labr = f"{cas_lab} {con_3_lab}"
                output_test4(f'<<lightblue>> get_Films_key_CAO: new labr "{labr}" ')
    # ---
    get_Films_key_CAO_cash[con_3] = labr
    # ---
    return labr


def Films(cate, Start, con_3, fa=""):
    # ---
    cash_key = f"{cate}, {Start}, {con_3}".lower().strip()
    # ---
    if cash_key in Films_cash:
        return Films_cash[cash_key]
    # ---
    # for contry in Nat_women:
    # ---
    # output_test4('<<lightblue>> Films : cate "%s" ' % cate)
    # ---
    # wd = {"contry":"", "k":""}
    contry = Start
    # wd["contry"] = contry
    contry_lab = ""
    # ---
    if con_3:
        llab = Nat_mens[contry] if con_3 == "people" else Nat_women[contry]
        con_3_lab = New_2018_for_women_without_al_Keys.get(con_3.strip(), "")
        if con_3_lab:
            contry_lab = con_3_lab.format(llab)
            output_test4(f'<<lightblue>> test_4:Films: new contry_lab  "{contry_lab}" ')
        # ---#Films_key_CAO
        if not contry_lab:
            con_3_lab = Films_key_CAO.get(con_3, get_Films_key_CAO(con_3))
            if con_3_lab:
                # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
                contry_lab = f"{con_3_lab} {llab}"
                # ---
                if con_3 in Films_key_CAO_new_format:
                    contry_lab = Films_key_CAO_new_format[con_3].format(llab)
                # ---
                output_test4(f'<<lightblue>> test_4:Films: new contry_lab "{contry_lab}" , con_3:{con_3} ')
        # ---#Films_key_For_nat
        if not contry_lab:
            con_3_lab = Films_key_For_nat.get(con_3, "")
            if con_3_lab:
                # output_test4('<<lightblue>> cate.startswith("%s"), con_3:"%s"' % (cate , con_3))
                contry_lab = con_3_lab.format(llab)
                output_test4(f'<<lightblue>> Films_key_For_nat:Films: new contry_lab  "{contry_lab}" ')
                # wd["k"] = con_3
    # else:
    # output_test4( '<<lightred>> con_3 == "" ')
    # ---#get_Films_key_CAO
    if not contry_lab:
        cate_lab = Films_key_CAO.get(cate, "")
        if cate_lab:
            contry_lab = cate_lab
            output_test4(f'<<lightblue>> test Films: contry_lab "{contry_lab}" ')
    # ---
    if not contry_lab:
        contry_lab = get_Films_key_CAO(cate)
        if contry_lab:
            output_test4(f'<<lightblue>> test Films: new contry_lab "{contry_lab}" ')
    # ---
    # wd["lab"] = contry_lab
    # ---
    Films_cash[cash_key] = contry_lab
    # ---
    return contry_lab


def Ethnic(cate, Start, con_3):
    return test_5.Ethnic(cate, Start, con_3)


def try_relegins_jobs(cate):
    # ---
    cach_key = cate.lower().strip()
    # ---
    if cach_key in try_relegins_jobs_cash:
        return try_relegins_jobs_cash[cach_key]
    # ---
    output_test4(f"\t xx start: <<lightred>>try_relegins_jobs >> <<lightpurple>> cate:{cate}")
    # ---
    contry_lab = ""
    # ---

    # ---
    job_example, nat = get_con_3(cate, religious_keys_PP, "religions")
    # ---
    Tab = religious_keys_PP.get(nat, {})
    # ---
    if job_example:
        contry_lab = Jobs(cate, nat, job_example, Type="rel", tab=Tab)
    # ---
    output_test4(f"\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:{cate}, contry_lab:{contry_lab} ")
    # ---
    try_relegins_jobs_cash[cach_key] = contry_lab
    # ---
    return contry_lab


def test4_2018_Jobs(cate, out=False, tab=None):
    # ---
    if not tab:
        tab = {}
    # ---
    cate = re.sub(r"_", " ", cate)
    # ---
    cach_key = cate.lower().strip()
    # ---
    if cach_key in test4_2018_Jobs_cash:
        return test4_2018_Jobs_cash[cach_key]
    # ---
    output_test4(f"<<lightyellow>>>> test4_2018_Jobs >> cate:({cate}) ")
    # ---

    # ---
    cate2_no_lower = cate.lower()
    cate2 = cate.lower()
    # ---
    Main_Ss = ""
    Main_lab = ""
    # ---
    for me, melab in Main_priffix.items():
        me2 = f"{me} "
        if cate.lower().startswith(me2.lower()):
            Main_Ss = me
            cate = cate2_no_lower[len(me2) :]
            # ---
            Main_lab = melab
            if cate.endswith("women") or cate.endswith("women's"):
                if Main_lab in change_male_to_female:
                    Main_lab = change_male_to_female[Main_lab]
            # ---
            output_test4(f'<<lightblue>> test4_2018_Jobs Main_priffix cate.startswith(me2: "{me2}") cate:"{cate}",Main_lab:"{Main_lab}". ')
    # ---
    cate2_no_lower = cate
    cate = cate.lower()
    # ---
    if cate != cate2:
        output_test4(f'<<lightblue>> test4_2018_Jobs cate:"{cate}",cate2:"{cate2}",Main_Ss:"{Main_Ss}". ')
    contry_lab = "أشخاص" if cate == "people" else ""
    # ---
    if Main_Ss.strip() == "fictional" and cate.strip().startswith("female"):
        Main_lab = "{} خياليات"
        print("{} خياليات")
    # ---
    if not contry_lab:
        contry_lab = People_key.get(cate, "")
    if not contry_lab:
        contry_lab = Jobs_key_womens.get(cate, "")
    if not contry_lab:
        contry_lab = Lang_work(cate)
    if not contry_lab:
        contry_lab = Jobs_key_mens.get(cate, "")
    # ---
    nat = ""
    job_example = ""
    # ---
    if not contry_lab:
        job_example, nat = get_con_3(cate, All_Nat, "nat")
    # ---
    job_example_lab = ""
    # ---
    # priffix_lab_for_2018
    if job_example and (Main_Ss in priffix_lab_for_2018) and contry_lab == "":
        # ---
        # New_2018_for_women_without_al_Keys
        job_example_lab = New_2018_for_women_without_al_Keys.get(job_example.strip(), "")
        if job_example_lab:
            contry_lab = job_example_lab.format(Nat_women[nat])
            output_test4(f'<<lightblue>> test_4, new contry_lab "{contry_lab}" ')
            Main_lab = priffix_lab_for_2018[Main_Ss]["women"]
        # ---
        # New_2018_men_Keys_without_all
        if not contry_lab:
            job_example_lab = New_2018_men_Keys_without_all.get(job_example.strip(), "")
            if job_example_lab:
                contry_lab = job_example_lab.format(Nat_men[nat])
                output_test4(f'<<lightblue>> test_4, new contry_lab "{contry_lab}" ')
                Main_lab = priffix_lab_for_2018[Main_Ss]["men"]
    # ---
    if job_example and contry_lab == "":
        contry_lab = Jobs(cate, nat, job_example, Type="nat")
    # ---
    if not contry_lab:
        contry_lab = Women_s_priffix_work(cate)
    # ---
    if not contry_lab:
        contry_lab = priffix_Mens_work(cate)
    # ---
    # Try with Jobs
    # ---
    if Main_Ss and Main_lab and contry_lab:
        contry_lab = Main_lab.format(contry_lab)
        # ---
        if Main_Ss in Main_priffix_to and job_example_lab:
            job_example_lab = job_example_lab.format("").strip()
            contry_lab = Main_priffix_to[Main_Ss].format(nat=Nat_women[nat], t=job_example_lab)
    # ---
    if not contry_lab:
        contry_lab = try_relegins_jobs(cate)
    # ---
    output_test4(f'end test4_2018_Jobs "{cate}" , contry_lab:"{contry_lab}", cate2:{cate2}')
    # ---
    test4_2018_Jobs_cash[cach_key] = contry_lab
    # ---
    return contry_lab


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
        contry_lab = Ethnic(cate, nat, con_3)
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


def nat_match(cate, out=False, fa="", tab=None):
    # ---
    if not tab:
        tab = {}
    # ---

    # ---
    cate2 = cate.lower().replace("category:", "")
    contry = ""
    mat_m = ""
    # ---
    output_test4(f'<<lightblue>> test_4: nat_match cate2 :: "{cate2}" ')
    # ---
    matchs = {
        r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
        # r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
        # r"^anti\-(\w+) sentiment$": "مشاعر معادية لل%s",
    }
    # ---
    for mat, matl in matchs.items():
        if re.match(mat, cate2):
            contry = re.sub(mat, r"\g<1>", cate2)
            mat_m = matl
    # ---
    """
    cate3 = cate2
    if mat_m == "" and cate3.endswith(" sentiment") :
        cate3 = cate3[:-len(" sentiment")]
        if cate2.startswith("anti-") or cate2.startswith("anti-") :
            cate3 = cate2[5:]
    output_test4('<<lightblue>> test_4: nat_match cate3 :: "%s" ' % cate3)
    """
    # ---
    if contry:
        output_test4(f'<<lightblue>> test_4: nat_match contry :: "{contry}" ')
    # ---
    contry_L = Nat_mens.get(contry, "")
    contry_lab = mat_m % contry_L if mat_m and contry_L else ""
    # ---
    if contry_lab:
        output_test4(f'<<lightblue>> test_4: nat_match contry_lab :: "{contry_lab}" ')
    # ---
    return contry_lab


def test4_2018_with_nat(cate, out=False, fa="", tab=None):
    # ---
    if not tab:
        tab = {}
    # ---
    if cate in test4_2018_with_nat_cash:
        return test4_2018_with_nat_cash[cate]
    # ---

    # ---
    output_test4(f"<<lightyellow>>>> test4_2018_with_nat >> cate:({cate}), fa:{fa}..")
    contry_lab = ""
    # ---
    # output_test4('test4_2018_with_nat "%s"' % cate)
    # ---
    cate = re.sub(r"_", " ", cate.lower())
    cate = re.sub(r"-", " ", cate)
    # ---
    if not contry_lab:
        contry_lab = Jobs_key_womens.get(cate, "")
    # ---
    if not contry_lab:
        contry_lab = Jobs_key_mens.get(cate, "")
    # ---
    con_3, nat = get_con_3(cate, All_Nat, "nat")
    # ---
    if con_3:
        # ---
        if not contry_lab:
            contry_lab = Work_for_me(cate, nat, con_3)
        # ---
        if not contry_lab:
            contry_lab = Films(cate, nat, con_3, fa=fa)
        # ---
        if not contry_lab:
            contry_lab = Ethnic(cate, nat, con_3)
        # ---
        if not contry_lab:
            contry_lab = nat_match(cate, nat, con_3)
        # ---
    # ---
    if not contry_lab:
        contry_lab = priffix_Mens_work(cate)
    # ---
    if not contry_lab:
        contry_lab = Women_s_priffix_work(cate)
    # ---
    if contry_lab == "" and con_3 == "":
        contry_lab = Films(cate, "", "", fa=fa)
    # ---
    if contry_lab:
        if con_3:
            contry2 = ""
            output_test4(f'<<lightblue>> test4_2018_with_nat startswith({contry2}),con_3:"{con_3}"')
        output_test4(f'<<lightblue>> test_4: test4_2018_with_nat :: "{contry_lab}" ')
    # ---
    # Try with Jobs
    # ---
    test4_2018_with_nat_cash[cate] = contry_lab
    # ---
    return contry_lab


def Jobs_in_Multi_Sports(cate, out=False, tab=None):
    # ---
    if not tab:
        tab = {}
    # ---
    if cate in Jobs_in_Multi_Sports_cash:
        return Jobs_in_Multi_Sports_cash[cate]
    # ---

    # ---
    # python3 core8/pwb.py make2/test_4 Asian_Games_wrestlers
    # ---
    output_test4(f"<<lightyellow>>>> Jobs_in_Multi_Sports >> cate:({cate}) ")
    # ---
    Main_lab = ""
    # ---
    cate = re.sub(r"_", " ", cate)
    # ---
    # cate2_no_lower = cate
    cate2 = cate.lower()
    # ---
    job = ""
    job_lab = ""
    game_lab = ""
    for ga, game_lab in Multi_sport_for_Jobs.items():
        # ---
        game = f"{ga} "
        if cate.startswith(game):
            job = cate2[len(game) :]
            output_test4(f'Jobs_in_Multi_Sports cate.startswith(game: "{game}") game_lab:"{game_lab}",job:"{job}". ')
    # ---
    if not job_lab and job:
        job_lab = test4_2018_Jobs(job)
        # job_lab = Jobs_key_womens.get(job , "")
    # ---
    if job and game_lab and job_lab:
        Main_lab = f"{job_lab} في {game_lab}"
        # ---
    # ---
    output_test4(f'end Jobs_in_Multi_Sports "{cate}" , Main_lab:"{Main_lab}"')
    # ---
    Jobs_in_Multi_Sports_cash[cate] = Main_lab
    # ---
    return Main_lab


def main():
    # ase = try_relegins_jobs("hindu apologists")
    # print(f"ase:{ase}")
    # ---
    # python3 core8/pwb.py make2/bots/test_4 Afghan_men's_football_players testprint
    # ---
    if sys.argv and sys.argv[1]:
        La = sys.argv[1].lower()
        La = re.sub(r"_", " ", La)
        La = re.sub(r"Category:", "", La)
        so = test4_2018_Jobs(La, out=True)
        # ss = nat_match(La, out = True)
        # so = test4_2018_Jobs(La, out=True)
        # so = priffix_Mens_work(La)
        print(f"Lab: {La}")
        print(f"so :{so}")
        # print("yemeni :" +  Nat_mens.get("yemeni","")   )
        # print("so :" + so   )


if __name__ == "__main__":
    main()
