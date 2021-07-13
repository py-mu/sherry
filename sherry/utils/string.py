# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 16:25
"""
import os
import re

REGEX_URL = re.compile("url\\((.*?)\\)", re.S)


def format_style_file(text, root):
    # type: (str, str) -> str
    """对样式表进行变量替换"""
    for path in re.findall(REGEX_URL, text):
        n_path = get_abs_image_path(path, root)
        text = text.replace(path, n_path)
    return text


def get_abs_image_path(path, root):
    """当用户项目目录下不存在资源文件时使用eq的内部资源"""
    root = root.replace("\\", "/")
    if not os.path.exists(path):
        _path = root + path.strip('.')
        if os.path.exists(_path):
            return _path
    return path
