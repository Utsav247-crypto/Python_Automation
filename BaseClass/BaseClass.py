import inspect

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Config_Properties.Config_Properties import Config_Properties
import pytest
import logging

@pytest.mark.usefixtures("setup")
class Baseclass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.INFO)
        return logger

    def invoke_browser(self):
        if Config_Properties.browser == "Chrome":
            driver = webdriver.Chrome(executable_path=Config_Properties.chromedriver_path)
            driver.get("https://rbi-safer-tenant.qa.cyberinc.com/login")
            driver.maximize_window()

        elif Config_Properties.browser == "Firefox":
            driver = webdriver.Firefox(executable_path=Config_Properties.geckodriver_path)
            driver.get("https://rbi-safer-tenant.qa.cyberinc.com/login")
            driver.maximize_window()

        else:
            print("Enter valid browser name in config properties")

        return driver

    def refresh_current_page(self, driver_name):
        driver_name.refresh()