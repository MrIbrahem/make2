"""

Usage:

"""
from typing import Dict
from .. import printe
from .bot_2018 import pop_All_2018
from ..helps.print_bot import output_test
from .bot import Films_O_TT, New_players
from .centries_bot import centries_years_dec

from ..ma_lists_bots import pf_keys2
from ..ma_lists_bots import Music_By_table
from ..ma_lists_bots import Films_key_man
from .bot import All_P17
from ..ma_lists_bots import By_table

fasop: Dict[str, str] = {}
table1get_tab: Dict[str, str] = {}

KAKO: Dict[str, Dict[str, str]] = {
    "pf_keys2": pf_keys2,
    "pop_All_2018": pop_All_2018,
    "Music_By_table": Music_By_table,
    "Films_key_man": Films_key_man,
    "All_P17": All_P17,
    "By_table": By_table,
    "Films_O_TT": Films_O_TT,
    "New_players": dict(New_players),
}


def get_KAKO(cont: str) -> str:
    cnt_la = ""
    for KO, KOTab in KAKO.items():
        if not cnt_la:
            cnt_la = KOTab.get(cont, "")
            if cnt_la:
                output_test(f'>> get_KAKO_({KO}) for ["{cont}"] = "{cnt_la}"')
                return cnt_la
    return cnt_la
