# coding=utf-8
"""
    create by pymu
    on 2021/7/14
    at 20:12
"""
import logging

from sherry.variable import import_lib_after


def retouch():
    for lib in import_lib_after:
        try:
            __import__(lib)
        except ImportError:
            logging.exception("can't import module '{}'. ".format(lib))
