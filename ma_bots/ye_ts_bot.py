import re
import sys
import functools
from typing import Optional
from ..fix import fixtitle
from ..matables_bots.bot_2018 import pop_All_2018
from ..helps.print_bot import print_def_head
from ..format_bots import Tit_ose_Nmaes
from ..date_bots import year_lab
from ..ma_bots.ar_label_bot import find_ar_label
from ..matables_bots.bot import Films_O_TT, New_players

Find_f_wikidata = {1: "nowikidata" not in sys.argv}


@functools.lru_cache(maxsize=None)
def direct_lookup_handler(category: str) -> Optional[str]:
    """
    Handles direct lookups in various dictionaries.
    """
    return pop_All_2018.get(category) or Films_O_TT.get(category) or New_players.get(category)


@functools.lru_cache(maxsize=None)
def year_lab_handler(category: str) -> str:
    """
    Handles year-based translations.
    """
    return year_lab.make_year_lab(category)


@functools.lru_cache(maxsize=None)
def titose_nmaes_handler(category: str, original_category: str, do_get_contry2: bool) -> Optional[str]:
    """
    Handles translations based on Tit_ose_Nmaes.
    """
    for tito, tito_name in Tit_ose_Nmaes.items():
        if f" {tito} " in category:
            return find_ar_label(
                category, f" {tito} ", tito_name, category, original_category, do_Get_contry2=do_get_contry2
            )
    return None


@functools.lru_cache(maxsize=None)
def translate_general_category(category_r: str, do_Get_contry2: bool = True) -> str:
    """
    Translates a general category by trying a series of strategies.
    """
    category = re.sub(r"_", " ", category_r)
    category = re.sub(r"category:", "", category, flags=re.IGNORECASE)

    print_def_head(f"<<lightyellow>>>> ^^^^^^^^^ translate_general_category start ^^^^^^^^^ ({category}) ")

    handlers = [
        direct_lookup_handler,
        year_lab_handler,
        lambda cat: titose_nmaes_handler(cat, category_r, do_Get_contry2),
    ]

    arlabel = ""
    for handler in handlers:
        lab = handler(category.lower())
        if lab:
            arlabel = lab
            break

    if arlabel:
        arlabel = fixtitle.fixlab(arlabel, en=category_r)

    print_def_head("<<lightyellow>>>> ^^^^^^^^^ translate_general_category end ^^^^^^^^^ ")
    return arlabel


