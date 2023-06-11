import pytest

from indi_dummy.math_code import add_two_numbers, sub_two_numbers, mul_two_numbers

@pytest.mark.parametrize("a,b,c", [(1,1,2),(2,2,4)])
def test_add_two_numbers(a, b, c):
    assert add_two_numbers(a,b) == c

@pytest.mark.parametrize("a,b,c", [(1,1,0),(2,2,0)])
def test_sub_two_numbers(a, b, c):
    assert sub_two_numbers(a,b) == c

@pytest.mark.parametrize("a,b,c", [(1,1,1),(2,2,4)])
def test_mul_two_numbers(a, b, c):
    assert mul_two_numbers(a,b) == c