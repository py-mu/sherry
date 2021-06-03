from re import Pattern
from typing import AnyStr

REGEX_DEFINED:  Pattern[AnyStr]
REGEX_URL:  Pattern[AnyStr]

def json_str_to_dict(json_data: str) -> dict: ...

def format_style_file(text: str, root: str) -> str: ...

def get_abs_image_path(path: str, root: str) -> str: ...