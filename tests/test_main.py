import pytest

from indi_dummy.main import depart, greet


@pytest.mark.parametrize("name", ["a", "b"])
def test_greet(name):
    assert greet(name) is None

@pytest.mark.parametrize("name", ["a", "b"])
def test_depart(name):
    assert depart(name) is None
