import sys
import re
from . import fax2
from . import list_cat_format
from .. import ma_lists_sport_lab as sport_lab
from ..date_bots import year_lab
from ..o_bots import univer
from ..ma_lists_bots import New_P17_Finall
from ..fromnet import kooora
from ..fromnet.wd_bot import find_wikidata
from ..format_bots import pp_ends_with, pp_ends_with_pase, change_cat
from ..fix import fixtitle
from ..matables_bots.bot_2018 import pop_All_2018
from ..bots import tmp_bot
from .lab_seoo_bot import event_Lab_seoo
from .contry2_bot import Get_contry2
from . import ye_ts_bot

en_literes = "[abcdefghijklmnopqrstuvwxyz]"
Find_f_wikidata = {1: "nowikidata" not in sys.argv}


class TranslationPipeline:
    def __init__(self, category_r):
        self.category_r = category_r
        self.category = ""
        self.category3 = ""
        self.orginal_category3 = ""
        self.category3_nolower = ""
        self.list_of_cat = ""
        self.Find_wd = False
        self.Find_ko = False
        self.foot_ballers = False
        self.category_lab = ""

    def preprocess(self):
        self.category = self.category_r.lower().replace("_", " ")
        if not self.category.startswith("category:"):
            self.category = f"category:{self.category}"
        self.category = change_cat(self.category)

        self.category3_nolower = self.category_r
        if self.category3_nolower.startswith("Category:"):
            self.category3_nolower = self.category3_nolower.split("Category:")[1]

        self.category3 = self.category.lower()
        if self.category3.startswith("category:"):
            self.category3 = self.category3.split("category:")[1]

        self.orginal_category3 = self.category3

    def run(self):
        self.preprocess()

        self.category_lab = fax2.get_list_of_and_cat3_with_lab2(self.category3, self.category3_nolower)
        if self.category_lab:
            return self.postprocess()

        (
            self.list_of_cat,
            self.Find_wd,
            self.Find_ko,
            self.foot_ballers,
            self.category3,
        ) = fax2.get_list_of_and_cat3(self.category3, self.category3_nolower)

        handlers = [
            lambda: Get_contry2(self.orginal_category3) if self.list_of_cat == "لاعبو {}" else None,
            lambda: year_lab.make_year_lab(self.category3),
            lambda: sport_lab.Get_New_team_xo(self.category3),
            lambda: Get_contry2(self.category3),
            lambda: kooora.kooora_team(self.category3, Local=Find_f_wikidata[1]) if self.Find_ko else None,
        ]
        for handler in handlers:
            lab = handler()
            if lab:
                self.category_lab = lab
                break

        if self.list_of_cat == "لاعبو {}" and self.category_lab:
            self.list_of_cat = ""

        self.handle_pp_ends_with()

        if not self.category_lab:
            self.category_lab = event_Lab_seoo("", self.category3)

        self.format_list_of_cat()

        if self.list_of_cat and not self.category_lab:
            self.list_of_cat = ""
            self.category_lab = event_Lab_seoo(self.category_r, self.orginal_category3)

        if not self.category_lab:
            self.category_lab = tmp_bot.Work_Templates(self.orginal_category3)

        if not self.category_lab:
            self.handle_cricketers()

        return self.postprocess()

    def handle_pp_ends_with(self):
        if self.list_of_cat or self.category_lab:
            return

        for pri_ff, vas in pp_ends_with_pase.items():
            if self.category3.endswith(pri_ff.lower()):
                self.list_of_cat = vas
                self.category3 = self.category3.replace(pri_ff.lower(), "", 1).strip()
                return
        for pri_ff, vasv in pp_ends_with.items():
            if self.category3.endswith(pri_ff.lower()):
                self.list_of_cat = vasv
                self.category3 = self.category3.replace(pri_ff.lower(), "", 1).strip()
                return

    def format_list_of_cat(self):
        if self.list_of_cat and self.category_lab:
            self.category_lab, self.list_of_cat = list_cat_format.list_of_cat_func(
                self.category_r, self.category_lab, self.list_of_cat, self.foot_ballers
            )

    def handle_cricketers(self):
        category32 = ""
        list_of_cat2 = ""
        if self.category3.endswith(" cricketers"):
            list_of_cat2 = "لاعبو كريكت من {}"
            category32 = self.category3_nolower.replace(" cricketers", "", 1)
        elif self.category3.endswith(" cricket captains"):
            list_of_cat2 = "قادة كريكت من {}"
            category32 = self.category3_nolower.replace(" cricket captains", "", 1)

        if list_of_cat2 and category32:
            category3_lab = New_P17_Finall.get(category32.lower(), "")
            if category3_lab:
                self.category_lab = list_of_cat2.format(category3_lab)

    def postprocess(self):
        if self.category_lab:
            fixed = fixtitle.fixlab(self.category_lab, en=self.category_r)
            return f"تصنيف:{fixed}"
        return ""


def event_Lab(cate_r):
    pipeline = TranslationPipeline(cate_r)
    return pipeline.run()
