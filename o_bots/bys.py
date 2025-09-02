import re

from ..ma_lists_bots import By_table, By_orginal2, By_table_orginal
from ..ma_lists_bots import New_P17_Finall
from ..matables_bots.bot_2018 import pop_All_2018
from ..p17_bots.nats import find_nat_others
from ..media_bots.films_bot import test_films


def print_put(s):
    # printe.output(s)
    pass


def get_label_for_by_part(by_part):
    """
    Tries to find a label for a given 'by' part of a category.
    """
    label = By_orginal2.get(by_part, "")
    if not label:
        label = test_films(by_part)
    if not label:
        label = find_nat_others(by_part)
    return label


def get_label_for_main_part(main_part):
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


def Make_By_lab(cate):
    """
    Translates categories that contain 'by' or 'and'.
    """
    cate_lower = cate.lower()

    # Case 1: "by .* and .*"
    match = re.match(r"^by (.*?) and (.*?)$", cate_lower)
    if match:
        by1 = match.group(1)
        by2 = match.group(2)
        by1_lab = By_orginal2.get(by1, "")
        by2_lab = By_orginal2.get(by2, "")
        if by1_lab and by2_lab:
            return f"حسب {by1_lab} و{by2_lab}"

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
        by_part_lab = By_table.get(by_part.lower(), "")
        if not by_part_lab:
            by_part_lab = By_table_orginal.get(by_part.lower(), "")

        if main_part_lab and by_part_lab:
            return f"{main_part_lab} {by_part_lab}"

    # Case 4: ".* and .*"
    match = re.match(r"(.*?) and (.*)", cate, flags=re.IGNORECASE)
    if match:
        part1 = match.group(1)
        part2 = match.group(2)

        part1_lab = get_label_for_main_part(part1)
        part2_lab = get_label_for_main_part(part2)

        if part1_lab and part2_lab:
            return f"{part1_lab} و{part2_lab}"

    return ""
