"""

Usage:
from .bot import event # event(tab, **kwargs)

from . import bot # bot.event(tab, **kwargs)

from . import bot as MA_MAIN # MA_MAIN.event(tab, **kwargs)
"""

from . import main
from .media_bots import films_bot  # test_films
# from .jobs_bots.test4_bots.langs_w import Lang_work

def event(tab, return_no_labs=False, **kwargs):
    return main.event(tab, return_no_labs=return_no_labs, **kwargs)


def test_films(cate, fa=""):
    return films_bot.test_films(cate, fa=fa)
