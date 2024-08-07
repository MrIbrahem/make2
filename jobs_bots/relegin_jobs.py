#!/usr/bin/python3
"""

"""
from ..jobs_bots.jobs_mainbot import Jobs  # , Jobs2
from ..ma_lists_bots import religious_keys_PP
from ..helps.print_bot import output_test4
from ..jobs_bots.get_helps import get_con_3

try_relegins_jobs_cash = {}


def try_relegins_jobs(cate):
    # ---
    cach_key = cate.lower().strip()
    # ---
    if cach_key in try_relegins_jobs_cash:
        return try_relegins_jobs_cash[cach_key]
    # ---
    output_test4(f"\t xx start: <<lightred>>try_relegins_jobs >> <<lightpurple>> cate:{cate}")
    # ---
    contry_lab = ""
    # ---
    job_example, nat = get_con_3(cate, religious_keys_PP, "religions")
    # ---
    Tab = religious_keys_PP.get(nat, {})
    # ---
    if job_example:
        contry_lab = Jobs(cate, nat, job_example, Type="rel", tab=Tab)
    # ---
    output_test4(f"\t xx end: <<lightred>>try_relegins_jobs <<lightpurple>> cate:{cate}, contry_lab:{contry_lab} ")
    # ---
    try_relegins_jobs_cash[cach_key] = contry_lab
    # ---
    return contry_lab
