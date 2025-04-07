#!/usr/bin/env python3
import sys
import os
import unittest
from io import StringIO
from getbest_code import getbest

class TestClass(unittest.TestCase):

    def test_cols(self): #tests whether the number and mark column indexs are correct
        f = StringIO("""Course,Student Number,Mark,Comment
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-""") #bestDat0.csv as string used with String.IO to parse it to getCols  
        col_num, mark_num = getbest.getCols(f)
        self.assertEqual(col_num, 1)
        self.assertEqual(mark_num, 2)

if __name__ == '__main__':
    unittest.main()
