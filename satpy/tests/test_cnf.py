# 
#  test_cnf.py: Tests for cnf.py
#  satpy
#  

import unittest
from satpy.cnf import count_ones

class CNFTestCase(unittest.TestCase):

    def test_count_ones(self):
        self.assertEqual(count_ones(0), 0)
        self.assertEqual(count_ones(1), 1)
        self.assertEqual(count_ones(2), 1)
        self.assertEqual(count_ones(3), 2)
        self.assertEqual(count_ones(4), 1)
        self.assertEqual(count_ones(255), 8)


def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(CNFTestCase)