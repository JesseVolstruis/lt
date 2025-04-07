#!/usr/bin/env python3
import sys
import os
import unittest
from getbest_code import getbest

class TestClass(unittest.TestCase):

    def test_cols(self): #tests whether the number and mark column indexs are correct
        f = open("test/myData.csv") #imports test data
        col_num, mark_num = getbest.getCols(f) #gets the id index and mark index from getCols
        self.assertEqual(col_num, 1) #checks if id column is index 1
        self.assertEqual(mark_num, 2) #checks if mark column is index 4
        f.close()

if __name__ == '__main__':
    unittest.main()
