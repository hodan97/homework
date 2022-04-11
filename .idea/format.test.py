# say you have a function like this

#def area(a)
#    return(a*a)
# area(5)
#
# import unittest
# from file name containing area function import *

# class TestArea(unittest.TestCase): ### class needs defining for all defined tests to go under
#     def test_area(self):  ### each test needs defining
#         self.assertEqual(area(5) 25)  ### add assertion here theres many to choose from
#### this shows that when you run the function area and you give a value of 5 it should return 25 and the test is checking
#### that when area function runs we want to see value 5 and output 5 when function run
#### if we see this the test passed if not something wrong, like syntax error or bug or software issue or input error or
#### something is missing, mistake, misspelled
#  it then needs  # if __name__ == '__main__':
#                       unittest.main()
# then test should run

#SECOND EXAMPLE OF UNIT TEST THIS TIME USING STRING FUNCTION
# import unittest
# from file containing function you want to test
# class TestStringMethods(unittest, Testcase):
# def string_case(self):
#      self.assertEqual(codefirstgirls.upper(), CODEFIRSTGIRLS)
#      self.assertEqual(codefirstgirls.upper() == CODEFIRSTGIRLS) # same as above another way to do it
# def string_is_upper(self): ##### this is checking if something is true or false
#      self.assertTrue('CODEFIRSTGIRLS.isupper())
#      self.assertFalse('CodeFIRSTgirls.isupper())  # for true or false only one parameter needed
# unittest.main()
# this is checking the string in '' if it is.upper true the test ran fine and if false and it's assert false then fine

###########
# def test_pin_code_correct(self):
#     self.assertTrue(homework4.pin_checker(pin_code="0000"))
#
#
# def test_pin_code_incorrect(self):
#     self.assertFalse(homework4.pin_checker(pin_code="0000"))
# CODE ABOVE WOULD HAVE WORKED TO TEST PIN CODE FOR ATM - always separate functions to easily test them
# THIS WORKS BY TAKING FILE NAME THEN . FUNCTION THEN ENTERING WHAT YOU WANNA TEST IS TRUE OR FALSE- done easier!