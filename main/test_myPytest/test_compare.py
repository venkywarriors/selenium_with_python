'''
Created on 05-Jul-2020

@author: venkateshwara D
'''
import pytest


@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.others
def test_less():
    num = 100
    assert num < 200
