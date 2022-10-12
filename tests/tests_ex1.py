# import pytest
# # Use fixtures for data/models manipulation
# @pytest.fixture(scope='session')
# def fixture_1():
#     print('run-fixture-1')
#     return 1


# @pytest.fixture
# def yield_fixture():
#     '''
#     You can tear down a test to check the begining and end of the test 
#     '''
#     print('Start Test Phase')
#     yield 6
#     print('End Test Phase')
# def test_dummy():
#     assert 1

# @pytest.mark.slow
# def test_1is1(fixture_1):
#     assert 1==fixture_1
   
# @pytest.mark.slow
# def test_2is2(fixture_1):
#     assert 2==fixture_1 + fixture_1

    
# def test_example(yield_fixture):
#     print('num-example-1')
#     assert yield_fixture == 6
    
    
    
