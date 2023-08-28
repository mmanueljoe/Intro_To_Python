import pytest
from unittest import TestCase
from utils.calculator import Calculator


class CalculatorTest(TestCase):
    def test(self):
        pass

    def test_calculator_int(self):
        calculator = calculator(4,5)
        int_datatype = type(calculator)
