
import os, sys, inspect
from app import *

from nose.tools import assert_equal
from nose.tools import assert_not_equal



class TestApp(object):

    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""

    def setUp(self):
        """This method is run once before _each_ test method is executed"""

    def teardown(self):
        """This method is run once after _each_ test method is executed"""

    def test_input_0(self):
        input = 0
        result = reverse_factorial(input)
        assert_equal(result, None)

    def test_input_120(self):
        input =120 
        result = reverse_factorial(input)
        assert_equal(result, 5)

    def test_input_150(self):
        input =150 
        result = reverse_factorial(input)
        assert_equal(result, None)

    def test_input_6(self):
        input = 6 
        result = reverse_factorial(input)
        assert_equal(result, 3)

    def test_input_18(self):
        input = 18 
        result = reverse_factorial(input)
        assert_equal(result, None)

    def test_input_3628800(self):
        input = 3628800 
        result = reverse_factorial(input)
        assert_equal(result, 10)


