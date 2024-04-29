"""
from  make2.bots.popl import Work_peoples
"""

from ..matables_bots.bot import Pp_Priffix
from ma_lists.peoples import People_key

# ---
Work_peoples_cash = {}


def print_put(s):
    # ---
    # printe.output(s)
    # ---
    return


def Work_peoples(SUUS):
    # ---
    cash_key = SUUS.lower().strip()
    # ---
    if cash_key in Work_peoples_cash:
        return Work_peoples_cash[cash_key]
    # ---
    print_put(f"<<lightpurple>> >Work_peoples:> len People_key: {len(People_key)} ")
    PpP_lab = ""
    person = ""
    pri = ""
    for pri_ff in Pp_Priffix:
        if not person:
            if SUUS.endswith(pri_ff):
                print_put(f'>>>><<lightblue>> Work_peoples :"{SUUS}"')
                pri = pri_ff
                person = SUUS[: -len(pri_ff)]
                break

    personlab = People_key.get(person, "")
    if not personlab:
        print_put(f'>>>><<lightblue>> cant find personlab for:"{person}"')

    if person and personlab:
        print_put(f'>>>><<lightblue>> person :"{person}", personlab : "{personlab}"')
        PpP_lab = Pp_Priffix[pri].format(personlab)
        print_put(f'>>>><<lightblue>> SUUS.endswith pri("{pri}"), PpP_lab:"{PpP_lab}"')
    # ---
    Work_peoples_cash[cash_key] = PpP_lab
    # ---
    return PpP_lab
