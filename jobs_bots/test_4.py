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

import re
import sys

# ---
from ma_lists.Nationality import (
    All_Nat,
    Nat_women,
    Nat_men,
    Nat_mens,
    All_contry_with_nat_ar,
)
from ma_lists.all_keys3 import NN_table
from ma_lists.Jobs import (
    Jobs_key_mens,
    Jobs_key_womens,
)
from ma_lists.peoples import People_key
from ma_lists.languages import (
    languages_key,
    lang_key_m,
)
from ma_lists.male_keys import New_female_keys, New_male_keys

from ma_lists.test_4_list import New_2018_For_kkk, New_2018_men_Keys_with_all, New_2018_men_Keys_without_all, New_2018_for_women_Keys_with_all, New_2018_for_women_without_al_Keys, change_male_to_female, priffix_lab_for_2018, Main_priffix, Main_priffix_to, Multi_sport_for_Jobs
from ma_lists.jobs_defs import religious_keys_PP
from ..media_bots.film_keys_bot import Films
from ..jobs_bots.get_helps import get_con_3

# ---
from ..o_bots import ethnic_bot
from ..helps.print_bot import output_test4, print_put
from ..jobs_bots.priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..jobs_bots.jobs_mainbot import Jobs  # , Jobs2

try_relegins_jobs_cash = {}
Lang_work_cash = {}
priffix_Mens_work_cash = {}
priffix_woMens_work_cash = {}
Jobs_cash = {}
Jobs_in_Multi_Sports_cash = {}
test4_2018_Jobs_cash = {}
wo_2018_cash = {}
Work_for_me_cash = {}
test4_2018_with_nat_cash = {}


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
            print_put(con_43)
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
        print_put("{} خياليات")
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
            contry_lab = ethnic_bot.Ethnic(cate, nat, con_3)
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
    # print_put(f"ase:{ase}")
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
        print_put(f"Lab: {La}")
        print_put(f"so :{so}")
        # print_put("yemeni :" +  Nat_mens.get("yemeni","")   )
        # print_put("so :" + so   )


if __name__ == "__main__":
    main()
