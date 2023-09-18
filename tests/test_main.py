import pytest

from indi_dummy.main import depart, greet, some_random_method,some_random_method2,some_random_method3


@pytest.mark.parametrize("name", ["a", "b"])
def test_greet(name):
    assert greet(name) is None

@pytest.mark.parametrize("name", ["a", "b"])
def test_depart(name):
    assert depart(name) is None


@pytest.mark.parametrize("method", [some_random_method, some_random_method2, some_random_method3])
@pytest.mark.parametrize("name", ["a", "b"])
def test_random_methods(method, name):
    assert method(name) == name
