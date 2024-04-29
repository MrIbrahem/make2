"""

Usage:
from make2.matables_bots.table1_bot import table1get, get_KAKO

"""

from make2 import printe
from .bot_2018 import pop_All_2018
from make2.helps.print_bot import output_test
from .bot import Add_to_main2_tab  # Add_to_main2_tab()
from .bot import Films_O_TT, New_players
from .centries_bot import centries_years_dec

fasop = {}
table1get_tab = {}
# ---
Fgos2 = {
    "Films_O_TT": Films_O_TT,
    "pop_All_2018": pop_All_2018,
}

Fgos1 = {
    "centries_years_dec": centries_years_dec,
    "pop_All_2018": pop_All_2018,
    "New_players": New_players,
    "Films_O_TT": Films_O_TT,
}

papa = False
if papa == 4:
    for tabd in list(Fgos1):
        for ta in Fgos1[tabd]:
            ta2 = ta.lower()

            if "ف" in Fgos1[tabd][ta] and ta2.find("f") == -1 and ta2.find("ph") == -1:
                fasop[ta2] = Fgos1[tabd][ta]

            if ta2 in table1get_tab and table1get_tab[ta2] != Fgos1[tabd][ta]:
                printe.output(f"<<lightblue>>{tabd}: {ta2}: {table1get_tab[ta2]} != {Fgos1[tabd][ta]}")
            table1get_tab[ta2] = Fgos1[tabd][ta]
            if Fgos1[tabd][ta].find(",") != -1:
                printe.output(Fgos1[tabd][ta])
    printe.output(f'<<lightblue>> len "<<lightpurple>>table1get_tab"<<default>>:\t{len(table1get_tab)}. ')
    # for aaa in fasop.keys():

    printe.output(f"<<lightblue>>len fasop: {len(fasop)}")

Fgo_done = {}

for tabd in list(Fgos1):
    Fgo_done[tabd] = {}
for tabd in list(Fgos2):
    Fgo_done[tabd] = {}

FgosLi = {1: Fgos1, 2: Fgos2}

from ma_lists.all_keys2 import pop_final_all_keys2
from ma_lists.by_type import Music_By_table
from ma_lists.films_mslslat import Films_key_man
from .bot import All_P17
from ma_lists.by_type import By_table

KAKO = {
    "pop_final_all_keys2": pop_final_all_keys2,
    # "pop_new" : pop_new ,
    "pop_All_2018": pop_All_2018,
    "Music_By_table": Music_By_table,
    "Films_key_man": Films_key_man,
    "All_P17": All_P17,
    "By_table": By_table,
    "Films_O_TT": Films_O_TT,
    # "pop_of_in" : pop_of_in ,
    "New_players": New_players,
}


def get_KAKO(cont):
    cnt_la = ""
    for KO in KAKO:
        if not cnt_la:
            cnt_la = KAKO[KO].get(cont, "")
            if cnt_la:
                output_test(f'>> get_KAKO_({KO}) for ["{cont}"] = "{cnt_la}"')
                return cnt_la
    return cnt_la


def table1get(category3, tt):
    Fgos = FgosLi.get(tt, {})

    y_lab = ""
    for table1 in list(Fgos):
        if not y_lab:
            if category3 not in Fgo_done[table1]:
                output_test(f'a<<lightblue>>>>>> table1get find in "{len(Fgos[table1])}" keys in table1 "{table1}"')
                y_lab = Fgos[table1].get(category3, "")

                Fgo_done[table1][category3] = y_lab
                break
            else:
                Capo = Fgo_done[table1][category3]
                output_test(f'a<<lightblue>>>>>> category3:"{category3}" in table1 "{table1}", lab:"{Capo}"')

                if Capo:
                    Add_to_main2_tab(category3, Capo)
                    output_test(f'a<<lightgreen>>>>>> category3:"{category3}" in table1 "{table1}", lab:"{Capo}"')
                    y_lab = Capo
                    break
    return y_lab
