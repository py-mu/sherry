from typing import List, Callable, Dict, Type, Tuple, Optional

from PyQt5.QtWidgets import QStyle

app_name: str
author: str
app_version: str or float
log_file: str
base_qss: str
base_style: QStyle
TaskDispatcher: Dict[str, Tuple[Optional[Callable, Type, object], Tuple, Dict]]
DEBUG: bool
import_lib_before: List[str]
import_lib_after: List[str]
