import re
import functools
from typing import Callable
from ..ma_lists_bots import By_table, By_orginal2, By_table_orginal
from ..ma_lists_bots import New_P17_Finall
from ..matables_bots.bot_2018 import pop_All_2018
from ..p17_bots.nats import find_nat_others
from ..media_bots.films_bot import test_films


def print_put(s: str) -> None:
    # printe.output(s)
    pass


@functools.lru_cache(maxsize=None)
def get_label_for_by_part(by_part: str) -> str:
    """
    Tries to find a label for a given 'by' part of a category.
    """
    label = By_orginal2.get(by_part, "")
    if not label:
        label = test_films(by_part)
    if not label:
        label = find_nat_others(by_part)
    return label


@functools.lru_cache(maxsize=None)
def get_label_for_main_part(main_part: str) -> str:
    """
    Tries to find a label for the main part of a category.
    """
    main_part_lower = main_part.lower()
    if main_part_lower.startswith("the "):
        main_part_lower = main_part_lower[len("the ") :]

    label = New_P17_Finall.get(main_part_lower, "")
    if not label:
        label = pop_All_2018.get(main_part_lower, "")
    return label


def _handle_and_case(
    part1_str: str, part2_str: str, template: str, label_getter: Callable[[str], str]
) -> str:
    """
    Helper function to handle cases with 'and'.
    """
    part1_label = label_getter(part1_str)
    part2_label = label_getter(part2_str)
    if part1_label and part2_label:
        return template.format(part1_label, part2_label)
    return ""


@functools.lru_cache(maxsize=None)
def Make_By_lab(cate: str) -> str:
    """
    Translates categories that contain 'by' or 'and'.
    """
    cate_lower = cate.lower()

    # Case 1: "by .* and .*"
    match = re.match(r"^by (.*?) and (.*?)$", cate_lower)
    if match:
        return _handle_and_case(match.group(1), match.group(2), "حسب {} و{}", By_orginal2.get)

    # Case 2: "by .*"
    if cate_lower.startswith("by "):
        by_part = cate[len("by ") :]
        by_part_lab = get_label_for_by_part(by_part)
        if by_part_lab:
            return f"بواسطة {by_part_lab}"

    # Case 3: ".* by .*"
    match = re.match(r"^(.*?) (by .*)$", cate, flags=re.IGNORECASE)
    if match:
        main_part = match.group(1)
        by_part = match.group(2)

        main_part_lab = get_label_for_main_part(main_part)
        by_part_lab = By_table.get(by_part.lower(), "") or By_table_orginal.get(by_part.lower(), "")

        if main_part_lab and by_part_lab:
            return f"{main_part_lab} {by_part_lab}"

    # Case 4: ".* and .*"
    match = re.match(r"(.*?) and (.*)", cate, flags=re.IGNORECASE)
    if match:
        return _handle_and_case(match.group(1), match.group(2), "{} و{}", get_label_for_main_part)

    return ""
