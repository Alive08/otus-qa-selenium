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

    LOCATOR_BUTTON_LOGIN_SUBMIT = Selector(
        By.CSS_SELECTOR, "button.btn.btn-primary")
    LOCATOR_BUTTON_FORGOTTEN_PASSWORD_CANCEL = Selector(
        By.CSS_SELECTOR, "a.btn.btn-default")
    LOCATOR_BUTTON_FORGOTTEN_PASSWORD_SUBMIT = Selector(
        By.CSS_SELECTOR, "button.btn.btn-primary")
    LOCATOR_BUTTON_ALERT_CLOSE = Selector(By.CSS_SELECTOR, "button.close")

    LOCATOR_LINK_FORGOTTEN_PASSWORD = Selector(
        By.LINK_TEXT, "Forgotten Password")

    LOCATOR_ALERT_DANGER_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    LOCATOR_ALERT_SUCCESS_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")


class AdminLoginPage(BasePage):

    locator = AdminLoginPageLocators

    def enter_login(self, login):
        inp = self.find_element(self.locator.LOCATOR_INPUT_USERNAME)
        inp.clear()
        inp.click()
        inp.send_keys(login)

    def enter_password(self, password):
        inp = self.find_element(
            self.locator.LOCATOR_INPUT_PASSWORD)
        inp.clear()
        inp.click()
        inp.send_keys(password)

    def enter_email(self, email):
        inp = self.find_element(self.locator.LOCATOR_INPUT_EMAIL)
        inp.clear()
        inp.click()
        inp.send_keys(email)

    def click_login_button(self):
        self.find_element(self.locator.LOCATOR_BUTTON_LOGIN_SUBMIT).click()

    def admin_login_with(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()

    def click_forgotten_password_link(self):
        self.find_element(self.locator.LOCATOR_LINK_FORGOTTEN_PASSWORD).click()

    def close_alert(self):
        self.find_element(self.locator.LOCATOR_BUTTON_ALERT_CLOSE).click()

    def click_forgotten_password_cancel_button(self):
        self.find_element(
            self.locator.LOCATOR_BUTTON_FORGOTTEN_PASSWORD_CANCEL).click()

    def click_forgotten_password_reset_button(self):
        self.find_element(
            self.locator.LOCATOR_BUTTON_FORGOTTEN_PASSWORD_SUBMIT).click()

    def does_present_alert_danger(self):
        return self.does_present(self.locator.LOCATOR_ALERT_DANGER_MESSAGE)

    def does_not_present_alert_danger(self):
        return self.does_not_present(self.locator.LOCATOR_ALERT_DANGER_MESSAGE)

    def does_present_alert_success(self):
        return self.does_present(self.locator.LOCATOR_ALERT_SUCCESS_MESSAGE)

    def does_not_present_alert_success(self):
        return self.does_not_present(self.locator.LOCATOR_ALERT_SUCCESS_MESSAGE)


if __name__ == '__main__':

    print(AdminLoginPage.locator.locators)
