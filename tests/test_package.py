import pytest

def test_package():

    with pytest.raises(Exception):
        1/0

    assert 42
