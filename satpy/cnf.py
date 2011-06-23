# 
#  cnf.py: Conjuctive normal form representation.
#  satpy
#  

class Clause(object):
    """
    Clause representation by two binary numbers, one for positive 
    and second for negative literals.
    """

    def __init__(self, positive=0, negative=0):
        super(Clause, self).__init__()
        self.positive = positive
        self.negative = negative
        self.no_positive = count_ones(self.positive)
        self.no_negative = count_ones(self.negative)
        self.no_literals = self.no_positive + self.no_negative

    def __repr__(self):
        bin_positive = bin(self.positive)
        bin_negative = bin(self.negative)
        return "Clause(p"+bin_positive[2:]+", n"+bin_negative[2:]+")"


def count_ones(num):
    """Count ones in binary encoded number."""
    binary = bin(num)
    return binary.count('1')
    