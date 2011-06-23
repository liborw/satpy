# 
#  satio.py: SAT Input Output
#  satpy
#  
#  This module contain input and output tools for sat problems.
#
#  References:
#   [1] http://www.satcompetition.org/2004/format-solvers2004.html

import os
import cnf

# Constants
SATISFIABLE = 10
UNSATISFIABLE = 20
UNKNOWN = 0
SATTIMEOUT = "SATTIMEOUT"
SATRAM = "SATRAM"

def print_comment(msg, args):
    """Prints comment in format specified in [1]."""
    print "c ", msg % args

def print_values(values):
    """Prints values in format specitied in [1]. """
    print "v ", " ".join(values)

def print_solution(solution):
    """Prints one of the SATISFABLE, UNSATISFABLE and UNKNOWN the input
    is constant with the same name."""
    print { SATISFIABLE: "SATISFIABLE",
            UNSATISFIABLE: "UNSATISFIABLE",
            UNKNOWN: "UNKNOWN"}[solution]

def get_time_limit():
    """"
    Returns time limit in seconds for current problem,
    None if no specified.
    """"
    if SATTIMEOUT in os.environ.keys:
        return os.environ[SATTIMEOUT]
    else:
        return None

def get_ram_limit():
    """
    Returns memory limit in Mb for current problem,
    None if not specified.
    """
    if SATRAM in os.environ.keys:
        return os.environ[SATRAM]
    else:
        return None
