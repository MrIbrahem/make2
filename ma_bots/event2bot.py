import re
import sys
from .. import printe
from ..fix import fixtitle
from ..bots import tmp_bot
from ..date_bots import with_years_bot
from .lab_seoo_bot import event_Lab_seoo
from ..o_bots import univer
from ..matables_bots.bot import safo, titttto
from ..helps.print_bot import print_put
from .contry_bot import Get_contry
from .dodo_bots.event2bot_dodo import make_lab_dodo

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
event2_cash = {}
Find_stubs = {1: "-stubs" in sys.argv}


def university_handler(category):
    """
    Handles university-related categories.
    """
    return univer.test_Universities(category)


def country_handler(category):
    """
    Handles country-related categories.
    """
    if all(x not in category for x in [" in ", " of ", " from ", " by ", " at "]):
        # if category starts with a number
        if re.match(r"^\d", category):
            lab = with_years_bot.Try_With_Years(category)
            if lab:
                return f"تصنيف:{lab}"
        else:
            return Get_contry(category)
    return None


def date_handler(category_r, category):
    """
    Handles date and time parsing.
    """
    yy = (
        r"\d+th century BCE|\d+th millennium BCE|\d+th century BC|\d+th millennium BC|\d+th century|\d+th millennium"
        + r"|\d+st century BCE|\d+st millennium BCE|\d+st century BC|\d+st millennium BC|\d+st century|\d+st millennium"
        + r"|\d+rd century BCE|\d+rd millennium BCE|\d+rd century BC|\d+rd millennium BC|\d+rd century|\d+rd millennium"
        + r"|\d+nd century BCE|\d+nd millennium BCE|\d+nd century BC|\d+nd millennium BC|\d+nd century|\d+nd millennium"
        + r"|\d+ century BCE|\d+ millennium BCE|\d+ century BC|\d+ millennium BC"
        + r"|\d+ century|\d+ millennium|\d+s BCE|\d+ BCE|\d+s BC|\d+ BC"
    )
    en_dash = r"|\d+\–\d+"
    MINUS = r"|\d+\−\d+"
    keybord = r"|\d+\-\d+"
    yy += en_dash + MINUS + keybord + r"|\d+s|\d+"
    MONTHSTR2 = "(january |february |march |april |may |june |july |august |september |october |november |december |)"
    tita_year = r"Category\:" + MONTHSTR2 + "(" + yy + "|).*"
    tita_year = tita_year.lower()
    tita_other = r"\s*(" + safo + r"|)\s*(" + titttto + r"|)\s*(.*|).*"
    tita = r"Category\:" + MONTHSTR2 + "(" + yy.lower() + "|)" + tita_other
    tita = tita.lower()

    category = category.replace("−century", " century").replace("–century", " century")
    if not category.lower().startswith("category:"):
        category = f"Category:{category}"

    ddd = r"category\:(january|february|march|april|may|june|july|august|september|october|november|december|)\s*"
    test_month = re.sub(ddd, "", category.lower())

    if test_month == category:
        Tita_year = r"category\:(|)\s*(" + yy + ").*"
    else:
        Tita_year = tita_year

    Tita_year = Tita_year.lower()
    _category_ = category.replace("-century", " century").replace("-millennium", " millennium")
    category3 = re.sub(r"category:", "", _category_.lower(), flags=re.IGNORECASE)

    return make_lab_dodo(_category_, Tita_year, tita, tita_other, category3, category, category3, category_r)


def stub_handler(category_r):
    """
    Handles "stub" categories.
    """
    category = category_r.replace("−century", " century").replace("–century", " century")
    if not category.lower().startswith("category:"):
        category = f"Category:{category}"

    if category.endswith(" stubs") and Find_stubs[1]:
        category = category.replace(" stubs", "", 1)
        sub_ar_label = event_Lab_seoo("", category) or tmp_bot.Work_Templates(category)
        if sub_ar_label:
            return f"بذرة {sub_ar_label}"
    return None


def event2(category_r):
    """
    Translates an event-related category by trying a series of strategies.
    """
    cash_key = category_r.replace("category:", "").lower().strip()
    if not category_r or cash_key in event2_cash:
        return event2_cash.get(cash_key, "")

    handlers = [
        university_handler,
        country_handler,
        lambda cat: date_handler(category_r, cat),
        stub_handler,
    ]

    ar_label = ""
    for handler in handlers:
        ar_label = handler(category_r)
        if ar_label:
            break

    if ar_label and re.sub(en_literes, "", ar_label, flags=re.IGNORECASE) == ar_label:
        ar_label = fixtitle.fixlab(ar_label, en=category_r)
        if not ar_label.startswith("تصنيف:"):
            ar_label = f"تصنيف:{ar_label}"

    event2_cash[cash_key] = ar_label
    return ar_label
