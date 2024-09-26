#!/usr/bin/python3
"""
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg

python3 core8/pwb.py -m cProfile -s ncalls make2/main.py

"""


import re
import sys
from tqdm import tqdm
from pathlib import Path
from .date_bots import labs_years

# ---
from . import printe
from .co_bots import filter_en
from .ma_bots import event_lab_bot
from .pop_format_bot import change_cat
from .matables_bots.bot import cash_2022, make_tab, main2_tab
from .fix import fixtitle

from .ma_bots import ye_ts_bot
from .helps.print_bot import do_print_options, output_main, print_put, output_test

from .ma_bots import event2bot

Dir_ma = Path(__file__).parent.parent

event_done = {}

start_yementest = {1: True if "yementest" in sys.argv else False}
use_main_s = {1: True if "usemains" in sys.argv or "use_main_s" in sys.argv else False}
Find_f_wikidata = {1: False if "nowikidata" in sys.argv else True}


def event(NewList, noprint="", maketab="", Use_main_s="", printfirst=False, Local=False, printhead=False, all_print_off=False, tst_prnt_all=None, return_no_labs=False):
    """Process a list of categories and generate corresponding labels.

    This function takes a list of categories and processes each category to
    determine its corresponding label. It handles various options for
    printing and tabulation. The function also manages categories that do
    not have associated labels and can return these as needed. If specified,
    it can also utilize a main script for additional functionality.

    Args:
        NewList (list): A list of category names to process.
        noprint (str?): Option to suppress printing. Defaults to "".
        maketab (str?): Option to create a table. Defaults to "".
        Use_main_s (str?): Flag to indicate the use of the main script. Defaults to "".
        printfirst (bool?): If True, prints the first output. Defaults to False.
        Local (bool?): If True, sets local processing options. Defaults to False.
        printhead (bool?): If True, prints the header. Defaults to False.
        all_print_off (bool?): If True, disables all printing. Defaults to False.
        tst_prnt_all (any?): Test print option. Defaults to None.
        return_no_labs (bool?): If True, returns categories without labels. Defaults to False.

    Returns:
        dict: A dictionary mapping categories to their corresponding labels.
        list: A list of categories that do not have associated labels (if
            return_no_labs is True).
    """

    if Local is True:
        Find_f_wikidata[1] = False
    # ---
    do_print_options(noprint=noprint, printfirst=printfirst, printhead=printhead, all_print_off=all_print_off, tst_prnt_all=tst_prnt_all)
    # ---
    if Use_main_s:
        printe.output("<<lightblue>>  Use_main_s ")
        use_main_s[1] = True

    poiu = ""
    if len(NewList) < 10:
        poiu = ",".join(NewList)
    print_put("<<lightred>> vvvvvvvvvvvv event start vvvvvvvvvvvv ")
    print_put(f"<<lightblue>> event work with >  {len(NewList)} cats. {poiu} ")

    num = 0
    lenth = len(NewList)
    # tit = {}
    Labels__p = {}
    Labels = {}
    NoLab_list = []
    # ---
    uxu = NewList if "all_print_off" not in sys.argv else tqdm(NewList)
    # ---
    for category_r in uxu:
        num += 1
        toout = f'<<lightyellow>>> event ===  {num} / {lenth}  category_r:"{category_r}" === '

        if not category_r:
            continue

        category_r = re.sub(r"_", " ", category_r)

        if maketab is True:
            make_tab[1] = True
            main2_tab[1]["title"] = category_r

        if printfirst:
            printe.output(toout)
            with open(f"{str(Dir_ma)}/textfiles/make2-err.txt", "a", encoding="utf-8") as lo:
                lo.write(f"{category_r}\n")
        else:
            print_put(toout)

        category_lab = new_func_lab(category_r)
        # ---
        if not category_lab or category_lab.strip() == "تصنيف:":
            NoLab_list.append(category_r)
        else:
            if not category_lab.startswith("تصنيف:"):
                category_lab = f"تصنيف:{category_lab}"
            Labels[category_r] = category_lab
        # ---
        if make_tab[1]:
            main2_tab[1]["ar"] = category_lab
            Labels__p[category_r] = main2_tab[1]
        # ---
        event_done[category_r] = category_lab
    # ---
    if make_tab[1]:
        return Labels__p
    # ---
    _lenth_ = len(Labels.keys())
    catnumb = 0
    # ---
    if Labels and Labels is not None:
        for cat, cat_lab in Labels.items():
            catnumb += 1
            ux = f'"{cat}"'
            if printfirst:
                print(f'     {ux.ljust(60)} : "{cat_lab}",')
    else:
        printe.output(f"<<lightyellow>>> event: Labels == None len = {_lenth_}")

    for cat in NoLab_list[:]:
        if cat in Labels:
            NoLab_list.remove(str(cat))

    catb = 0
    if NoLab_list:
        printe.output(f"a<<lightred>>> {len(NoLab_list)} cat in NoLab_list ")
        for cat in NoLab_list:
            catb += 1
            printe.output(f'  {catb}:  "{cat}" : "",')
    print_put("<<lightred>>> ^^^^^^^^^ event end ^^^^^^^^^ ")
    # ---
    if return_no_labs:
        return Labels, NoLab_list
    # ---
    return Labels


def new_func_lab(category_r):
    category_lab = ""
    # ---
    cat_year, from_year = labs_years.lab_from_year(category_r)
    if from_year:
        category_lab = from_year
    # ---
    if not category_lab and filter_en.filter_cat(category_r):
        changed_cat = change_cat(category_r)

        if category_r in event_done:
            output_test(f'>>>> category_r: "{category_r}" in event_done, lab:"{event_done[category_r]}"')
            category_lab = event_done[category_r]

        if not category_lab:
            if category_r.lower() in cash_2022:
                category_lab = cash_2022[category_r.lower()]

        if not category_lab:
            if start_yementest[1]:
                # print("yementest_with_Titose_Nmaes 1")
                category_lab = ye_ts_bot.yementest_with_Titose_Nmaes(changed_cat)

        if not category_lab:
            category_lab = event2bot.event2(changed_cat)

        if not category_lab:
            category_lab = event_lab_bot.event_Lab(changed_cat)
    # ---
    if category_lab:
        category_lab = fixtitle.fixlab(category_lab, en=category_r)

    # ---
    if not from_year and cat_year:
        labs_years.lab_from_year_add(category_r, category_lab, cat_year)

    return category_lab
