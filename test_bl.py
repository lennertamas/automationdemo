import bl
import pytest
import allure

@allure.title("Test 4 is not prime ")
@allure.description("This test attempts to test wether 4 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_4_is_prime():
    assert bl.is_prime(4) == False

@allure.title("Test 5 is prime ")
@allure.description("This test attempts to test wether 4 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_5_is_prime():
    assert bl.is_prime(5) == True

@allure.title("Test 7 is prime ")
@allure.description("This test attempts to test wether 4 is prime or not.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_7_is_prime():
    assert bl.is_prime(7) == True