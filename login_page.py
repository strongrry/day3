from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    LOGIN_BTN = (By.CSS_SELECTOR, "[data-testid='login-btn']")
    def login_button(self):
        return self.driver.find_element(*self.LOGIN_BTN)