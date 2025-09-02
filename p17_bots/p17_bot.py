import re
import functools
from typing import Optional, Tuple, List
from ..jobs_bots.get_helps import get_con_3
from ..matables_bots.bot import All_P17, Add_to_main2_tab
from ..format_bots import Tit_ose_Nmaes, pop_format
from ..ma_lists_bots import (
    sport_formts_en_ar_is_p17,
    en_is_P17_ar_is_mens,
    en_is_P17_ar_is_P17,
    en_is_P17_ar_is_al_women,
    All_contry_with_nat_keys_is_en,
    contries_from_nat,
)
from .. import ma_lists_sport_lab as sport_lab


def print_put(s: str) -> None:
    # printe.output(s)
    pass


def add_all(lab: str) -> str:
    """
    Adds 'ال' to the beginning of a string, and to the beginning of each word in the string.
    """
    lab_no_al = re.sub(r" ", " ال", lab)
    new_lab = f"ال{lab_no_al}"
    return new_lab


@functools.lru_cache(maxsize=None)
def handle_men_nationality(cate: str) -> str:
    """
    Handles translation for categories with men's nationalities.
    """
    for nana, gak in en_is_P17_ar_is_mens.items():
        nana2 = f" {nana.strip().lower()}"
        if cate.lower().endswith(nana2):
            gagaga = cate[: -len(nana2)].strip()
            mens = All_contry_with_nat_keys_is_en.get(gagaga, {}).get("mens", "")
            if mens:
                return gak.format(mens)
    return ""


@functools.lru_cache(maxsize=None)
def handle_women_nationality(cate: str) -> str:
    """
    Handles translation for categories with women's nationalities.
    """
    for nana, gak in en_is_P17_ar_is_al_women.items():
        nana2 = f" {nana.strip().lower()}"
        if cate.lower().endswith(nana2):
            gagaga = cate[: -len(nana2)].strip()
            women = All_contry_with_nat_keys_is_en.get(gagaga, {}).get("women", "")
            if women:
                women = add_all(women)
                return gak.format(women)
    return ""


@functools.lru_cache(maxsize=None)
def Get_P17_2(cate: str) -> str:
    """
    Translates categories where the English name is a country and the Arabic is a nationality.
    e.g. "United States government officials"
    """
    translation = handle_men_nationality(cate)
    if not translation:
        translation = handle_women_nationality(cate)
    return translation


@functools.lru_cache(maxsize=None)
def find_label_for_category_part(con_3: str) -> Tuple[str, Optional[List[Tuple[str, str]]]]:
    """
    Finds a label for a part of a category from various sources.
    Returns the label and the data to be added to the tables.
    """
    # List of functions to get the label from different sources
    label_sources = [
        lambda x: "{} " + Tit_ose_Nmaes[x]
        if x in Tit_ose_Nmaes and Tit_ose_Nmaes[x].startswith("لل")
        else "",
        lambda x: sport_formts_en_ar_is_p17.get(x.strip(), ""),
        lambda x: en_is_P17_ar_is_P17.get(x.strip(), ""),
        lambda x: sport_lab.Get_Sport_Format_xo_en_ar_is_P17(x.strip()),
        lambda x: pop_format.get(x, ""),
    ]
    for source in label_sources:
        label = source(con_3)
        if label:
            return label, [(con_3, label)]
    return "", None


@functools.lru_cache(maxsize=None)
def Get_P17(cate: str) -> str:
    """
    Translates categories where the English name is a nationality and the Arabic is a country name.
    """
    cate_lower = cate.lower()
    con_3, contry_start = get_con_3(cate_lower, All_P17, "All_P17")
    contry_start_lab = All_P17.get(contry_start, "")

    if not con_3 and not contry_start:
        con_3, contry_start = get_con_3(cate_lower, contries_from_nat, "contries_from_nat")
        contry_start_lab = contries_from_nat.get(contry_start, "")

    if con_3 and contry_start:
        con_3_lab, new_data = find_label_for_category_part(con_3)
        if con_3_lab:
            if new_data:
                for key, value in new_data:
                    Add_to_main2_tab(key, value)
            Add_to_main2_tab(contry_start, contry_start_lab)

            if "{nat}" in con_3_lab:
                return con_3_lab.format(nat=contry_start_lab)
            else:
                return con_3_lab.format(contry_start_lab)

    return ""
