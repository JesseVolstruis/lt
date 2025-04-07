#!/usr/bin/env python3
import sys
import os
import unittest
from io import StringIO  # using this to emulate the test data with a string
from getbest_code import getbest

class TestClass(unittest.TestCase):

    def test_Top(self): #tests whether top is functioning
        f = StringIO("""Course,Student Number,Mark,Comment 
ELEN3020,160001,72,OK
ELEN3020,167381,90,Check
ELEN3020,143211,83,-
ELEN3020,17171,48,Redo
ELEN3020,191919,73,-""") #bestDat0.csv as string used with String.IO to parse it to getCols

        col_num, mark_num = getbest.getCols(f) #gets the id index and mark index from getCols
        idx, best = getbest.findTop(f,col_num,mark_num) #gets the id and mark of the top student
        self.assertEqual(idx, 167381)
        self.assertEqual(best, 90)


if __name__ == '__main__':
    unittest.main()
