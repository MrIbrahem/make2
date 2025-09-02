import re
import functools
from typing import Dict, Tuple
from ..ma_lists_bots import (
    All_contry_with_nat,
    All_contry_with_nat_keys_is_en,
    sport_formts_en_p17_ar_nat,
    military_format_women_without_al_from_end,
    military_format_women_without_al,
    military_format_women,
    military_format_men,
)


def print_put(s: str) -> None:
    # printe.output(s)
    pass


@functools.lru_cache(maxsize=None)
def find_country_from_category(category: str) -> Tuple[str, str, str]:
    """
    Finds the country from the category string and returns the remaining part of the category,
    and the women and men labels for that country.
    """
    for country, country_data in All_contry_with_nat.items():
        en_country_name = country_data.get("en", "")
        women_label = country_data.get("women", "")
        men_label = country_data.get("men", "")

        if not en_country_name or (not women_label and not men_label):
            continue

        en_country_name_lower = f"{en_country_name.lower()} "
        # "the " is a common prefix that should be stripped
        en_country_name_lower_no_the = (
            en_country_name_lower[4:].strip() if en_country_name_lower.startswith("the ") else en_country_name_lower
        )
        country_lower = f"{country.lower()} "

        if category.startswith(en_country_name_lower):
            return category[len(en_country_name_lower) :].strip(), women_label, men_label
        if category.startswith(en_country_name_lower_no_the):
            return category[len(en_country_name_lower_no_the) :].strip(), women_label, men_label
        if category.startswith(country_lower):
            return category[len(country_lower) :].strip(), women_label, men_label

    return "", "", ""


@functools.lru_cache(maxsize=None)
def handle_military_format_women_without_al_from_end(category: str) -> str:
    """
    Handles translation for categories that start with a military format for women,
    without 'al' at the end.
    e.g. Category:Unmanned_aerial_vehicles_of_Jordan -> طائرات بدون طيار أردنية
    """
    for format_str, translation_template in military_format_women_without_al_from_end.items():
        if category.startswith(f"{format_str} "):
            country_name = category[len(format_str) + 1 :].strip()
            country_label = All_contry_with_nat_keys_is_en.get(country_name, {}).get("women", "")
            if country_label:
                return translation_template.format(nat=country_label)
    return ""


@functools.lru_cache(maxsize=None)
def handle_military_format_women_without_al(category_part: str, women_label: str) -> str:
    """
    Handles translation for categories that match a military format for women, without 'al'.
    """
    translation_template = military_format_women_without_al.get(category_part, "")
    if translation_template:
        return translation_template.format(nat=women_label)
    return ""


@functools.lru_cache(maxsize=None)
def handle_endswith_table(category_part: str, women_label: str) -> str:
    """
    Handles translation for categories that end with specific keywords like 'civilians', 'generals', etc.
    """
    endswith_table = {
        " civilians": "مدنيو {}",
        " generals": "جنرالات {}",
        " accidents and incidents": "حوادث {}",
    }
    for suffix, translation_template in endswith_table.items():
        if category_part.endswith(suffix):
            sub_category = category_part.replace(suffix, "", 1)
            sub_category_translation = military_format_women.get(sub_category, "")
            if sub_category_translation:
                women_label_with_al = f"ال{re.sub(r' ', ' ال', women_label)}"
                translated_subcategory = sub_category_translation.format(nat=women_label_with_al)
                return translation_template.format(translated_subcategory)
    return ""


def _format_with_men_label(category_part: str, men_label: str, format_dict: Dict[str, str]) -> str:
    """
    Helper function to format a translation with a men's label.
    """
    translation_template = format_dict.get(category_part, "")
    if translation_template and men_label:
        men_label_with_al = f"ال{re.sub(r' ', ' ال', men_label)}"
        return translation_template.format(nat=men_label_with_al)
    return ""


@functools.lru_cache(maxsize=None)
def handle_military_format_men(category_part: str, men_label: str) -> str:
    """
    Handles translation for categories that match a military format for men.
    e.g. Category:French_labour_law
    """
    return _format_with_men_label(category_part, men_label, military_format_men)


@functools.lru_cache(maxsize=None)
def handle_sport_formats(category_part: str, men_label: str) -> str:
    """
    Handles translation for categories that match a sport format.
    e.g. Category:China Basketball Federation
    """
    return _format_with_men_label(category_part, men_label, sport_formts_en_p17_ar_nat)


@functools.lru_cache(maxsize=None)
def test_Army(category: str) -> str:
    """
    Translates a category related to military subjects.
    """
    category_lower = category.lower()
    translation = ""

    category_part, women_label, men_label = find_country_from_category(category_lower)

    if not category_part:
        translation = handle_military_format_women_without_al_from_end(category_lower)
    else:
        handlers = [
            (handle_military_format_women_without_al, women_label),
            (handle_endswith_table, women_label),
            (handle_military_format_men, men_label),
            (handle_sport_formats, men_label),
        ]
        for handler, label in handlers:
            translation = handler(category_part, label)
            if translation:
                break
    return translation
