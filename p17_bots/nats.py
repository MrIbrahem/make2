import re
import functools
from typing import Optional, Tuple, Dict, Any
from .. import printe
from ..ma_lists_bots import sport_formts_for_p17, nat_p17_oioi
from ..ma_lists_bots import fanco_line, Sports_Keys_For_Team
from ..matables_bots.bot import New_players, Add_to_main2_tab
from .. import ma_lists_sport_lab as sport_lab
from ..ma_lists_bots import All_Nat, Nat_women
from ..jobs_bots.get_helps import get_con_3


def print_put(s: str) -> None:
    # printe.output(s)
    pass


@functools.lru_cache(maxsize=None)
def get_sport_template_label(sport_format_string: str) -> str:
    """
    Generates a sport label from a template.
    This function uses a placeholder 'oioioi' to match templates and then replaces it
    with the specific sport key.
    e.g. "football junior championships" -> "بطولات الناشئين لكرة القدم"
    """
    # First, check for a direct match in the pre-compiled formats
    direct_label = sport_formts_for_p17.get(sport_format_string, "")
    if direct_label:
        return direct_label

    # If no direct match, try to match a template using fanco_line regex
    match = re.match(fanco_line, sport_format_string, flags=re.IGNORECASE)
    if not match:
        return ""

    sport_key = match.group(1)
    # Use 'oioioi' as a placeholder for the sport key to match the template
    template_key = re.sub(sport_key, "oioioi", sport_format_string, flags=re.IGNORECASE)

    if template_key in nat_p17_oioi:
        sport_key_label = Sports_Keys_For_Team.get(sport_key, "")
        template_label = nat_p17_oioi[template_key]

        if sport_key_label and template_label:
            # Replace the placeholder with the actual sport label
            final_label = template_label.replace("oioioi", sport_key_label)
            if "oioioi" not in final_label:
                return final_label
    return ""


@functools.lru_cache(maxsize=None)
def handle_female_sport_translation(category_part: str, country_key: str) -> str:
    """
    Handles translation for female sport categories.
    """
    label_template = sport_lab.Get_sport_formts_female_nat(category_part)
    if label_template:
        return label_template.format(nat=Nat_women[country_key])
    return ""


@functools.lru_cache(maxsize=None)
def handle_generic_sport_translation(
    category_part: str, country_key: str, original_category: str
) -> Tuple[str, Optional[Dict[str, Any]]]:
    """
    Handles translation for generic sport categories.
    Returns the translated label and the data to be added to the tables.
    """
    label_template = get_sport_template_label(category_part)
    country_label = All_Nat[country_key].get("ar", "")

    if label_template and country_label:
        final_label = label_template.format(nat=country_label)
        new_data = {
            "main2_tab": [(category_part, label_template), (final_label, country_label)],
            "new_players": {original_category: final_label},
        }
        return final_label, new_data
    return "", None


@functools.lru_cache(maxsize=None)
def find_nat_others(cate: str, fa: str = "") -> str:
    """
    Finds translations for sports-related categories that include a nationality.
    Caches the results.
    """
    translated_label = ""
    category_lower = cate.lower()

    # Extract the country and the rest of the category
    category_part, country_key = get_con_3(category_lower, Nat_women, "nat")

    if category_part and country_key:
        # First, try to find a translation for a female-specific sport category
        translated_label = handle_female_sport_translation(category_part, country_key)

        # If that fails, try a generic sport translation
        if not translated_label:
            translated_label, new_data = handle_generic_sport_translation(
                category_part, country_key, cate
            )
            if new_data:
                for key, value in new_data["main2_tab"]:
                    Add_to_main2_tab(key, value)
                New_players.update(new_data["new_players"])

    return translated_label


if __name__ == "__main__":
    print_put = printe.output
    print("_________________")
    # python3 core8/pwb.py make/bots/nats
    op = get_sport_template_label("football junior championships")
    print(op)

    zo = find_nat_others("yemeni football junior championships")
    print(zo)
