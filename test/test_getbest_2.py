#!/usr/bin/env python3
import sys
import os
import unittest
from getbest_code import getbest

class TestClass(unittest.TestCase):

    def test_Top(self): #tests whether top is functioning
        f = open("test/myData.csv") #imports test data 
        col_num, mark_num = getbest.getCols(f) #gets the id index and mark index from getCols
        idx, best = getbest.findTop(f,col_num,mark_num) #gets the id and mark of the top student
        self.assertEqual(idx, 2597626) #checks if student id is correct
        self.assertEqual(best, 95) #checks if top mark is correct
        f.close()


if __name__ == '__main__':
    unittest.main()
