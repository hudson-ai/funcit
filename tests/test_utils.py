import pytest
from textwrap import dedent
from funcit.util import (
    compiles, 
    defines_only_funcs, 
    defines_one_func,
)

@pytest.fixture
def funcs():
    return [
        dedent("""
            def foo():
                return 42
        """).strip(),

        dedent("""
            def bar():
                return 69
        """).strip(),        
    ]

def test_compiles(funcs):
    good_code = funcs[0]
    bad_code = f"Here is a function:\n{good_code}"
    assert compiles(good_code)
    assert not compiles(bad_code)

def test_defines_only_funcs(funcs):
    good_code = '\n'.join(funcs)
    assert defines_only_funcs(good_code)
    bad_code = f"x='cake'\n{good_code}"
    assert compiles(bad_code)
    assert not defines_only_funcs(bad_code)

def test_defines_one_func(funcs):
    assert defines_one_func(funcs[0])
    assert not defines_one_func('\n'.join(funcs))