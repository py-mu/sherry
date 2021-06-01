# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 20:13
"""
import threading
import traceback
import warnings
from typing import TypeVar, List

T = TypeVar('T')

warnings.simplefilter("default")


class Bean:
    """
    如果需要获取单例则需要使用方法 instance()，如果重复的实例化，将会影响单例对象
    """
    _instance_dict = {}
    _instance_lock = threading.Lock()  # Note: 单例锁(instance lock)

    def __post_init__(self):
        bean_name = str(self.__class__.__name__)
        _instance = Bean._instance_dict.get(bean_name)
        if 'inited' not in _instance:

            _instance.update({'caller': traceback.extract_stack()})
            _instance.update({'inited': True})
        else:
            traceback_object = _instance.get('caller')[0]
            message = (f"实体 {bean_name} 已经装载在 {traceback_object.name}. 即 {traceback_object.filename} "
                       f"的 {traceback_object.lineno} 行. 对已经装载的bean对象进行实例化会修改其属性产生未知的后果, "
                       f"首先保证你已经知道这样修改所带来的的负面影响, 否则请使用 instance() 方法获取对象."
                       )
            warnings.warn(message, DeprecationWarning)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance_dict'):
            Bean._instance_dict = {}
        cls_name = cls.__name__
        if cls_name not in Bean._instance_dict.keys():
            with Bean._instance_lock:
                _instance = object.__new__(cls)
                Bean._instance_dict[cls_name] = {'instance': _instance}
        return Bean._instance_dict[cls_name].get('instance')

    @classmethod
    def instance(cls):
        """
        获取其子类的单例返回, 需要通过此类获取实例化的对象，否则会创建一个新的实例。
        只会获取最远亲的子类。

        To get the singleton return of its subclass,
        you need to get the instantiated object through this class, otherwise a new instance will be created.
        Only get the most distant relatives.
        """
        subclasses: List[type(cls)] = cls.__subclasses__()
        subclass: cls = cls._instance()
        if subclasses:
            _class_ = cls.__subclasses__()[-1]
            if _class_.__subclasses__():
                return getattr(_class_, 'instance')()
            return getattr(_class_, '_instance')()
        return subclass

    @classmethod
    def _instance(cls):
        """对类进行实例化，不会重复运行init方法"""
        return cls.__new__(cls)
