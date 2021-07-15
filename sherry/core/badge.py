# coding=utf-8
"""
    create by pymu
    on 2021/6/20
    at 0:36
"""
import logging
import threading
import traceback


class BadgeError(ValueError):
    ...


class BadgeNotFoundError(BadgeError):
    ...


def get_subclasses_graph(base, relative, badge_name):
    """获取子类有向图"""

    def subclass_recursion(cls):
        subclasses = {}
        for subclass in cls.__subclasses__():
            subclasses.update({
                subclass: subclass_recursion(subclass)
            })
        return subclasses

    def format_recursion(graph: dict, format_list, item=None, ):
        item = item or []
        for k, v in graph.items():
            new_item = item + [k]
            if not v:
                format_list.append(new_item)
            else:
                format_recursion(v, format_list, new_item)

    def check_graph():
        """返回最长继承链， 如果相等"""
        result = []
        format_recursion({base: subclass_recursion(base)}, result)
        max_list = max(result, key=len)
        max_size = len(max_list)
        temp_class = None
        # 如果使用名字索引则对所有的子孙进行匹配
        # 否则只对最远亲的那一脉进行匹配
        sub_list = result if badge_name else filter(lambda x: len(x) == max_size, result)

        for i in sub_list:
            temp_class = temp_class or i[-1]
            if badge_name:
                badge_list = list(filter(lambda c: c.__name__ == badge_name, i))
                if badge_list:
                    temp_class = badge_list[0]
                    break
                continue
            if temp_class is not i[-1]:
                temp_class = i[-1]
                ss = [" - ".join([c.__name__ for c in _]) for _ in result]
                logging.warning('The loading class has malformed branches, so there is loading ambiguity, '
                                'please use single chain inheritance as much as possible.'
                                'or set the badge_name what you want to used.'
                                ' detail: source: {} target: {}， \n\nbranch: \n\t{}. \n\nuse: \n\t{}\n'.format(
                    base,
                    temp_class,
                    "\n\t".join(ss),
                    " - ".join([_.__name__ for _ in i]) + "(use)")
                )
                break
        if badge_name and not badge_name == temp_class.__name__:
            raise BadgeNotFoundError("can't found a badge {} by name".format(badge_name))
        return temp_class or base

    if not relative:
        return base
    return check_graph()


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

    def __new__(cls,
                *args,
                source=None,
                singleton=True,
                relative=True,
                return_class=False,
                badge_name='',
                **kwargs):
        """
        通过获取组内最远亲的子类，获取其子类的单例返回, 需要通过此类获取实例化的对象，否则会创建一个新的实例。
        只会获取最远亲的子类。当然这也会牺牲init方法初始化参数的问题，只能依托于重构方法时
        手动创建。

        To get the singleton return of its subclass,
        you need to get the instantiated object through this class, otherwise a new instance will be created.
        Only get the most distant relatives.

        :param source: 需要创建的类或子类 The class or subclass that needs to be created
        :param singleton: 是否从对象列表中获取单例 Whether to get the singleton from the object list, default True
        :param relative: 是否获取其子类 Whether to get its subclass
        :param return_class: 是否其类型
        :param badge_name: 在畸形分支中获取指定的子类 Get the specified subclass in the malformed branch.
        """
        if not source:
            raise ValueError('badge 需要使用键值对的的形式传入, 否则会引发递归调用')
        target = get_subclasses_graph(source, relative, badge_name)
        if return_class:
            return target
        cls_name = target.__name__
        caller = traceback.extract_stack()[-2]  # type: traceback.FrameSummary
        logging.debug(
            '{} in {} -> {} install subclass <{}> from <{}>.'.format(
                caller.filename,
                caller.lineno,
                caller.name,
                target.__module__ + target.__name__,
                source.__module__ + source.__name__
            ))
        if cls_name not in Badge.__instance__:
            obj = target(*args, **kwargs)
            with Badge._instance_lock:
                Badge.__instance__.update({
                    cls_name: obj
                })
        if not singleton:
            obj = target(*args, **kwargs)
            return obj
        else:
            return Badge.__instance__[cls_name]

    @staticmethod
    def decoration(badge, relative=True):
        """
        确定需要装饰的类，这样你不要改动这里的代码，你只需要在需要类上使用被装饰的父类，
        其逻辑也很简单，就是从被装饰后的父类子集类中查找一个合适子类，然后再实现继承

        Determine the class to be decorated.

            class A:
                pass

            class B(A):
                pass

        Use example:

            @Badge.decoration(badge=A)
            class Test(A):
                pass

        Equivalent to:

            class Test(B):
                pass

        :param badge: 需要创建的类或子类 The class or subclass that needs to be created
        :param relative: 是否获取其子类 Whether to get its subclass
        """

        def _build_(mcs):
            new_bases = []
            tt = None  # Note: 注入类 Injection class.
            ts = None  # Note: 被注入类 Injected class.
            for i in mcs.__bases__:
                if i is badge:
                    tt = Badge(source=badge, relative=relative, singleton=False, return_class=True)
                    ts = i
                    new_bases.append(tt)
                else:
                    new_bases.append(i)
            if tt:
                logging.debug('injection class "{}" from "{}", happened at "{}".'.format(tt, ts, mcs.__name__))
            return type(mcs.__name__, tuple(new_bases), dict(mcs.__dict__))

        return _build_
