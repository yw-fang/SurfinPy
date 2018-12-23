import numpy as np
import numpy.testing as npt
import sys 
from surfinpy import phaseplot as pp
import unittest
from numpy.testing import assert_almost_equal, assert_equal

class TestPhaseplot(unittest.TestCase):

    def test_get_levels(self):
        X = np.arange(5)
        levels = pp.get_levels(X)
        expected = np.array([-1, 0, 1, 2, 3, 4])
        assert np.array_equal(levels, expected)

    def test_get_ticks(self):
        X = np.arange(5)
        tick = pp.get_ticks(X)
        expected = [-0.5, 0.5, 1.5, 2.5, 3.5]
        assert tick == expected

#https://matplotlib.org/devel/testing.html