from typing import Dict, Any, List
from . import main
from .media_bots import films_bot  # test_films


def event(tab: Dict[str, Any], return_no_labs: bool = False, **kwargs: Any) -> List[str]:
    return main.event(tab, return_no_labs=return_no_labs, **kwargs)


def test_films(cate: str, fa: str = "") -> str:
    return films_bot.test_films(cate, fa=fa)
