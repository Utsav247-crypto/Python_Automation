from BaseClass.BaseClass import Baseclass
import pytest
from Pages.LoginPage import Login
import time
from selenium import webdriver

driver = Baseclass.invoke_browser

class TestLogin(Baseclass):
    @pytest.mark.sanity
    def test_username(self):
        log = self.getLogger()
        driver = self.driver
        login = Login(driver)
        login.enter_username("utsav.roy@forcepoint.com")
        log.info("Login Username entry pass")

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_password(self):
        log = self.getLogger()
        driver = self.driver
        login = Login(driver)
        login.enter_password("Admin#123")
        log.info("Login Password entry pass")

    @pytest.mark.regression
    def test_login(self):
        log = self.getLogger()
        driver = self.driver
        login = Login(driver)
        login.click_login()
        log.info("Login button click is pass")