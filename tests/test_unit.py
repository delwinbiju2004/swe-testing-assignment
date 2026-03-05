import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator
import pytest

calc = Calculator()

def test_addition():
    assert calc.add(5,3) == 8

def test_subtraction():
    assert calc.subtract(10,4) == 6

def test_multiplication():
    assert calc.multiply(6,7) == 42

def test_division():
    assert calc.divide(8,2) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calc.divide(5,0)

def test_negative_numbers():
    assert calc.add(-5,3) == -2

def test_decimal_numbers():
    assert calc.divide(5.0,2.0) == 2.5

def test_large_numbers():
    assert calc.multiply(100000,100000) == 10000000000
