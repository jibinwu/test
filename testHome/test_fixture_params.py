import  pytest
@pytest.fixture(params=['jbw','zxy'])
def test_data(request):
    print(request.param)
    return request
def test_one(test_data):
    print(test_data)