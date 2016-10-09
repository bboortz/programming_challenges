
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

    def test_input_wisdowm(self):
        input1 = "wisdom"
        input2= "mid sow"
        result = detect_anagram(input1, input2)
        assert_equal(result, True)

    def test_input_Seth_Rogan(self):
        input1 = "Seth Rogan"
        input2= "Gathers No"
        result = detect_anagram(input1, input2)
        assert_equal(result, True)

    def test_input_Reddit(self):
        input1 = "Reddit"
        input2= "Eat Dirt"
        result = detect_anagram(input1, input2)
        assert_equal(result, False)

    def test_input_Schoolmaster(self):
        input1 = "Schoolmaster"
        input2= "The classroom"
        result = detect_anagram(input1, input2)
        assert_equal(result, True)

    def test_input_Astronomers(self):
        input1 = "Astronomers"
        input2= "Moon starer"
        result = detect_anagram(input1, input2)
        assert_equal(result, False)

    def test_input_Vacation_Times(self):
        input1 = "Vacation Times"
        input2= "I'm Not as Active"
        result = detect_anagram(input1, input2)
        assert_equal(result, True)

    def test_input_Dormitory(self):
        input1 = "Dormitory"
        input2= "Dirty Rooms"
        result = detect_anagram(input1, input2)
        assert_equal(result, False)

