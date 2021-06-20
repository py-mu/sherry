import threading
import traceback
from typing import TypeVar, Dict, Union, List, Type, Optional

from PyQt5.QtCore import QEvent, QTimerEvent, QChildEvent
from PyQt5.QtGui import QMouseEvent, QWheelEvent, QTabletEvent, QKeyEvent, QFocusEvent, QPaintEvent, QMoveEvent, \
    QResizeEvent, QCloseEvent, QShowEvent, QHideEvent, QContextMenuEvent, QDropEvent, QDragLeaveEvent
from PyQt5.QtWidgets import QWidget

T = TypeVar('T')


class Bean:
    _instance_dict: Dict[str, Dict[str, Union[List[traceback.FrameSummary], type, bool]]]
    _instance_lock: threading.Lock  # Note: 实例锁

    @classmethod
    def instance(cls: Type[T]) -> T: ...

    @classmethod
    def _instance(cls: Type[T]) -> T: ...


class QCustomEvent(object):
    pass


EVENT_TYPE = Union[
    QEvent,
    QTimerEvent,  #         定时器事件
    QMouseEvent,  #         鼠标事件
    QWheelEvent,  #         滑动鼠标滑轮事件
    QTabletEvent,
    QKeyEvent,  #           键盘事件
    QFocusEvent,  #         焦点事件
    QPaintEvent,  #         绘画事件
    QMoveEvent,  #          移动事件
    QResizeEvent,  #        窗口尺寸大小改变事件
    QCloseEvent,  #         关闭事件
    QShowEvent,  #          显示事件
    QHideEvent,  #          隐藏事件
    QContextMenuEvent,  #   上下文菜单事件（右键菜单事件）
    QDropEvent,  #          拖放动作
    QDragLeaveEvent,  #     拖拽的离开事件
    QChildEvent,  #         当一个子窗口被添加或者移除时候被送入QObject的
    QCustomEvent,  #        用户自定义事件
]


class EventCell:
    """装载单元"""

    widget: QWidget
    event: EVENT_TYPE

    def __init__(self, widget: QWidget, event: EVENT_TYPE): ...

    def __hash__(self):
        return id(self.__class__.__name__)

    def __call__(self) -> Optional[bool]:
        return None
