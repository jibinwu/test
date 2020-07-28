import pytest

def test_multiple_assert():
    pytest.assume(3==3)
    pytest.assume(1==2)
    pytest.assume(3==4)

