"""
from . import fax2
# list_of_cat, Find_wd, Find_ko, foot_ballers, category_lab = fax2.get_list_of_and_cat3(category3, category3_nolower)

"""

import sys
from ..helps.print_bot import print_put
from .squad_title_bot import get_squad_title

Find_stubs = {1: True if "-stubs" in sys.argv else False}


def get_list_of_and_cat3(category3, category3_nolower):
    foot_ballers = False
    Find_wd = False
    Find_ko = False
    category_lab = ""
    list_of_cat = ""

    if category3.startswith("women members of "):
        list_of_cat = "عضوات {}"
        category3 = category3.replace("women members of ", "", 1)

    elif category3.endswith(" footballers"):
        foot_ballers = True
        if category3.endswith(" women's footballers"):
            Find_wd = True
            Find_ko = True
            list_of_cat = "لاعبات {}"
            category3 = category3_nolower.replace(" women's footballers", "", 1)

        elif category3.endswith(" female footballers"):
            Find_wd = True
            Find_ko = True
            list_of_cat = "لاعبات {}"
            category3 = category3_nolower.replace(" female footballers", "", 1)

        elif category3.endswith("c. footballers"):
            Find_wd = True
            list_of_cat = "لاعبو {}"
            category3 = category3_nolower.replace(" footballers", "", 1)

        elif category3.endswith(" footballers"):
            Find_wd = True
            Find_ko = True
            list_of_cat = "لاعبو {}"
            category3 = category3_nolower.replace(" footballers", "", 1)

    elif category3.startswith("discoveries by "):
        Find_wd = True
        list_of_cat = "اكتشافات بواسطة {}"
        category3 = category3.replace("discoveries by ", "", 1)

    elif category3.startswith("lists of "):
        list_of_cat = "قوائم {}"
        category3 = category3.replace("lists of ", "", 1)

    elif category3.startswith("children of "):
        list_of_cat = "أطفال {}"
        category3 = category3.replace("children of ", "", 1)

    elif category3.startswith("association football matches navigational boxes by teams:"):
        list_of_cat = "صناديق تصفح مباريات كرة قدم حسب الفرق:{}"
        category3 = category3.replace("association football matches navigational boxes by teams:", "", 1)
    elif category3.endswith(" squad templates"):
        list_of_cat = "قوالب تشكيلات {}"
        category3 = category3.replace(" squad templates", "", 1)
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = cate_labs
            list_of_cat = "قوالب {}"

    elif category3.endswith(" squad navigational boxes"):
        list_of_cat = "قوالب تصفح تشكيلات {}"
        category3 = category3.replace(" squad navigational boxes", "", 1)
        cate_labs = get_squad_title(category3)
        if cate_labs:
            category_lab = cate_labs
            list_of_cat = "قوالب تصفح {}"
    elif category3.startswith("presidents of "):
        list_of_cat = "رؤساء {}"
        category3 = category3.replace("presidents of ", "", 1)

    elif category3.startswith("family of "):
        list_of_cat = "عائلة {}"
        category3 = category3.replace("family of ", "", 1)

    elif category3.endswith(" stubs") and Find_stubs[1]:
        list_of_cat = "بذرة {}"
        category3 = category3.replace(" stubs", "", 1)
    elif category3.endswith(" alumni"):
        Find_wd = True
        list_of_cat = "خريجو {}"
        category3 = category3.replace(" alumni", "", 1)

    elif category3.endswith(" board members"):
        Find_wd = True
        list_of_cat = "أعضاء مجلس {}"
        category3 = category3.replace(" board members", "", 1)
    elif category3.endswith(" faculty"):
        Find_wd = True
        list_of_cat = "أعضاء هيئة تدريس {}"
        category3 = category3.replace(" faculty", "", 1)

    elif category3.endswith(" trustees"):
        Find_wd = True
        list_of_cat = "أمناء {}"
        category3 = category3.replace(" trustees", "", 1)

    elif category3.endswith(" award winners"):
        list_of_cat = "حائزو جوائز {}"
        category3 = category3.replace(" award winners", "", 1)

    elif category3.endswith(" awards winners"):
        list_of_cat = "حائزو جوائز {}"
        category3 = category3.replace(" awards winners", "", 1)

    elif category3.endswith(" sidebars"):
        list_of_cat = "أشرطة جانبية {}"
        category3 = category3.replace(" sidebars", "", 1)

    elif category3.endswith(" charts"):
        list_of_cat = "مخططات {}"
        category3 = category3.replace(" charts", "", 1)

    elif category3.endswith(" sidebar templates"):
        list_of_cat = "قوالب أشرطة جانبية {}"
        category3 = category3.replace(" sidebar templates", "", 1)

    elif category3.endswith(" politics and government templates"):
        list_of_cat = "قوالب سياسة وحكومة {}"
        category3 = category3.replace(" politics and government templates", "", 1)
    elif category3.endswith("c. playerss") or category3.endswith("c. playerss"):
        Find_wd = True
        Find_ko = True
        list_of_cat = "لاعبو {}"
        category3 = category3_nolower.replace(" playerss", "", 1)
    elif category3.endswith("c. players") or category3.endswith("c. players"):
        Find_ko = True
        Find_wd = True
        list_of_cat = "لاعبو {}"
        category3 = category3_nolower.replace(" players", "", 1)
    elif category3.endswith(" episodes"):
        Find_wd = True
        if category3.endswith(" (season 1) episodes"):
            list_of_cat = "حلقات {} الموسم 1"
            category3 = category3_nolower.replace(" (season 1) episodes", "", 1)

        elif category3.endswith(" (season 2) episodes"):
            list_of_cat = "حلقات {} الموسم 2"
            category3 = category3_nolower.replace(" (season 2) episodes", "", 1)

        elif category3.endswith(" (season 3) episodes"):
            list_of_cat = "حلقات {} الموسم 3"
            category3 = category3_nolower.replace(" (season 3) episodes", "", 1)

        elif category3.endswith(" (season 4) episodes"):
            list_of_cat = "حلقات {} الموسم 4"
            category3 = category3_nolower.replace(" (season 4) episodes", "", 1)

        elif category3.endswith(" (season 5) episodes"):
            list_of_cat = "حلقات {} الموسم 5"
            category3 = category3_nolower.replace(" (season 5) episodes", "", 1)

        elif category3.endswith(" (season 6) episodes"):
            list_of_cat = "حلقات {} الموسم 6"
            category3 = category3_nolower.replace(" (season 6) episodes", "", 1)

        elif category3.endswith(" (season 7) episodes"):
            list_of_cat = "حلقات {} الموسم 7"
            category3 = category3_nolower.replace(" (season 7) episodes", "", 1)

        elif category3.endswith(" (season 8) episodes"):
            list_of_cat = "حلقات {} الموسم 8"
            category3 = category3_nolower.replace(" (season 8) episodes", "", 1)

        elif category3.endswith(" (season 9) episodes"):
            list_of_cat = "حلقات {} الموسم 9"
            category3 = category3_nolower.replace(" (season 9) episodes", "", 1)

        elif category3.endswith(" episodes"):
            list_of_cat = "حلقات {}"
            category3 = category3_nolower.replace(" episodes", "", 1)

    elif category3.endswith(" playerss"):
        Find_ko = True
        Find_wd = True
        if category3.endswith(" playerss"):
            list_of_cat = "لاعبو {}"
            category3 = category3_nolower.replace(" playerss", "", 1)

    elif category3.endswith(" players"):
        Find_ko = True
        Find_wd = True
        if category3.endswith(" players"):
            list_of_cat = "لاعبو {}"
            category3 = category3_nolower.replace(" players", "", 1)

    elif category3.endswith(" sports navigational boxes"):
        list_of_cat = "صناديق تصفح الرياضة في {}"
        category3 = category3.replace(" sports navigational boxes", "", 1)

    elif category3.endswith(" events"):
        list_of_cat = "أحداث {}"
        category3 = category3.replace(" events", "", 1)
    elif category3.endswith(" navigational boxes"):
        list_of_cat = "صناديق تصفح {}"
        category3 = category3.replace(" navigational boxes", "", 1)

    elif category3.endswith(" infobox templates"):
        list_of_cat = "قوالب معلومات {}"
        category3 = category3.replace(" infobox templates", "", 1)

    elif category3.endswith(" templates"):
        list_of_cat = "قوالب {}"
        category3 = category3.replace(" templates", "", 1)

    elif category3.endswith(" tournaments"):
        list_of_cat = "بطولات {}"
        category3 = category3.replace(" tournaments", "", 1)

    elif category3.endswith(" commissioners"):
        # "Category:Major Indoor Soccer League (1978–1992) commissioners"
        # "تصنيف:مفوضو الدوري الرئيسي لكرة القدم داخل الصالات (1978–1992)",
        list_of_cat = "مفوضو {}"
        category3 = category3.replace(" commissioners", "", 1)

    elif category3.endswith(" commentators"):
        # "Category:Major Indoor Soccer League (1978–1992) commentators"
        # "تصنيف:معلقو الدوري الرئيسي لكرة القدم داخل الصالات (1978–1992)",
        list_of_cat = "معلقو {}"
        category3 = category3.replace(" commentators", "", 1)

    if list_of_cat:
        print_put(f'<<lightblue>> list_of_cat:"{list_of_cat}", category3:"{category3}",Find_wd:{str(Find_wd)},Find_ko:{str(Find_ko)} ')

    return list_of_cat, Find_wd, Find_ko, foot_ballers, category_lab
