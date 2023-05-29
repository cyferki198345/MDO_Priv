import pytest

from methods import sub, mult, div, mean

def testSub():
    assert sub(8,4) == 4
    assert sub(7,10) == -3
    assert sub(0,0) == 0

def testMult():
    assert mult(2,2) == 4
    assert mult(4,5) == 20
    assert mult(9,0) == 0

def testDiv():
    assert div(6,2) == 3.0
    assert div(5,2) == 2.5
    with pytest.raises(ValueError):
        div(5,0)

def testMean():
    assert mean([1,2,3]) == 2
    assert mean([0,0,0]) == 0
    assert mean([2,6,10,16]) == 8.5 