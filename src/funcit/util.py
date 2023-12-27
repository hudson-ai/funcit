import ast
from .schema import Function

__all__ = [
    'instantiate',
    'compiles',
    'defines_only_funcs',
    'defines_one_func',
]

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

def defines_only_funcs(code: str) -> bool:
    module = ast.parse(code)
    body = module.body
    for thing in body:
        if not isinstance(thing, ast.FunctionDef):
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
