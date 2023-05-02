"""
Sample Tests
"""
from rest_framework import APICLient
from django.test import SimpleTestCase
from . import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Testing adding numbers together"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)
    
    def test_subtract_numbers(self):
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)