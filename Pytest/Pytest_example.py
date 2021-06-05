import pytest


def test_add():
    assert (2+2) == (1+3)


def test_raise():
    with pytest.raises(TypeError) as e:
        print(e)
    assert test_add()