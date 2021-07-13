from typing import List, Callable, Union, Dict, Type, Tuple, Optional

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication

app_name: str
author: str
app_version: str or float
app: Union[QApplication, QCoreApplication]
TaskDispatcher: Dict[str, Tuple[Optional[Callable, Type, object], Tuple, Dict]]
DEBUG: bool
import_lib: List[str]
