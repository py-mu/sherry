import threading
from typing import TypeVar, Optional, Type, Union, Any

T = TypeVar('T')


class Badge(object):
    id_entity = None
    __bases__ = (object,)
    __instance__ = {}
    _instance_lock = threading.Lock()  # Note: 单例锁(instance lock)

    def __new__(cls, *args, source: Optional[Type[T]] = None, singleton=True, relative=True, return_class=False,
                **kwargs) -> Union[Type[T], T]:
        ...

    @staticmethod
    def decoration(badge: Any, relative=True):
        pass
