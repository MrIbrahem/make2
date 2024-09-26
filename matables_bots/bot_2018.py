#!/usr/bin/python3
r"""

Usage:
from ..matables_bots import bot_2018
# bot_2018.pop_All_2018.get()


from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.bot_2018 import get_pop_All_18, Add_to_pop_All_18 # get_pop_All_18(key, "") #Add_to_pop_All_18(tab)


# pop_All_2018\.get\((.*?), (.*?)\)
# get_pop_All_18($1, $2)

or

# pop_All_2018\.get
# get_pop_All_18

"""

import sys

from ..helps import len_print
from ..ma_lists_bots import pop_final_all_keys2
from ..ma_lists_bots import New_P17_Finall
from ..ma_lists_bots import films_mslslat_tab
from ..ma_lists_bots import Jobs_new, Jobs_key
from ..ma_lists_bots import Sports_Keys_For_Label
from ..ma_lists_bots import By_table

from ..ma_lists_bots import Teams_new
from ..ma_lists_bots import pop_All_2018

pop_All_2018["country"] = "البلد"


def Add_to_pop_All_18(tab):
    for key, lab in tab.items():
        pop_All_2018[key] = lab


def get_pop_All_18(key, va=""):
    return pop_All_2018.get(key, va)


for gg, gg_lab in pop_final_all_keys2.items():
    gg2 = gg.lower()
    if not pop_All_2018.get(gg2):
        pop_All_2018[gg2] = gg_lab

# ---
for pla in Jobs_new:
    pla2 = pla.lower()
    if Jobs_new[pla]:
        if not pop_All_2018.get(pla2):
            pop_All_2018[pla2] = Jobs_new[pla]
# ---
for pla in Jobs_key:
    pla2 = pla.lower()
    if Jobs_key[pla]:
        if not pop_All_2018.get(pla2):
            pop_All_2018[pla2] = Jobs_key[pla]

# films_mslslat.py
for cyi in films_mslslat_tab:
    cyi2 = cyi.lower()
    if not pop_All_2018.get(cyi2):
        pop_All_2018[cyi2] = films_mslslat_tab[cyi]

for by in By_table:
    by2 = by.lower()
    if By_table[by]:
        if not pop_All_2018.get(by2):
            pop_All_2018[by2] = By_table[by]

for paa, taba in Teams_new.items():
    paa2 = paa.lower()
    if taba:
        if not pop_All_2018.get(paa2):
            pop_All_2018[paa2] = taba

for xo in list(New_P17_Finall):  #
    xo2 = xo.lower()
    if not pop_All_2018.get(xo2):
        pop_All_2018[xo2] = New_P17_Finall[xo]  # ["ar"]

for paa in Sports_Keys_For_Label:  #
    paa2 = paa.lower()
    if Sports_Keys_For_Label[paa]:
        if not pop_All_2018.get(paa2):
            pop_All_2018[paa2] = Sports_Keys_For_Label[paa]

# pop_All_2018["conflicts"] = "نزاعات"
pop_All_2018["by country"] = "حسب البلد"
pop_All_2018["in"] = "في"
pop_All_2018["films"] = "أفلام"
pop_All_2018["decades"] = "عقود"
pop_All_2018["women"] = "المرأة"
pop_All_2018["women in"] = "المرأة في"

# for le in Lenth:

pop_All_2018["medalists"] = "فائزون بميداليات"
pop_All_2018["gold medalists"] = "فائزون بميداليات ذهبية"
pop_All_2018["silver medalists"] = "فائزون بميداليات فضية"
pop_All_2018["bronze medalists"] = "فائزون بميداليات برونزية"

pop_All_2018["kingdom of"] = "مملكة"
pop_All_2018["kingdom-of"] = "مملكة"

olympicss = {
    "universiade competitors": "منافسون في الألعاب الجامعية",
    "universiade medalists": "فائزون بميداليات الألعاب الجامعية",
    "olympic medalists": "فائزون بميداليات أولمبية",
    "olympic competitors": "منافسون أولمبيون",
    "olympic gold medalists": "فائزون بميداليات ذهبية أولمبية",
    "olympic silver medalists": "فائزون بميداليات فضية أولمبية",
    "olympic bronze medalists": "فائزون بميداليات برونزية أولمبية",
    "paralympic competitors": "منافسون بارالمبيون",
    "pan american games competitors": "منافسون في دورة الألعاب الأمريكية",
    "commonwealth games competitors": "منافسون في ألعاب الكومنولث",
    "commonwealth games gold medalists": "فائزون بميداليات ذهبية في ألعاب الكومنولث",
    "winter olympics competitors": "منافسون في الألعاب الأولمبية الشتوية",
    "winter olympics medalists": "فائزون بميداليات أولمبية شتوية",
    "summer olympics medalists": "فائزون بميداليات أولمبية صيفية",
    "summer olympics competitors": "منافسون في الألعاب الأولمبية الصيفية",
}

