import pytest
from selenium import webdriver
import time
from BaseClass.BaseClass import Baseclass
from Pages.LoginPage import Login

@pytest.fixture(scope="class")
def setup(request):
    invoke = Baseclass()
    driver = invoke.invoke_browser()
    #login = Login(driver)
    #login.enter_username("utsav.roy@forcepoint.com")
    request.cls.driver = driver

    yield
    driver.close()