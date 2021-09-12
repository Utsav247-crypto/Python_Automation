from BaseClass.BaseClass import Baseclass
from selenium import webdriver
import pytest
from Pages.LoginPage import Login
import time
from selenium import webdriver
import time

driver = Baseclass.invoke_browser
class TestLogin1(Baseclass):
    @pytest.mark.sanity
    def test_username1(self):
        log = self.getLogger()
        driver = self.driver
        time.sleep(2)
        driver.refresh()
        time.sleep(2)