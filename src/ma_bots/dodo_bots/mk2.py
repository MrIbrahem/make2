#!/usr/bin/python3
"""
Usage:
from .mk2 import new_func_mk2
# cat_test, arlabel = new_func_mk2(category, cat_test, year, typeo, In, country, arlabel, year_labe, suf, Add_In, cnt_la, Add_In_Done)

"""

import re
from typing import Dict, List, Set

from ...format_bots import ar_lab_before_year_to_add_in, contry_before_year
from ...matables_bots.bot import (
    Add_to_main2_tab,
    Films_O_TT,
    New_players,
    Table_for_frist_word,
    Add_in_table,
    Keep_it_frist,
    add_in_to_contry,
)
from ...helps.print_bot import print_put, output_test


def check_key_in_tables_return_tuple(key: str, tables: Dict[str, Dict[str, str] | Set[str]]) -> tuple[bool, str]:
    """Return presence flag and table name when ``key`` is found."""
    for name, table in tables.items():
        if key in table or key.lower() in table:
            return True, name
    return False, ""


def add_the_in(in_table, country, arlabel, suf, In, typeo, year_labe, country_label, cat_test):
    """Insert location prepositions into labels when table rules require them."""
    Add_In_Done = False
    arlabel2 = arlabel

    if in_table and typeo not in Keep_it_frist:
        if (In.strip() == "in" or In.strip() == "at") or (country.lower() in New_players) and not country_label.startswith("حسب"):
            if year_labe:
                country_label = f"{country_label} في "
                Add_In_Done = True
                output_test(">>> Add في line: 1010")
                cat_test = cat_test.replace(In, "")

        arlabel = country_label + suf + arlabel
        if arlabel.startswith("حسب"):
            arlabel = arlabel2 + suf + country_label
        Add_to_main2_tab(In.strip(), "في")
    else:
        if In.strip() == "in" or In.strip() == "at":
            country_label = f"في {country_label}"

            cat_test = cat_test.replace(In, "")
            Add_to_main2_tab(In.strip(), "في")
            Add_In_Done = True

        arlabel = arlabel + suf + country_label
        arlabel = re.sub(r"\s+", " ", arlabel)
        arlabel = arlabel.replace(" في في ", " في ")
        print_put(f">3252 arlabel: {arlabel}")

        # if (typeo == '" and In == "') and (country and year != ""):
    return Add_In_Done, arlabel, cat_test


def added_in_new(country: str, arlabel: str, suf: str, year_labe: str, country_label: str, Add_In: bool, arlabel2: str):
    """Handle cases where a year prefix needs a linking preposition."""
    Add_In_Done = False
    to_check_them_tuble = {
        "Add_in_table": Add_in_table,
        "add_in_to_country": add_in_to_contry,
        "Films_O_TT": Films_O_TT,
    }

    co_in_tables, tab_name = check_key_in_tables_return_tuple(country, to_check_them_tuble)
    # co_in_tables = country in Add_in_table or country in add_in_to_country or country in Films_O_TT
    # ANY CHANGES IN FOLOWING LINE MAY BRAKE THE CODE !
    # print(f"co_in_tables: {co_in_tables} tab_name:{tab_name}, country: {country}")

    print_put("a<<lightblue>>>>>> Add year before")
    if (
        suf.strip() == "" and country_label.startswith("ال")
    ) or co_in_tables:
        suf = " في "
        print_put("a<<lightblue>>>>>> Add في to suf")

    print_put(f'a<<lightblue>>>>>> country_label:{country_label},suf:{suf}:,arlabel2:"{arlabel2}"')

    if suf.strip() == "" and year_labe.strip() == arlabel2.strip():
        if Add_In and country_label.strip() in ar_lab_before_year_to_add_in:
            print_put("ar_lab_before_year_to_add_in Add في to arlabel")
            suf = " في "
            Add_In = False
            Add_In_Done = True

        elif country_label.strip().startswith("أعضاء ") and country_label.find(" حسب ") == -1:
            print_put(">354 Add في to arlabel")
            suf = " في "
            Add_In = False
            Add_In_Done = True

    arlabel = country_label + suf + arlabel2

    print_put("a<<lightblue>>>3265>>>arlabel = country_label + suf +  arlabel2")
    print_put(f"a<<lightblue>>>3265>>>{arlabel}")

    return arlabel, Add_In, Add_In_Done


def new_func_mk2(category, cat_test, year, typeo, In, country, arlabel, year_labe, suf, Add_In, cnt_la, Add_In_Done):
    """Process and modify category-related labels based on various conditions.

    This function takes multiple parameters related to categories and
    modifies the `cat_test` and `arlabel` based on the presence of the
    country in predefined tables, the type of input, and other conditions.
    It also handles specific formatting for the labels and manages the
    addition of certain phrases based on the context. The function performs
    checks against lists of countries and predefined rules to determine how
    to construct the final output labels.

    Args:
        category (str): The category to be processed.
        cat_test (str): The test string for the category.
        year (str): The year associated with the category.
        typeo (str): The type of input being processed.
        In (str): A string indicating location (e.g., "in", "at").
        country (str): The country name to be checked.
        arlabel (str): The Arabic label to be modified.
        year_labe (str): The label for the year.
        suf (str): A suffix to be added to the label.
        Add_In (bool): A flag indicating whether to add a specific input.
        cnt_la (str): A counter or label associated with the country.
        Add_In_Done (bool): A flag indicating whether the addition has been completed.

    Returns:
        tuple: A tuple containing the modified `cat_test` and `arlabel`.
    """

    Add_to_main2_tab(country, cnt_la)
    cat_test = cat_test.replace(country, "")

    arlabel = " ".join(arlabel.strip().split())
    arlabel2 = arlabel

    country_label = cnt_la
    suf = f" {suf.strip()} " if suf else " "
    # ---------------------
    # phase 1
    # ---------------------
    in_table = False
    for table in Table_for_frist_word.keys():
        if country in Table_for_frist_word[table]:
            in_table = True
            output_test(f'>> >> dX:<<lightpurple>> in_table "{country}" in {table}.')

    if country in contry_before_year:
        in_table = True
        output_test(f'>> >> X:<<lightpurple>> in_table "{country}" in contry_before_year.')

    Add_In_Done, arlabel, cat_test = add_the_in(in_table, country, arlabel, suf, In, typeo, year_labe, country_label, cat_test)

    print_put(f"{year_labe=}, {arlabel2=}")

    # ---------------------
    # phase 2
    # ---------------------
    # print(xx)
    if not Add_In_Done:
        if typeo == "" and In == "" and country and year:
            arlabel, Add_In, Add_In_Done = added_in_new(country, arlabel, suf, year_labe, country_label, Add_In, arlabel2)

    arlabel = " ".join(arlabel.strip().split())

    print_put(f'a<<lightblue>>>>>> p:{cnt_la}, year_labe: {year_labe}:, cat:"{category}"')
    print_put(f'a<<lightblue>>>>>> arlabel  "{arlabel}"')

    return cat_test, arlabel
