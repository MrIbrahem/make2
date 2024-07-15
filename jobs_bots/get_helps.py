#!/usr/bin/python3
"""

from ..jobs_bots.get_helps import get_con_3

"""

from ..helps.print_bot import output_test4

get_con_cash = {}


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
                        output_test4(f'<<lightyellow>>>>>> get_con_3 start_th key_:{key_d} ("{tables[key_d]}"), fo_3:"{fo_3}",contry_start:"{contry_start}"')
                        break
    # ---
    get_con_cash[T_uple] = fo_3, contry_start
    # ---
    if fo_3 and contry_start:
        output_test4(f'<<lightpurple>>>>>> test_4.py contry_start:"{contry_start}",get_con_3 fo_3:"{fo_3}",Type:{Type}')
    # ---
    return fo_3, contry_start
