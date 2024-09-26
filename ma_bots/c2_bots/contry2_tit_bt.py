#!/usr/bin/python3
"""
from .c2_bots.contry2_tit_bt import contry_2_tit

"""

import re
from ... import printe

from ...pop_format_bot import Tit_ose_Nmaes

from ...helps.print_bot import print_put, output_test

from .c_1_c_2_labs import c_1_1_lab, c_2_1_lab
from .cn_lab import make_cnt_lab


def make_conas(tat_o, contry):
    """Process a country name based on a specified separator.

    This function takes a separator and a country name, splits the country
    name around the separator, and formats the resulting parts. It handles
    variations in casing and whitespace, and it also modifies the output
    based on the specified separator. The function aims to return two
    formatted strings that represent parts of the country name.

    Args:
        tat_o (str): The separator used to split the country name.
        contry (str): The country name to be processed.

    Returns:
        tuple: A tuple containing two formatted strings derived from the input
        country name.
    """

    contry2_no_lower = contry.strip()
    contry2 = contry.lower().strip()

    con_1 = contry2.split(tat_o)[0]
    con_2 = contry2.split(tat_o)[1]

    Mash = f"^(.*?)(?:{tat_o}?)(.*?)$"

    Type_t = re.sub(Mash, r"\g<1>", contry2_no_lower, flags=re.IGNORECASE)
    contry_t = re.sub(Mash, r"\g<2>", contry2_no_lower, flags=re.IGNORECASE)

    test_N = contry2.lower().replace(con_1.strip().lower(), "")

    try:
        test_N = test_N.strip().replace(con_2.strip().lower(), "")
    except Exception:
        printe.output(f'<<lightblue>> >>>> <<lightblue>> except, test_N:"{test_N}",con_2:"{con_2}",con_1:"{con_1}"')
        test_N = re.sub(con_2.strip().lower(), "", test_N)
        test_N = test_N.replace(con_2.strip().lower(), "")

    if tat_o.strip() == "by":
        con_2 = f"by {con_2}"
        contry_t = f"by {contry_t}"

    if tat_o.strip() in ["of", "-of"]:
        Type_t = f"{Type_t} of"
        con_1 = f"{con_1} of"

    print_put(f'>>>> con_1:"{con_1.strip()}",test_N:"{test_N.strip()}",con 2:"{con_2.strip()}"')

    if test_N and test_N.strip() != tat_o.strip():
        print_put(f'>>>> <<lightblue>> test_N != "",Type_t:"{Type_t}",tat_o:"{tat_o}",contry_t:"{contry_t}"')
        con_1 = Type_t
        con_2 = contry_t

    return con_1, con_2


def make_sps(tat_o, c_1_l, cona_1):
    """Generate a specific string based on input parameters.

    This function takes three string inputs and returns a specific string
    based on the value of the first input (`tat_o`). It checks the value of
    `tat_o` against predefined conditions and returns corresponding Arabic
    phrases. The function also considers the context provided by the second
    input (`c_1_l`) and the third input (`cona_1`) to determine the
    appropriate output.

    Args:
        tat_o (str): The first input string that determines the output.
        c_1_l (str): The second input string that may influence the output.
        cona_1 (str): The third input string that may influence the output.

    Returns:
        str: A specific Arabic phrase based on the conditions evaluated
        from the input strings.
    """

    sps = " "

    if tat_o.strip() == "to" and cona_1.strip() == "ambassadors of":
        sps = " لدى "
    elif tat_o.strip() == "to":
        sps = " إلى "
    elif tat_o.strip() == "on":
        sps = " على "
    elif tat_o.strip() == "about":
        sps = " عن "
    elif tat_o.strip() in Tit_ose_Nmaes:
        if tat_o.strip() != "by":
            sps = f" {Tit_ose_Nmaes[tat_o.strip()]} "
    elif tat_o.strip() == "based in":
        sps = " مقرها في "

    if tat_o.strip() == "to" and c_1_l.startswith("سفراء "):
        sps = " لدى "

    return sps


def contry_2_tit(tat_o, contry, With_Years=True):
    """Convert country name and generate labels based on input parameters.

    This function takes a country name and a type of operation (tat_o) to
    generate corresponding labels. It processes the country name, checks for
    specific conditions, and formats the output accordingly. The function
    also handles cases where additional words need to be appended to the
    labels based on the context of the operation.

    Args:
        tat_o (str): The type of operation (e.g., "in", "from").
        contry (str): The name of the country to process.
        With_Years (bool): A flag indicating whether to include years in the output. Defaults to
            True.

    Returns:
        str: The generated label based on the input parameters. Returns an empty
            string if
        certain conditions are not met.
    """

    print_put(f'>>>> <<lightblue>> Get_contry2: <<lightyellow>> New Way to find lab for "{contry.lower().strip()}".')

    con_1, con_2 = make_conas(tat_o, contry)

    print_put(f'2060 con_1:"{con_1}",con_2:"{con_2}",tat_o:"{tat_o}"')

    c_2_l = c_2_1_lab(With_Years, con_2)

    c_1_l = c_1_1_lab(tat_o, With_Years, con_1)

    cona_1 = con_1.strip().lower()
    cona_2 = con_2.strip().lower()

    fAAA = '>>>> XX--== <<lightgreen>> Ccon_1:"%s", lab"%s", cona_2:"%s", lab"%s", cnt_test: "%s"'

    contry2 = contry.lower().strip()
    cnt_test = contry2

    if c_2_l == "" or c_1_l == "":
        print_put(fAAA % (cona_1, c_1_l, cona_2, c_2_l, cnt_test))
        return ""

    cnt_test = cnt_test.replace(cona_1, "").replace(cona_2, "").replace(tat_o.strip(), "").strip()

    if (tat_o.strip() == "in" or cona_1.endswith(" in")) and (not cona_1.endswith(" في")):
        output_test(f'>>>> Add في to c_1_l : "{c_1_l}"')
        c_1_l = f"{c_1_l} في"

    elif (tat_o.strip() == "from" or cona_2.endswith(" from")) and (not c_2_l.endswith(" من")):
        output_test(f'>>>> Add من to c_2_l : "{c_2_l}"')
        c_2_l = f"من {c_2_l}"

    print_put(fAAA % (cona_1, c_1_l, cona_2, c_2_l, cnt_test))

    sps = make_sps(tat_o, c_1_l, cona_1)

    if cnt_test:
        print_put(f'>>>> cnt_test:"{cnt_test}" != "" ')

    cnt_labe = make_cnt_lab(tat_o, contry2, c_2_l, c_1_l, cona_1, cona_2, sps)

    return cnt_labe
