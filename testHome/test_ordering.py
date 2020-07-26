import pytest
a=0
@pytest.mark.run(order=2)
def test_02():
    assert a == 10
@pytest.mark.run(order=1)
def test_01():
    global a
    a = 10
    assert a == 10
