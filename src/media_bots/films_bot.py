#!/usr/bin/python3
"""

# from ..media_bots.films_bot import test_films


from ..media_bots import films_bot

lab = films_bot.test_films()

films_bot.

"""

import re
from typing import Dict
from ..o_bots.army import test_Army
from ..p17_bots import p17_bot
from ..media_bots.film_keys_bot import get_Films_key_CAO
from ..jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs
from ..jobs_bots.test_4 import test4_2018_with_nat, Jobs_in_Multi_Sports, nat_match
from ..o_bots import fax
from ..matables_bots.bot import Add_to_main2_tab
from ..matables_bots.bot import Films_O_TT, add_key_new_players
from ..helps.print_bot import print_def_head, output_test, mainoutput

test_films_done: Dict[str, str] = {}


def test_films(cate: str, fa: str = "") -> str:
    normalized_category = cate.lower()
    if normalized_category in test_films_done:
        output_test(f'>>>> normalized_category: "{normalized_category}" in test_films_done, lab:"{test_films_done[normalized_category]}"')
        return test_films_done[normalized_category]

    print_def_head(f"<<lightblue>>>> xxxxxxxxxx test_films normalized_category:{normalized_category} xxxxxxxxxxx ")
    resolved_label = ""

    if re.match(r"^\d+$", normalized_category.strip()):
        resolved_label = normalized_category.strip()

    if not resolved_label:
        resolved_label = get_Films_key_CAO(normalized_category)

    if not resolved_label:
        resolved_label = Jobs_in_Multi_Sports(normalized_category, out=mainoutput[1])
        if resolved_label:
            add_key_new_players(normalized_category, resolved_label, "films_bot.py")
            Add_to_main2_tab(normalized_category, resolved_label)
            output_test(f'>>>> Jobs_in_Multi Sports: [{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = test4_2018_with_nat(normalized_category, out=mainoutput[1], fa=fa)
        if resolved_label:
            Add_to_main2_tab(normalized_category, resolved_label)
            Films_O_TT[normalized_category] = resolved_label
            # print(f"films: {normalized_category=}, {resolved_label=}\n"*10)

    if not resolved_label:
        resolved_label = test4_2018_Jobs(normalized_category, out=mainoutput[1])
        if resolved_label:
            add_key_new_players(normalized_category, resolved_label, "films_bot.py2")
            Add_to_main2_tab(normalized_category, resolved_label)
            output_test(f'>>>> test_4 2018 Jobs: [{normalized_category}] ="{resolved_label}"')

    if not resolved_label:
        resolved_label = nat_match(normalized_category)
        if resolved_label:
            Add_to_main2_tab(normalized_category, resolved_label)
            output_test(f'>>>> nat_match: [{normalized_category}] ="{resolved_label}"')
    if not resolved_label:
        resolved_label = p17_bot.Get_P17(normalized_category)

    if not resolved_label:
        resolved_label = p17_bot.Get_P17_2(normalized_category)

    if not resolved_label:
        resolved_label = fax.test_Lang(normalized_category)

    if not resolved_label:
        resolved_label = test_Army(normalized_category)

    if not resolved_label:
        resolved_label = test4_2018_Jobs(normalized_category, out=mainoutput[1])

    test_films_done[normalized_category] = resolved_label
    print_def_head(f"<<lightblue>>>> xxxxxxxxx test_films end xxxxxxxxxxx resolved_label:{resolved_label}")
    return resolved_label
