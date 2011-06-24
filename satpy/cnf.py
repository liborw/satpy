# 
#  cnf.py: Conjuctive normal form representation.
#  satpy
#  

from operator import rshift

class Clause(object):
    """Clause is set of positive and negative literals.
    
    Clause is represented by two bit vectors one for positive literals and
    one for negative.
    """

    def __init__(self, positive=0, negative=0):
        super(Clause, self).__init__()
        self.positive = positive
        self.negative = negative
        self.len = parity(self.positive) + parity(self.negative)

    def __len__(self):
        """Number of literals."""
        return self.len

    def tantology(self):
        """Check whether this clause is tantology.
        
        Clause is tantology if contatins positive and negative literal of 
        the same variable.
        """
        return not (self.positive & self.negative) == 0

    def unit(self):
        """Checks wheter this clause is unit clause.
        
        Unit clause is clause wit only one literal.
        """
        return self.len == 1

    def empty(self):
        """Checks if this clause is empty clasuse."""
        return self.len == 0


def parity(num):
    """Get parity of a binary encoded number."""
    p = 0
    while not num == 0:
        p = p + (num & 1L)
        num = rshift(num, 1)
    return p