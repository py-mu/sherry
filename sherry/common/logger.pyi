import logging
from types import TracebackType
from typing import Any, Union, Optional, Dict


class ApplicationLogger(logging.Logger):
    root_path: str
    app_name: str

    def set_handler(self, name: str): ...

    def error(self, msg: Any, *args: Any, exc_info: Union[None, bool, TracebackType, BaseException] = ...,
              stack_info: bool = ..., level: int = ..., extra: Optional[Dict[str, Any]] = ...,
              **kwargs: Any) -> None: ...