olympicss["winter olympics competitors"] = "منافسون أولمبيون شتويون"
olympicss["summer olympics competitors"] = "منافسون أولمبيون صيفيون"
olympicss["olympics competitors"] = "منافسون أولمبيون"
olympicss["paralympic competitors"] = "منافسون بارالمبيون"
olympicss["southeast asian games competitors"] = "منافسون في ألعاب جنوب شرق آسيا"
olympicss["asian games competitors"] = "منافسون في الألعاب الآسيوية"
olympicss["maccabiah games competitors"] = "منافسون في الألعاب المكابيه"
olympicss["world championships competitors"] = "منافسون في بطولات العالم"
olympicss["african games competitors"] = "منافسون في الألعاب الإفريقية"
olympicss["european games competitors"] = "منافسون في الألعاب الأوروبية"
olympicss["mediterranean games competitors"] = "منافسون في الألعاب المتوسطية"
olympicss["universiade competitors"] = "منافسون في الألعاب الجامعية"
olympicss["commonwealth games competitors"] = "منافسون في ألعاب الكومنولث"
olympicss["central american games competitors"] = "منافسون في ألعاب أمريكا الوسطى"
olympicss["south american games competitors"] = "منافسون في ألعاب أمريكا الجنوبية"

medalists_type = {
    "%s medallists": "فائزون بميداليات %s",
    "%s medalists": "فائزون بميداليات %s",
    "%s gold medalists": "فائزون بميداليات ذهبية %s",
    "%s silver medalists": "فائزون بميداليات فضية %s",
    "%s bronze medalists": "فائزون بميداليات برونزية %s",
}

for tty, tty_lab in medalists_type.items():
    olympicss[tty % "pan american games"] = tty_lab % "في دورة الألعاب الأمريكية"
    olympicss[tty % "pan arab games"] = tty_lab % "في دورة الألعاب العربية"
    olympicss[tty % "world athletics indoor championships"] = tty_lab % "بطولة العالم لألعاب القوى داخل الصالات"
    # olympicss[ tty % " games" ] = tty_lab % "في "
    # olympicss[ tty % " games" ] = tty_lab % "في "
    # olympicss[ tty % " games" ] = tty_lab % "في "
    olympicss[tty % "military world games"] = tty_lab % "في دورة الألعاب العسكرية"
    olympicss[tty % "winter olympics"] = tty_lab % "في الألعاب الأولمبية الشتوية"
    olympicss[tty % "summer olympics"] = tty_lab % "في الألعاب الأولمبية الصيفية"
    olympicss[tty % "olympics"] = tty_lab % "أولمبية"
    olympicss[tty % "paralympic"] = tty_lab % "في الألعاب البارالمبية"
    olympicss[tty % "islamic solidarity games"] = tty_lab % "في ألعاب التضامن الإسلامي"
    olympicss[tty % "southeast asian games"] = tty_lab % "في ألعاب جنوب شرق آسيا"

    olympicss[tty % "asian games"] = tty_lab % "في الألعاب الآسيوية"
    olympicss[tty % "asian winter games"] = tty_lab % "في الألعاب الآسيوية الشتوية"
    olympicss[tty % "asian summer games"] = tty_lab % "في الألعاب الآسيوية الصيفية"

    olympicss[tty % "mediterranean games"] = tty_lab % "في الألعاب المتوسطية"
    olympicss[tty % "maccabiah games"] = tty_lab % "في الألعاب المكابيه"
    olympicss[tty % "world championships"] = tty_lab % "في بطولات العالم"
    olympicss[tty % "african games"] = tty_lab % "في الألعاب الإفريقية"
    olympicss[tty % "european games"] = tty_lab % "في الألعاب الأوروبية"

    olympicss[tty % "the universiade"] = tty_lab % "في الألعاب الجامعية"
    olympicss[tty % "universiade"] = tty_lab % "في الألعاب الجامعية"
    olympicss[tty % "winter universiade"] = tty_lab % "في الألعاب الجامعية الشتوية"
    olympicss[tty % "summer universiade"] = tty_lab % "في الألعاب الجامعية الصيفية"

    olympicss[tty % "commonwealth games"] = tty_lab % "في ألعاب الكومنولث"
    olympicss[tty % "commonwealth youth games"] = tty_lab % "في ألعاب الكومنولث الشبابية"
    olympicss[tty % "central american games"] = tty_lab % "في ألعاب أمريكا الوسطى"
    olympicss[tty % "central american and caribbean games"] = tty_lab % "في ألعاب أمريكا الوسطى والكاريبي"
    olympicss[tty % "south american games"] = tty_lab % "في ألعاب أمريكا الجنوبية"
    olympicss[tty % "youth olympics games"] = tty_lab % "في الألعاب الأولمبية الشبابية"
    olympicss[tty % "youth olympics"] = tty_lab % "في الألعاب الأولمبية الشبابية"
    olympicss[tty % "european youth olympic"] = tty_lab % "في الألعاب الأولمبية الشبابية الأوروبية"
    olympicss[tty % "european youth olympic winter"] = tty_lab % "في الألعاب الأولمبية الشبابية الأوروبية الشتوية"
    olympicss[tty % "youth olympic"] = tty_lab % "في الألعاب الأولمبية الشبابية"
    # olympicss[ tty % " games" ] = tty_lab % "في "

    olympicss[tty % "fis nordic world ski championships"] = tty_lab % "في بطولة العالم للتزلج النوردي على الثلج"

olympicss["fis nordic world ski championships medalists"] = "فائزون بميداليات بطولة العالم للتزلج النوردي على الثلج"

for olmp, olmp_lab in olympicss.items():
    pop_All_2018[olmp] = olmp_lab

Lenth = {}
Lenth["pop_All_2018"] = sys.getsizeof(pop_All_2018)
# ---
len_print.lenth_pri("matables_bots/bot_2018.py", Lenth, Max=10)
