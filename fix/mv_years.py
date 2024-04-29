"""

from make2.fix.mv_years import move_years

تصنيف:1974–75 في دوريات كرة قدم لبنانية
Category:1974–75 in Lebanese football leagues
"""

import re
import sys
import re

# YEARS_REGEX = r'(\d+\sق[\s\.]م|\d+)|عقد\s(\d+\sق[\s\.]م|\d+)|القرن\s(\d+\sق[\s\.]م|\d+)|الألفية\s(\d+\sق[\s\.]م|\d+)'
YEARS_REGEX = r"(\d+[-–]\d+|\d+\sق[\s\.]م|\d+)|عقد\s(\d+\sق[\s\.]م|\d+)|القرن\s(\d+\sق[\s\.]م|\d+)|الألفية\s(\d+\sق[\s\.]م|\d+)"


def print_test(s):
    return s


def move_3(text_str):
    """
    A function that takes in a string and searches for a specific pattern within it. The function replaces underscores in the string with spaces and then uses a regular expression to search for a pattern of the form '{first_part} حسب {by_part} في {date}'.

    Parameters:
    - text_str (str): The input string.

    Returns:
    - str: The modified string if a match is found, otherwise the original string.
    """

    # ---
    # تصنيف:اتحاد الرجبي حسب البلد في 1989
    text_str = text_str.replace("_", " ")
    # ---
    new_text = text_str
    # ---
    # result = re.search(r'^(.*)\sحسب\s([\s\w]+)\sفي\s(القرن\s\d+|عقد\s\d+|\d+\sق[\s\.]م|\d+)$', text_str)
    # result = re.search(fr'^(.*)\sحسب\s([\s\w]+)\sفي\s(?P<first_part>{YEARS_REGEX})$', text_str)
    # ---
    # result = re.search(r'^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>.*?)$', text_str)
    if result := re.search(rf"^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>{YEARS_REGEX})$", text_str):
        # [[تصنيف:اتحاد الرجبي في 1989 حسب البلد]]
        # ---
        first_part = result.group("first_part")
        by_part = result.group("by_part")
        date = result.group("date")
        # ---
        new_text = f"{first_part} في {date} حسب {by_part}"
        # ---
        print_test(f"move_by_in: new_text: {new_text}")
    else:
        print_test("move_by_in: no match")
    # ---
    if new_text != text_str:
        new_text = re.sub(r"\s+", " ", new_text)
        new_text = re.sub(r"\bق\.م\b", "ق م", new_text)
        new_text = new_text.replace(" في في ", " في ")
    # ---
    return new_text


def move_by_in(text_str):
    """
    A function that takes in a string and searches for a specific pattern within it. The function replaces underscores in the string with spaces and then uses a regular expression to search for a pattern of the form '{first_part} حسب {by_part} في {date}'.

    Parameters:
    - text_str (str): The input string.

    Returns:
    - str: The modified string if a match is found, otherwise the original string.
    """

    # ---
    # تصنيف:اتحاد الرجبي حسب البلد في 1989
    text_str = text_str.replace("_", " ")
    # ---
    new_text = text_str
    # ---
    # result = re.search(r'^(.*)\sحسب\s([\s\w]+)\sفي\s(القرن\s\d+|عقد\s\d+|\d+\sق[\s\.]م|\d+)$', text_str)
    # result = re.search(fr'^(.*)\sحسب\s([\s\w]+)\sفي\s(?P<first_part>{YEARS_REGEX})$', text_str)
    # ---
    # result = re.search(r'^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>.*?)$', text_str)
    if result := re.search(rf"^(?P<first_part>.*)\sحسب\s(?P<by_part>[\s\w]+)\sفي\s(?P<date>{YEARS_REGEX})$", text_str):
        # [[تصنيف:اتحاد الرجبي في 1989 حسب البلد]]
        # ---
        first_part = result.group("first_part")
        by_part = result.group("by_part")
        date = result.group("date")
        # ---
        new_text = f"{first_part} في {date} حسب {by_part}"
        # ---
        print_test(f"move_by_in: new_text: {new_text}")
    else:
        print_test("move_by_in: no match")
    # ---
    if new_text != text_str:
        new_text = re.sub(r"\s+", " ", new_text)
        new_text = re.sub(r"\bق\.م\b", "ق م", new_text)
        new_text = new_text.replace(" في في ", " في ")
    # ---
    return new_text


