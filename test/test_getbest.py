#!/usr/bin/env python3
import sys
import os
import unittest
import getbest

class Test1(unittest.TestCase):

    def test_mark(self):
        self.assertEqual(1,1)

    def test_num(self):
        self.assertEqual(2,3)

if __name__ == '__main__':


    unittest.main()
