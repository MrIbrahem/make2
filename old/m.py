"""

Usage:
python3 I:/core/bots/ma/make2/m.py exit lenth_pri_text
python3 core8/pwb.py make2/m exit lenth_pri_text
python3 core8/pwb.py make2/m test Category:People executed by the International Military Tribunal in Nuremberg
"""

import time
import sys
import re
from pathlib import Path

Dir = Path(__file__).parent.parent
print(f"Dir: {Dir}")
sys.path.append(str(Dir))

from .. import bot  # event
from ..helps.print_bot import do_print_options
from ..memory import print_memory
from .. import printe

do_print_options(tst_prnt_all=True)

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
        tab = bot.event(lista, tst_prnt_all=True)
        # if tab and tab != None:
        for cate in lista:
            cate = re.sub(r"_", " ", cate)
            print(f"tab[{cate}] = \"{tab.get(cate, '')}\"")


def mainx():
    """Execute the main functionality of the script.

    This function serves as the entry point for the script, processing
    command-line arguments and executing specific tasks based on the
    provided options. It measures the execution time and outputs relevant
    information to the user. The function handles various command-line flags
    and arguments to customize its behavior.  If the script is run with
    "test" in the command-line arguments, it will parse the arguments,
    remove certain flags, and print the resulting name. The function also
    calls `justlab` with the constructed name for further processing.
    """

    # python3 core8/pwb.py make2/m t:2
    # python3 core8/pwb.py make2/m t:2 -lang:en -family:wikipedia -subcats:Category:Films_by_decade_of_setting
    # python3 core8/pwb.py make2/m t:2 -lang:en -family:wikipedia -subcats:Category:Actors_by_medium_by_nationality
    # python3 core8/pwb.py make2/m t:5 -cat:Category:Drama_films_by_country
    # python3 core8/pwb.py make2/m t:5 -cat:Category:Actors_by_medium_by_nationality
    # python3 core8/pwb.py make2/m t:lab -cat:Category:Ambassadors_of_Afghanistan_to_Australia
    # python3 core8/pwb.py make2/m t:lab -cat:Category:Military_installations_of_Morocco -cat1:Category:Military_installations_in_Morocco

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

    finals = time.time()
    delta = int(finals - starten)

    printe.output(f"<<lightgreen>> def main(): done in {delta} seconds")


def main_or():
    if "exit" in sys.argv:
        print_memory()
        sys.exit(0)

    mainx()

    print_memory()


if __name__ == "__main__":
    main_or()
