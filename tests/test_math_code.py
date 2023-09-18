import pytest

from indi_dummy.math_code import add_two_numbers, sub_two_numbers, mul_two_numbers, div_two_numbers, new_method, new_method2, pow_two_numbers, sq_number

@pytest.mark.parametrize("a,b,c", [(1,1,2),(2,2,4)])
def test_add_two_numbers(a, b, c):
    assert add_two_numbers(a,b) == c

@pytest.mark.parametrize("a,b,c", [(1,1,0),(2,2,0)])
def test_sub_two_numbers(a, b, c):
    assert sub_two_numbers(a,b) == c

@pytest.mark.parametrize("a,b,c", [(1,1,1),(2,2,4)])
def test_mul_two_numbers(a, b, c):
    assert mul_two_numbers(a,b) == c

@pytest.mark.parametrize("a,b,c", [(1,1,1),(2,2,1)])
def test_div_two_numbers(a, b, c):
    assert div_two_numbers(a,b) == c

@pytest.mark.parametrize("a", [(1,),(2,)])
def test_new_method(a):
    assert new_method(a) == a

@pytest.mark.parametrize("a", [(1,),(2,)])
def test_new_method2(a):
    assert new_method2(a) == a


@pytest.mark.parametrize("a, b, c", [(1,1,1),(2,2,4)])
def test_pow_method(a, b,c):
    assert pow_two_numbers(a, b) == c


@pytest.mark.parametrize("a, b", [(1,1),(2,4)])
def test_sq_num_(a, b):
    assert sq_number(a) == b