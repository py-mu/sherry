from re import Pattern
from typing import AnyStr, Dict

REGEX_DEFINED: Pattern[AnyStr]
REGEX_URL: Pattern[AnyStr]
REGEX_VAL: Pattern[AnyStr]
val_dict = Dict[str, str]


def json_str_to_dict(json_data: str) -> dict: ...


def format_style_file(text: str, root: str) -> str: ...


def get_mapping_css_value(name: str, value: str): ...


def get_abs_image_path(path: str, root: str) -> str: ...
