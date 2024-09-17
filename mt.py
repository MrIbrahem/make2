"""

Usage:
python3 I:/core/bots/ma/make/m.py exit lenth_pri_text
python3 core8/pwb.py make/m exit lenth_pri_text
python3 core8/pwb.py make/m test Category:People executed by the International Military Tribunal in Nuremberg
"""

import time
import sys
import re
from pathlib import Path
from .bot import event

from .helps.print_bot import do_print_options

do_print_options(tst_prnt_all=True)

from .memory import print_memory
import gent
from . import printe

# gc.set_debug(True)
removing = [
    "testprint",
    "noprint",
    "usemains",
    "nowikidata",
    "print_puts",
    "use_main_s",
    "kooora",
    "printhead",
    "nokooora",
    "print_put",
    "yementest",
    "israeli",
    "local",
]


def justlab(opo=""):
    lista = []

    if opo:
        lista.append(opo)

    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        if arg in ["cat", "-cat", "-cat1", "-cat2", "-cat3"]:
            # cate = value
            if value.strip():
                lista.append(value)
            else:
                print(f' value of arg"{arg}" == ""')
        if arg == "-file":
            # cate = value
            value_file = Path(value)
            if not value_file.exists():
                print(f' file "{value_file}" not found')
                continue
            text = value_file.read_text(encoding="utf-8")

            listo = text.split("\n")
            lista = [x.strip() for x in listo if x.strip() != ""]

    if lista:
        tab = event(lista, tst_prnt_all=True)
        # if tab and tab != None:
        for cate in lista:
            cate = re.sub(r"_", " ", cate)
            print(f"tab[{cate}] = \"{tab.get(cate, '')}\"")


def main2(args):
    # python3 core8/pwb.py make/ma_main t:2 -lang:en -family:wikipedia -subcatsr:Category:Establishments_in_India_by_millennium
    # python3 core8/pwb.py make/ma_main t:2 -lang:en -family:wikipedia -subcats:Category:20th-century_actresses
    # python3 core8/pwb.py make/ma_main t:2 -lang:en -family:wikipedia -subcats:Category:20th-century_actresses
    printe.output("<<lightgreen>> main2")
    generator = gent.get_gent(listonly=True, *args)

    for title in generator:
        printe.output(f"title: {title}")
        tab = event([title])
        if tab and tab is not None:
            for cate, xx in tab.items():
                ux = f"tab[{cate}]"
                printe.output(f'{ux.ljust(60)} = "{xx}"')


def mainx():
    # python3 core8/pwb.py make/m t:2
    # python3 core8/pwb.py make/m t:2 -lang:en -family:wikipedia -subcats:Category:Films_by_decade_of_setting
    # python3 core8/pwb.py make/m t:2 -lang:en -family:wikipedia -subcats:Category:Actors_by_medium_by_nationality
    # python3 core8/pwb.py make/m t:5 -cat:Category:Drama_films_by_country
    # python3 core8/pwb.py make/m t:5 -cat:Category:Actors_by_medium_by_nationality
    # python3 core8/pwb.py make/m t:lab -cat:Category:Ambassadors_of_Afghanistan_to_Australia
    # python3 core8/pwb.py make/m t:lab -cat:Category:Military_installations_of_Morocco -cat1:Category:Military_installations_in_Morocco

    starten = time.time()

    if sys.argv and "test" in sys.argv:
        Olist = sys.argv
        Olist.remove(sys.argv[0])
        Olist.remove("test")
        if "-stubs" in Olist:
            Olist.remove("-stubs")
        # Olist.remove("testprint") if "testprint" in Olist

        for arrg in removing:
            if arrg in Olist:
                Olist.remove(arrg)

        Name = " ".join(Olist)
        printe.output(f'Name: "{Name}"')
        justlab(opo=Name)
        # Get_P17(Name)

    for arg in sys.argv:
        arg, _, value = arg.partition(":")

        if arg == "t":
            if value == "2":
                main2(sys.argv)
                break
            elif value == "lab":
                justlab()
                break

    finals = time.time()
    delta = int(finals - starten)

    printe.output(f"<<lightgreen>> def main(): done in {delta} seconds")


if __name__ == "__main__":
    mainx()
    print_memory()
