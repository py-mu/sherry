from typing import List, Callable, Dict, Type, Tuple, Union

from PyQt5.QtWidgets import QStyle

app_name: str
author: str
app_version: str or float
log_file: str
base_qss: str
base_style: QStyle
TaskDispatcher: Dict[str, Union[
    Tuple[Union[Callable, Type, object], Tuple, Dict],
    Tuple[Union[Callable, Type, object], Tuple],
    Tuple[Union[Callable, Type, object], Dict],
    Union[Callable, Type, object],]
]
DEBUG: bool
import_lib_before: List[str]
import_lib_after: List[str]
