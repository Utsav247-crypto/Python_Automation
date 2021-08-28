from Locators.Locators import Locators

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.login_username = Locators.login_username_id
        self.login_password = Locators.login_password_id
        self.login_click = Locators.login_click_classname

    def enter_username(self, username):
        self.driver.find_element_by_id(self.login_username).clear()
        self.driver.find_element_by_id(self.login_username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.login_password).clear()
        self.driver.find_element_by_id(self.login_password).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_class_name(self.login_click).click()
