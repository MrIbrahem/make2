#!/usr/bin/python3
"""
"""

from typing import Iterable, Mapping
from ma_lists import lenth_pri as _lenth_pri


def lenth_pri(
    bot: str,
    tab: Mapping[str, int | float],
    Max: int=10000,
    lens: Iterable[str] | None=None,
) -> None:
    return _lenth_pri(
        bot,
        tab,
        Max,
        lens,
    )
