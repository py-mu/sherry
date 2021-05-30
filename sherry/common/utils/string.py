# encoding=utf-8
"""
    create by pymu
    on 2021/5/30
    at 16:25
"""
import json
import os
import re
from typing import List

REGEX_DEFINED = re.compile("DEFINED_VALUE{(.*?)}", re.S)
REGEX_URL = re.compile("url\((.*?)\)", re.S)


def json_str_to_dict(json_data) -> dict:
    """
    json转dict
    json to dict
    """
    return json.loads(json_data)


def format_style_file(text: str, root: str) -> str:
    """对样式表进行变量替换"""
    values: List[str] = re.findall(REGEX_DEFINED, text)
    text = re.sub(REGEX_DEFINED, "", text)
    if values:
        for i in values[0].split("\n"):
            if i:
                i = i.strip().replace("\t", "").replace(";", "").split(":")
                if len(i) > 1:
                    if 'url' in i[1]:
                        i[1] = get_abs_image_path(i[1], root)
                    text = text.replace(f"var({i[0]})", i[1])
    return text


def get_abs_image_path(path: str, root: str) -> str:
    """当用户项目目录下不存在资源文件时使用eq的内部资源"""
    values: List[str] = re.findall(REGEX_URL, path)
    root = root.replace("\\", "/")
    if values:
        _path = values[0]
        if not os.path.exists(_path):
            _path = root[2:-8] + _path[2:]
            if os.path.exists(_path):
                path = path.replace(values[0], _path)
    return path
