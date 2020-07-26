import random
import pytest

def add(x,y):
    return x+y
# @pytest.mark.parametrize('x,y,z',[(1,2,3),(2,3,7),(3,3,6)])
@pytest.mark.parametrize('x',[(1),(2),(3)])
def test_add(x):
    assert x == random.randrange(1,7)
    # assert add(2,3)==6
