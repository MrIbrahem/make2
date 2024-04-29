"""

Usage:
from  make2.bot import event # event(tab, **kwargs)

from  make2 import bot # bot.event(tab, **kwargs)

from  make2 import bot as MA_MAIN # MA_MAIN.event(tab, **kwargs)
"""

from . import main
from .media_bots import films_bot  # test_films


def event(tab, **kwargs):
    return main.event(tab, **kwargs)


def test_films(cate, fa=""):
    return films_bot.test_films(cate, fa=fa)
