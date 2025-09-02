import re

from ..ma_lists_bots import (
    All_contry_with_nat,
    All_contry_with_nat_keys_is_en,
    sport_formts_en_p17_ar_nat,
    military_format_women_without_al_from_end,
    military_format_women_without_al,
    military_format_women,
    military_format_men,
)

test_Army_Cash = {}


def print_put(s):
    # printe.output(s)
    pass


def find_country_from_category(cate):
    """
    Finds the country from the category string and returns the remaining part of the category,
    and the women and men labels for that country.
    """
    for contry, contry_dict in All_contry_with_nat.items():
        contry2 = contry_dict.get("en", "")
        women_labs = contry_dict.get("women", "")
        men_labs = contry_dict.get("men", "")

        if not contry2 or (not women_labs and not men_labs):
            continue

        contry2_lower = f"{contry2.lower()} "
        # "the " is a common prefix that should be stripped
        contry3_lower = contry2_lower[4:].strip() if contry2_lower.startswith("the ") else contry2_lower
        contry4_lower = f"{contry.lower()} "

        if cate.startswith(contry2_lower):
            return cate[len(contry2_lower):].strip(), women_labs, men_labs
        if cate.startswith(contry3_lower):
            return cate[len(contry3_lower):].strip(), women_labs, men_labs
        if cate.startswith(contry4_lower):
            return cate[len(contry4_lower):].strip(), women_labs, men_labs

    return "", "", ""


def handle_military_format_women_without_al_from_end(cate):
    """
    Handles translation for categories that start with a military format for women,
    without 'al' at the end.
    e.g. Category:Unmanned_aerial_vehicles_of_Jordan -> طائرات بدون طيار أردنية
    """
    for nana, nanalab in military_format_women_without_al_from_end.items():
        nana2 = f"{nana} "
        if cate.startswith(nana2):
            gagaga = cate[len(nana2) :].strip()
            con_labe = All_contry_with_nat_keys_is_en.get(gagaga, {}).get("women", "")
            if con_labe:
                return nanalab.format(nat=con_labe)
    return ""


def handle_military_format_women_without_al(con_77, women_lab):
    """
    Handles translation for categories that match a military format for women, without 'al'.
    """
    con_77_lab = military_format_women_without_al.get(con_77, "")
    if con_77_lab:
        return con_77_lab.format(nat=women_lab)
    return ""


def handle_endswith_table(con_77, women_lab):
    """
    Handles translation for categories that end with specific keywords like 'civilians', 'generals', etc.
    """
    endswith_table = {
        " civilians": "مدنيو {}",
        " generals": "جنرالات {}",
        " accidents and incidents": "حوادث {}",
    }
    for xi, xi_lab in endswith_table.items():
        if con_77.endswith(xi):
            con_88 = con_77.replace(xi, "", 1)
            con_88_lab = military_format_women.get(con_88, "")
            if con_88_lab:
                women_lab_no_al = re.sub(r" ", " ال", women_lab)
                women_lab = f"ال{women_lab_no_al}"
                cnt_la = con_88_lab.format(nat=women_lab)
                return xi_lab.format(cnt_la)
    return ""


def handle_military_format_men(con_77, men_lab):
    """
    Handles translation for categories that match a military format for men.
    e.g. Category:French_labour_law
    """
    con_77_lab = military_format_men.get(con_77, "")
    if con_77_lab and men_lab:
        men_lab_no_al = re.sub(r" ", " ال", men_lab)
        men_lab = f"ال{men_lab_no_al}"
        return con_77_lab.format(nat=men_lab)
    return ""


def handle_sport_formts_en_p17_ar_nat(con_77, men_lab):
    """
    Handles translation for categories that match a sport format.
    e.g. Category:China Basketball Federation
    """
    con_77_lab = sport_formts_en_p17_ar_nat.get(con_77, "")
    if con_77_lab and men_lab:
        men_lab_no_al = re.sub(r" ", " ال", men_lab)
        men_lab = f"ال{men_lab_no_al}"
        return con_77_lab.format(nat=men_lab)
    return ""


def test_Army(cate):
    """
    Translates a category related to military subjects.
    """
    if cate in test_Army_Cash:
        return test_Army_Cash[cate]

    cate_lower = cate.lower()
    cnt_la = ""

    con_77, women_lab, men_lab = find_country_from_category(cate_lower)

    # if a country was not found, try to find a translation without a country
    if not con_77:
        cnt_la = handle_military_format_women_without_al_from_end(cate_lower)
    # if a country was found, try to find a translation for the rest of the category
    else:
        handlers = [
            handle_military_format_women_without_al,
            handle_endswith_table,
            handle_military_format_men,
            handle_sport_formts_en_p17_ar_nat,
        ]

        for handler in handlers:
            # pass the correct lab based on the handler
            lab = men_lab if handler in [handle_military_format_men, handle_sport_formts_en_p17_ar_nat] else women_lab
            cnt_la = handler(con_77, lab)
            if cnt_la:
                break

    if cnt_la:
        test_Army_Cash[cate] = cnt_la

    return cnt_la