def move_years_first(text_str):
    """
    Generates a function comment for the given function body in a markdown code block with the correct language syntax.

    Args:
        text_str (str): The string to be processed.

    Returns:
        str: The processed string.
    """
    # ---
    new = text_str
    # ---
    # التعبير العادي للبحث عن النص المطلوب
    # pattern = r"^(?P<first_part>(\d+ ق[\s\.]م|\d+)|عقد (\d+ ق[\s\.]م|\d+)|القرن (\d+ ق[\s\.]م|\d+)|الألفية (\d+ ق[\s\.]م|\d+)) في (?P<second_part>[^0-9]*)$"
    pattern = rf"^(?P<first_part>{YEARS_REGEX})\sفي\s(?P<second_part>[^0-9]*)$"
    if match := re.match(pattern, text_str):
        # ---
        first_part = match.group("first_part").strip()
        second_part = match.group("second_part").strip()
        # ---
        print_test(f"{first_part=}")
        print_test(f"{second_part=}")
        # ---
        skip_it = [
            "أفلام",
            "الأفلام",
        ]
        # ---
        if second_part in skip_it:
            return text_str
        # ---- "^.*?_في_.*?_في_.*?$"
        if second_part.find(" في x") != -1:
            print_test('second_part.find(" في ") != -1:')
            return text_str
        # ---
        # إعادة ترتيب الجملة
        new = f"{second_part} في {first_part}"
        # ---
        # if the second part ends with "حسب [\s\w]+"
        # move it to the end
        # ---
        if result := re.search(r"^(.*)\sحسب\s([\s\w]+)$", second_part):
            print_test("<<yellow>> find حسب in result:")
            new = f"{result.group(1)} في {first_part}" + f" حسب {result.group(2)}"
    else:
        print_test("move_years no match")
        # text_str = move_by_in(text_str)
    # ---
    if new != text_str:
        new = re.sub(r"\s+", " ", new)
        new = re.sub(r"\bق\.م\b", "ق م", new)
        new = new.replace(" في في ", " في ")
    # ---
    return new


def move_years(text_str):
    # ---
    text_str = text_str.replace("_", " ").strip()
    # ---
    cat_ns = False
    # ---
    if text_str.startswith("تصنيف:"):
        cat_ns = True
        text_str = text_str.replace("تصنيف:", "")
    # ---
    new_text = move_years_first(text_str)
    # ---
    if new_text == text_str:
        new_text = move_by_in(text_str)
    # ---
    # if new_text == text_str:
    # new_text = move_3(text_str)
    # ---
    if cat_ns:
        new_text = f"تصنيف:{new_text}"
    # ---
    return new_text


if __name__ == "__main__":
    from make2 import printe

    print_test = printe.output
    # python3 core8/pwb.py make2/fix/mv_years test
    # python3 core8/pwb.py make2/fix/mv_years أشخاص أمريكيون شماليون حسب الجنسية في القرن 17
    text_list = [
        "أشخاص أمريكيون شماليون حسب الجنسية في القرن 17",
        "1989 في اتحاد الرجبي حسب البلد",
        "1881_في_الرياضة_في_رود_آيلاند",
        "القرن_19_في_الرياضة_في_رود_آيلاند",
        "هجمات_في_كندا_في_عقد_2020",
        "عقد_2020_في_مجتمع_في_مدريد",
        "عقد_2020_في_مجتمع_في_مدريد_حسب_المدينة_والبلد",
        "عقد_2020_حسب_المدينة_والبلد_في_مجتمع_في_مدريد",
        "القرن 17 في أشخاص أمريكيون شماليون حسب الجنسية",
        "مرشحون في انتخابات الولايات المتحدة حسب السنة في القرن 21",
        "منافسون في ألعاب الكومنولث حسب السنة في القرن 20",
        "أشخاص حسب النزاع في القرن 5 ق م",
        "المرأة في القرن 19 حسب المهنة والجنسية",
        "المرأة حسب المهنة والجنسية في القرن 19",
        "رياضة حسب القارة في عقد 1940",
        "كنديون حسب الأصل العرقي أو الوطني في القرن 20",
        "مسلسلات تلفزيونية كوميدية أمريكية حسب النوع الفني في عقد 1960",
        "",
        "يونانيون حسب المهنة في القرن 9",
        "القرن 21 في يونانيون في حسب المهنة",
        "تصنيف:1974–75 في دوريات كرة قدم لبنانية",
        "",
        "",
        "",
        "",
        "",
        "",
    ]
    lista = []
    if "test" in sys.argv:
        lista = text_list
    else:
        text = " ".join(sys.argv[1:])
        lista = [text]
    # ---
    same = []
    # ---
    for text in lista:
        text = text.replace("_", " ")
        if not text:
            continue
        new = move_years(text)
        if new != text:
            print_test(f'old: "{text}"')
            print_test(f'<<green>>new: "{new}"')
            print_test("----------")
        else:
            same.append(text)
    # ---
    for text in same:
        print_test(f'same: "{text}"')
