from selenium import webdriver
from Pages.LoginPage import Login
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:/Python Automation/Drivers/Chrome/chromedriver.exe')
driver.get("https://rbi-safer-tenant.qa.cyberinc.com/login")

login=Login(driver)
login.enter_username("utsav.roy@forcepoint.com")
login.enter_password("Admin#123")
login.click_login()