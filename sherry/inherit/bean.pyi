import threading
import traceback
from typing import TypeVar, Dict, Union, List, Type

T = TypeVar('T')

class Bean:
    _instance_dict: Dict[str, Dict[str, Union[List[traceback.FrameSummary], type, bool]]]
    _instance_lock: threading.Lock  # Note: 实例锁

    @classmethod
    def instance(cls: Type[T]) -> T: ...

    @classmethod
    def _instance(cls: Type[T]) -> T: ...
