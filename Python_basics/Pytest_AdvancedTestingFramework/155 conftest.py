'''
Created on May 30, 2018
@author: venkateshwara.d
'''
import pytest

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print("Running conftest demo one time setUp")
    yield
    print("Running conftest demo one time tearDown")
