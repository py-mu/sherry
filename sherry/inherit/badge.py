# coding=utf-8
"""
    create by pymu
    on 2021/6/20
    at 0:36
"""
import threading


class Badge(object):
    """
    徽章是所有成员联络的基础
    <img src=''/>

    Badges are the basis for all members to contact.
    """
    __bases__ = (object,)
    id_entity = None
    __instance__ = {}
    _instance_lock = threading.Lock()  # Note: 单例锁(instance lock)

    def __new__(cls, *args, badge=None, singleton=True, relative=True, **kwargs):
        """
        通过获取组内最远亲的子类，获取其子类的单例返回, 需要通过此类获取实例化的对象，否则会创建一个新的实例。
        只会获取最远亲的子类。当然这也会牺牲init方法初始化参数的问题，只能依托于重构方法时
        手动创建。

        To get the singleton return of its subclass,
        you need to get the instantiated object through this class, otherwise a new instance will be created.
        Only get the most distant relatives.

        :param badge: 需要创建的类或子类 The class or subclass that needs to be created
        :param singleton: 是否从对象列表中获取单例 Whether to get the singleton from the object list, default True
        :param relative: 是否获取其子类 Whether to get its subclass
        """
        if badge:
            group_class = badge.__subclasses__()
            if not group_class or not relative:
                subclass = badge
            else:
                # Only get the most distant relatives
                subclass = group_class[-1]
        else:
            subclass = cls
        cls_name = subclass.__name__
        if cls_name not in Badge.__instance__:
            with Badge._instance_lock:
                obj = super(subclass, subclass).__new__(subclass)
                Badge.__instance__.update({
                    cls_name: obj
                })
        if not singleton:
            obj = super(subclass, subclass).__new__(subclass)
            super(subclass, obj).__init__(*args, **kwargs)
            return obj
        else:
            return Badge.__instance__[cls_name]
