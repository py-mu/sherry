import functools
from typing import List, Type

from sherry.inherit.bean import EventCell

__instance_func__: List[Overrider.install]



def register(func):
    """注册方法"""

    @functools.wraps(func)
    def warps():
        __instance_func__.append(func)

    return warps


class Overrider:
    custom_events: List[Type[EventCell]]

    @staticmethod
    def install(): ...
