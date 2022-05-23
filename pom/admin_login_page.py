from selenium.webdriver.common.by import By
from frame.base_page import BasePage
from frame.base_locator import BaseLocator, Selector


class AdminLoginPageLocators(BaseLocator):

    URL = '/admin'

    URL_ADMIN_LOGIN_PAGE = URL

    TITLE_ADMIN_LOGIN_PAGE = "Administration"
    TITLE_ADMIN_PAGE = "Dashboard"
    TITLE_FORGOTTEN_PASSWORD_PAGE = "Forgot Your Password?"

    LOCATOR_INPUT_USERNAME = Selector(By.CSS_SELECTOR, "#input-username")
    LOCATOR_INPUT_PASSWORD = Selector(By.CSS_SELECTOR, "#input-password")
    LOCATOR_INPUT_EMAIL = Selector(By.CSS_SELECTOR, "#input-email")

    LOCATOR_BUTTON_LOGIN_SUBMIT = Selector(By.CSS_SELECTOR, "button.btn.btn-primary")
    LOCATOR_BUTTON_FORGOTTEN_PASSWORD_CANCEL = Selector(
        By.CSS_SELECTOR, "a.btn.btn-default")
    LOCATOR_BUTTON_FORGOTTEN_PASSWORD_SUBMIT = Selector(
        By.CSS_SELECTOR, "button.btn.btn-primary")
    LOCATOR_BUTTON_ALERT_CLOSE = Selector(By.CSS_SELECTOR, "button.close")

    LOCATOR_LINK_FORGOTTEN_PASSWORD = Selector(By.LINK_TEXT, "Forgotten Password")

    LOCATOR_ALERT_DANGER_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    LOCATOR_ALERT_SUCCESS_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")


class AdminLoginPage(BasePage):

    locator = AdminLoginPageLocators

    def enter_login(self, login):
        self.find_element(self.locator.LOCATOR_INPUT_USERNAME).send_keys(login)

    def enter_password(self, password):
        self.find_element(
            self.locator.LOCATOR_INPUT_PASSWORD).send_keys(password)

    def enter_email(self, email):
        self.find_element(self.locator.LOCATOR_INPUT_EMAIL).send_keys(email)

    def click_on_login_button(self):
        self.find_element(self.locator.LOCATOR_BUTTON_LOGIN_SUBMIT).click()

    def click_on_forgotten_password_link(self):
        self.find_element(self.locator.LOCATOR_LINK_FORGOTTEN_PASSWORD).click()

    def click_on_close_alert_button(self):
        return self.find_element(self.locator.LOCATOR_BUTTON_ALERT_CLOSE).click()

    def click_on_forgotten_password_cancel_button(self):
        self.find_element(
            self.locator.LOCATOR_BUTTON_FORGOTTEN_PASSWORD_CANCEL).click()

    def click_on_forgotten_password_reset_button(self):
        self.find_element(
            self.locator.LOCATOR_BUTTON_FORGOTTEN_PASSWORD_SUBMIT).click()


if __name__ == '__main__':

    print(AdminLoginPage.locator.locators)
