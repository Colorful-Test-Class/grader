import sys
import os

STUDENT_REPO_PATH = os.path.abspath('../calculator-test')

sys.path.insert(0, STUDENT_REPO_PATH)

from assignment import add, div, mul, sub, floordiv

from colorful_test import TestCase, show_message

class TestCalculator(TestCase):
    @show_message(
        success='The add function works as expected',
        fail='''
        The add function failed.
        
        Hints:
        Expected: %s
        Received: %f
        '''
    )
    def test_add_0(self):
        self.assert_equal(add(1, 1), 2)
        self.assert_equal(add(1, 2), 3)
        self.assert_equal(add(15, 37), 52)
        
    @show_message(
        success='The sub function works as expected',
        fail='''
        The sub function failed.
        
        Hints:
        Expected: %s
        Received: %f
        '''
    )
    def test_sub_1(self):
        self.assert_equal(sub(1, 1), 0)
        self.assert_equal(sub(15, 3), 12)
        self.assert_equal(sub(7, 9), -2)
     
    @show_message(
        success='The mul function works as expected',
        fail='''
        The mul function failed.
        
        Hints:
        Expected: %s
        Received: %f
        '''
    )   
    def test_sub_2(self):
        self.assert_equal(mul(1, 1), 1)
        self.assert_equal(mul(14, 0), 0)
        self.assert_equal(mul(3, 9), 27)
        
    @show_message(
        success='The div function works as expected',
        fail='''
        The div function failed.
        
        Hints:
        Expected: %s
        Received: %f
        '''
    )
    def test_div_3(self):
        self.assert_equal(div(1, 1), 1.0)
        self.assert_equal(div(5, 2), 2.5)
        self.assert_equal(div(7, 2), 3.5)
        
    @show_message(
        success='The floordiv function works as expected',
        fail='''
        The floordiv function failed.
        
        Hints:
        Expected: %s
        Received: %f
        '''
    )
    def test_floordiv_4(self):
        self.assert_equal(floordiv(1, 1), 1)
        self.assert_equal(floordiv(5, 2), 2)
        self.assert_equal(floordiv(7, 2), 3)
        

if __name__ == '__main__':
    TestCalculator.run_and_output_results(fail_fast=False)