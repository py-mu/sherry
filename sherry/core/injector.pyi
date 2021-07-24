# coding=utf-8
"""
    create by pymu
    on 2021/6/14
    at 2:43
"""
from typing import Tuple

__all__ = ('CursorAgent', 'PropertyAgent', 'BaseAgent')


class BaseAgent:
    __agent__: Tuple[str, ...]


class CursorAgent(BaseAgent):
    ...


class PropertyAgent(BaseAgent):
    ...
