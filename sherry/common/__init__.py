# coding=utf-8
"""
    create by pymu
    on 2021/4/30
    at 17:11
"""
import logging

import colorlog

from sherry.common.logger import ApplicationLogger

ch = logging.StreamHandler()
console_formatter = colorlog.ColoredFormatter(
    fmt='%(log_color)s%(asctime)s.%(msecs)03d %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s',
    datefmt='%Y-%m-%d  %H:%M:%S',
)
ch.setFormatter(console_formatter)
logging.root.setLevel(logging.DEBUG)
logging.root.addHandler(ch)
