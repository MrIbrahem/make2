import abc
from ..p17_bots.us_stat import Work_US_State
from ..o_bots.popl import Work_peoples
from ..p17_bots import nats
from ..o_bots import univer
from ..sports_bots import team_work
from ..jobs_bots.test_4 import Jobs_in_Multi_Sports
from ..jobs_bots.test4_bots.t4_2018_jobs import test4_2018_Jobs
from . import ye_ts_bot
from ..media_bots.films_bot import test_films
from . import event2bot
from ..ma_lists_bots import New_P17_Finall, Ambassadors_tab
from ..fromnet.wd_bot import find_wikidata
from ..matables_bots.bot_2018 import pop_All_2018
from ..matables_bots.centries_bot import centries_years_dec
from ..matables_bots.bot import New_Lan
from ..fix import fixtitle
import re
from ..helps.print_bot import mainoutput

class TranslationRequest:
    def __init__(self, category_r, category3):
        self.category_r = category_r
        self.category3 = category3
        self.category3_no_lower = category3.strip()
        self.category3_lower = category3.lower().strip()
        self.translation = None

class BaseHandler(abc.ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abc.abstractmethod
    def handle(self, request: TranslationRequest):
        pass

    def next(self, request: TranslationRequest):
        if self._successor:
            return self._successor.handle(request)
        return None

class NewP17FinallHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = New_P17_Finall.get(request.category3_lower)
        return translation or self.next(request)

class AmbassadorsTabHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = Ambassadors_tab.get(request.category3_lower)
        return translation or self.next(request)

class TeamWorkClubHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = team_work.Get_team_work_Club(request.category3_no_lower)
        return translation or self.next(request)

class Event2Handler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = event2bot.event2(request.category3_lower)
        return translation or self.next(request)

class PopAll2018Handler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = pop_All_2018.get(request.category3_lower)
        return translation or self.next(request)

class CentriesYearsDecHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = centries_years_dec.get(request.category3_lower)
        return translation or self.next(request)

class Test4_2018_JobsHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = test4_2018_Jobs(request.category3_lower, out=mainoutput[1])
        return translation or self.next(request)

class JobsInMultiSportsHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = Jobs_in_Multi_Sports(request.category3_no_lower, out=mainoutput[1])
        return translation or self.next(request)

class UniverHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = univer.test_Universities(request.category3_lower)
        return translation or self.next(request)

class TestFilmsHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = test_films(request.category3_lower, fa=request.category_r)
        return translation or self.next(request)

class NatsHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = nats.find_nat_others(request.category3_lower, fa=request.category_r)
        return translation or self.next(request)

class YeTsBotHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = ye_ts_bot.translate_general_category(request.category3_lower)
        return translation or self.next(request)

class WorkUSStateHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = Work_US_State(request.category3_lower)
        return translation or self.next(request)

class WorkPeoplesHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        translation = Work_peoples(request.category3_lower)
        return translation or self.next(request)

class Test3Handler(BaseHandler):
    def handle(self, request: TranslationRequest):
        if request.category3_lower in New_Lan:
            labs = New_Lan[request.category3_lower]
            if labs and re.sub("[a-zA-Z]", "", labs, flags=re.IGNORECASE) == labs:
                return f"تصنيف:{fixtitle.fixlab(labs, en=request.category_r)}"
        return self.next(request)

class WikidataHandler(BaseHandler):
    def handle(self, request: TranslationRequest):
        if " " not in request.category3_lower.strip():
            translation = find_wikidata(request.category3_lower)
            return translation or self.next(request)
        return self.next(request)
