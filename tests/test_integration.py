import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from calculator import Calculator

calc = Calculator()

def test_full_calculation():
    result = calc.add(5, 3)
    assert result == 8

def test_clear_function():
    calc.add(10, 5)
    result = calc.clear()
    assert result == 0
