import pytest
from selenium import webdriver
import time
from BaseClass.BaseClass import Baseclass

@pytest.fixture(scope="class")
def setup(request):
    invoke = Baseclass()
    driver = invoke.invoke_browser()
    driver.get("https://www.instagram.com")
    request.cls.driver = driver


    yield
    driver.close()
