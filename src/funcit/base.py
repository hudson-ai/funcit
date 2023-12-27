from .schema import Function
from .util import instantiate

__all__ = ['FuncSpec']

class FuncSpec:
    def __init__(self, func: Function) -> None:
        self.func = func

    def implement(self, func: str | Function) -> Function:
        if isinstance(func, str):
            func = instantiate(func)
        exec(f"{self.func.__name__} = func")
        return func
