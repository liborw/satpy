# 
#  test_cnf.py: Tests for cnf.py
#  satpy
#  

import unittest
from satpy.cnf import Clause
from BitVector import BitVector

class CNFTestCase(unittest.TestCase):

    def test_empty_clause_len(self):
        clause = Clause()
        self.assertEqual(len(clause), 0)

    def test_clause_len(self):
        clause = Clause(255, 255)
        self.assertEqual(len(clause), 16)

    def test_tantology(self):
        clause = Clause(1, 1)
        self.assertTrue(clause.tantology())

    def test_not_tantology(self):
        clause = Clause(1, 2)
        self.assertFalse(clause.tantology())

    def test_unit_clause(self):
        clause = Clause(2, 0)
        self.assertTrue(clause.unit())

    def test_not_unit_clause(self):
        clause = Clause(4, 1)
        self.assertFalse(clause.unit())

    def test_empty(self):
        clause = Clause()
        self.assertTrue(clause.empty())

def get_suite():
    return unittest.TestLoader().loadTestsFromTestCase(CNFTestCase)