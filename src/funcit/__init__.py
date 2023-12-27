import ast
import inspect
Function = type(lambda: ...)

class FuncSpec:
    def __init__(self, func: Function) -> None:
        self.func = func
        self.tests = []

    def implement(self, func: str | Function) -> Function:
        if isinstance(func, str):
            func = instantiate(func)
        exec(f"{self.func.__name__} = func")
        for test in self.tests:
            test()
        return func

    def test(self, test_func):
        self.tests.append(test_func)

def instantiate(code: str) -> Function:
    assert defines_one_func(code)
    [funcdef] = ast.parse(code).body
    exec(code)
    return locals()[funcdef.name]

def compiles(code: str) -> bool:
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True

def defines_one_func(code: str) -> bool:
    module = ast.parse(code)
    body = module.body
    if len(body) != 1:
        return False
    thing = body[0]
    if not isinstance(thing, ast.FunctionDef):
        return False
    return True


def has_unresolved_references(code: str) -> bool:
    raise NotImplementedError
