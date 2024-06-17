import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    print("Opening browser")
    mydriver = webdriver.Chrome()
    yield mydriver
    print("Closing driver")
    mydriver.close()