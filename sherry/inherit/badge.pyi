import threading
from typing import List, TypeVar, Optional, Type

T = TypeVar('T')


class Badge(object):
    id_entity = None
    __bases__ = (object,)
    __instance__ = {}
    _instance_lock = threading.Lock()  # Note: 单例锁(instance lock)

    def __new__(cls, *args, badge: Optional[Type[T]] = None, singleton=True, relative=True, **kwargs) -> T:
        pass

    def __subclasses__(self) -> List[Badge]: ...
