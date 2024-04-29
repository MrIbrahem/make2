"""
from  make2.bots.part import get_parties_lab

"""

#
# (C) Ibrahem Qasim, 2023
#
#
# ---
from ma_lists.us_counties import party_end_keys
from ma_lists.keys2 import Parties


def print_put(s):
    # ---
    # print(s)
    # ---
    return


def get_parties_lab(party):
    # إيجاد لاحقات الأحزاب
    print_put(f'get_parties_lab party:"{party}"')
    party_lab = ""

    for tat, tatb in party_end_keys.items():
        fafaf = f" {tat}"
        if party.endswith(fafaf) and party_lab == "":
            party_uu = party[: -len(fafaf)]
            print_put(f'party_uu:"{party_uu}", tat:"{tat}" ')
            label = Parties.get(party_uu, "")
            if label:
                party_lab = tatb % label if tatb.find("%s") != -1 else tatb.format(label)
                break

    if party_lab:
        print_put(f'get_parties_lab party:"{party}", party_lab:"{party_lab}"')

    return party_lab
