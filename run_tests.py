#!/usr/bin/env python
import unittest
from satpy.tests.test_cnf import get_suite as get_cnf_suite

tests = [
    get_cnf_suite()
]

if __name__ == "__main__":
    failures = unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(tests))
    