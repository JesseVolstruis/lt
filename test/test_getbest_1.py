#!/usr/bin/env python3
import sys
import os
import unittest
from io import StringIO  # using this to emulate the test data with a string
from getbest_code import getbest

class TestClass(unittest.TestCase):

    def test_cols(self):
        f = StringIO("""Course,Student Number,Mark,Comment
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-""") 

        col_num, mark_num = getbest.getCols(f)
        self.assertEqual(col_num, 1)
        self.assertEqual(mark_num, 4)

if __name__ == '__main__':
    unittest.main()
