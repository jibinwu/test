import pytest
@pytest.mark.skip
def test_one():
    print('this is one')
def test_two():
    print('this is two')
@pytest.mark.xfail
def test_three():
    print('this is three')