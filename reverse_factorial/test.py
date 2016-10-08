
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
        assert_equal(result, 0)
        assert_not_equal(result, -1)
