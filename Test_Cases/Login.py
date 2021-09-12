from selenium import webdriver
from Pages.LoginPage import Login

class LoginTest():
    def setup(self):
        self.driver = webdriver.Chrome('D:/Python Automation/Drivers/Chrome/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        driver=self.driver
        login = Login(driver)
        login.enter_username("utsav.roy@forcepoint.com")
        login.enter_password("Admin#123")
        login.click_login()
