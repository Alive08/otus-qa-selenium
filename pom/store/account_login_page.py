from selenium.webdriver.common.by import By
from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage

class AccountLoginPageLocators(BaseLocator):

    LOCATOR_BUTTON_CONTINUE = Selector(By.CSS_SELECTOR, '#content > div > div > a')
    LOCATOR_INPUT_EMAIL = Selector(By.ID, 'input-email')
    LOCATOR_INPUT_PASSWORD = Selector(By.ID, 'input-password')
    LOCATOR_BUTTON_LOGIN = Selector(By.CSS_SELECTOR, 'input[type=submit]')


class AccountLoginPage(BasePage):

    locator = AccountLoginPageLocators

    def enter_email(self, email):
        self.enter_text(self.locator.LOCATOR_INPUT_EMAIL, email)

    def enter_password(self, password):
        self.enter_text(self.locator.LOCATOR_INPUT_PASSWORD, password)

    def click_login(self):
        self.click(self.locator.LOCATOR_BUTTON_LOGIN)
    
    def login_with(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
    