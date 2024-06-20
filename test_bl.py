import bl
import pytest
import allure

def test_4_is_prime():
    assert bl.is_prime(4) == False

def test_5_is_prime():
    assert bl.is_prime(5) == True

def test_7_is_prime():
    assert bl.is_prime(7) == False