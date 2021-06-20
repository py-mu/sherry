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

REGEX_DEFINED = re.compile("DEFINED_VALUE *{(.*?)}", re.S)
REGEX_URL = re.compile("url\\((.*?)\\)", re.S)
REGEX_VAL = re.compile("var *\\((.*?)\\)")
val_dict = {}  # Note: qss 变量集合


def json_str_to_dict(json_data):
    """
    json转dict
    json to dict
    """
    return json.loads(json_data)


def format_style_file(text, root):
    """对样式表进行变量替换"""
    css_values = re.findall(REGEX_DEFINED, text)  # type: List[str]
    text = re.sub(REGEX_DEFINED, "", text)
    if not css_values:
        return text
    for css_defined_val in css_values[0].split("\n"):  # Note: css css defined val item.
        if not css_defined_val:
            continue
        css_defined_val = css_defined_val.strip().replace("\t", "")
        css_defined_val = css_defined_val.replace(";", "").split(":")
        if len(css_defined_val) <= 1:
            continue
        name, value = css_defined_val
        if 'url' in value:
            value = get_abs_image_path(value, root)
        val_dict.update({name: value})
        get_mapping_css_value(name, value)
        text = text.replace(f"var({name})", val_dict.get(name))
    return text


def get_mapping_css_value(name, value):
    """获取映射的变量"""
    map_value = REGEX_VAL.findall(value)
    if map_value:
        val_dict.update({name: val_dict.get(map_value[0], "")})
        get_mapping_css_value(name, map_value[0])


def get_abs_image_path(path, root):
    """当用户项目目录下不存在资源文件时使用eq的内部资源"""
    values = re.findall(REGEX_URL, path)  # type: List[str]
    root = root.replace("\\", "/")
    if values:
        _path = values[0]
        if not os.path.exists(_path):
            _path = root[2:-8] + _path[2:]
            if os.path.exists(_path):
                path = path.replace(values[0], _path)
    return path
