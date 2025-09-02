import re
import functools
from typing import Tuple, Optional, Dict, Any
from ...ma_lists_bots import (
    People_key, All_Nat, Nat_women, Nat_men, Jobs_key_mens, Jobs_key_womens
)
from ...ma_lists_bots import (
    en_is_nat_ar_is_man, en_is_nat_ar_is_women, change_male_to_female,
    priffix_lab_for_2018, Main_priffix, Main_priffix_to
)
from ..get_helps import get_con_3
from ...helps.print_bot import output_test4
from ..priffix_bot import Women_s_priffix_work, priffix_Mens_work
from ..jobs_mainbot import Jobs
from .relegin_jobs import try_relegins_jobs
from .langs_w import Lang_work


@functools.lru_cache(maxsize=None)
def handle_prefix(cate: str) -> Tuple[str, str, str]:
    """
    Handles prefixes in the category string.
    """
    for me, melab in Main_priffix.items():
        me2 = f"{me} "
        if cate.lower().startswith(me2.lower()):
            main_ss = me
            cate = cate[len(me2):]
            main_lab = melab
            if cate.endswith("women") or cate.endswith("women's"):
                if main_lab in change_male_to_female:
                    main_lab = change_male_to_female[main_lab]
            return main_ss, main_lab, cate
    return "", "", cate


@functools.lru_cache(maxsize=None)
def handle_direct_translation(cate: str) -> Optional[str]:
    """
    Handles direct translations from various dictionaries.
    """
    if cate == "people":
        return "أشخاص"
    return (
        People_key.get(cate)
        or Jobs_key_womens.get(cate)
        or Lang_work(cate)
        or Jobs_key_mens.get(cate)
    )


@functools.lru_cache(maxsize=None)
def handle_nationality_translation(cate: str, main_ss: str, main_lab: str) -> Tuple[str, str, str]:
    """
    Handles translations that involve nationalities.
    """
    job_example, nat = get_con_3(cate, All_Nat, "nat")
    if not job_example:
        return "", main_lab, ""

    if main_ss not in priffix_lab_for_2018:
        return "", main_lab, ""

    # Try to find a translation for women
    job_example_lab = en_is_nat_ar_is_women.get(job_example.strip())
    if job_example_lab:
        contry_lab = job_example_lab.format(Nat_women[nat])
        main_lab = priffix_lab_for_2018[main_ss]["women"]
        return contry_lab, main_lab, job_example_lab

    # Try to find a translation for men
    job_example_lab = en_is_nat_ar_is_man.get(job_example.strip())
    if job_example_lab:
        contry_lab = job_example_lab.format(Nat_men[nat])
        main_lab = priffix_lab_for_2018[main_ss]["men"]
        return contry_lab, main_lab, job_example_lab

    return "", main_lab, ""


@functools.lru_cache(maxsize=None)
def test4_2018_Jobs(cate: str, out: bool = False, tab: Optional[Dict[str, Any]] = None) -> str:
    """
    Retrieve job-related information based on the specified category.
    """
    original_cate = cate
    cate = re.sub(r"_", " ", cate)
    main_ss, main_lab, cate = handle_prefix(cate)

    if main_ss.strip() == "fictional" and cate.strip().startswith("female"):
        main_lab = "{} خياليات"

    contry_lab = handle_direct_translation(cate)

    job_example_lab = ""
    if not contry_lab:
        contry_lab, main_lab, job_example_lab = handle_nationality_translation(cate, main_ss, main_lab)

    if not contry_lab:
        job_example, nat = get_con_3(cate, All_Nat, "nat")
        if job_example:
            contry_lab = Jobs(cate, nat, job_example, Type="nat")

    if not contry_lab:
        contry_lab = Women_s_priffix_work(cate)

    if not contry_lab:
        contry_lab = priffix_Mens_work(cate)

    if main_ss and main_lab and contry_lab:
        contry_lab = main_lab.format(contry_lab)
        if main_ss in Main_priffix_to and job_example_lab:
            job_example_lab = job_example_lab.format("").strip()
            _, nat = get_con_3(cate, All_Nat, "nat")
            if nat:
                contry_lab = Main_priffix_to[main_ss].format(nat=Nat_women[nat], t=job_example_lab)

    if not contry_lab:
        contry_lab = try_relegins_jobs(cate)

    output_test4(f'end test4_2018_Jobs "{original_cate}" , contry_lab:"{contry_lab}"')
    return contry_lab or ""
