from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By
from pom.shared.store_breadcrumb import StoreBreadcrumb
from pom.shared.store_menu_account import StoreMenuAccount


class RegisterAccountPageLocators(BaseLocator):

    URL = "index.php?route=account/register"
    URL_REGISTER_ACCOUNT = URL
    TITLE_REGISTER_ACCOUNT = "Register Account"

    LOCATOR_LINK_LOGIN = Selector(By.CSS_SELECTOR, "#content > p > a")
    LOCATOR_LINK_PRIVACY_POLICY = Selector(By.CSS_SELECTOR, "#content > form > div > div > a")
    LOCATOR_INPUT_FIRST_NAME = Selector(By.CSS_SELECTOR, "#input-firstname")
    LOCATOR_INPUT_LAST_NAME = Selector(By.CSS_SELECTOR, "#input-lastname")
    LOCATOR_INPUT_EMAIL = Selector(By.CSS_SELECTOR, "#input-email")
    LOCATOR_INPUT_TELEPHONE = Selector(By.CSS_SELECTOR, "#input-telephone")
    LOCATOR_INPUT_PASSWORD = Selector(By.CSS_SELECTOR, "#input-password")
    LOCATOR_INPUT_PASSWORD_CONFIRM = Selector(
        By.CSS_SELECTOR, "#input-confirm")

    TEXT_PASSWORDS_MISMATCH = "Password confirmation does not match password!"
    TEXT_FIRST_NAME_ERROR = "First Name must be between 1 and 32 characters!"
    TEXT_LAST_NAME_ERROR = "Last Name must be between 1 and 32 characters!"
    TEXT_EMAIL_ERROR = "E-Mail Address does not appear to be valid!"
    TEXT_TELEPHONE_ERROR = "Telephone must be between 3 and 32 characters!"
    TEXT_PASSWORD_ERROR = "Password must be between 4 and 20 characters!"

    LOCATOR_CHECKBOX_AGREE = Selector(By.CSS_SELECTOR, "input[type=checkbox]")
    LOCATOR_BUTTON_CONTINUE = Selector(
        By.CSS_SELECTOR, ".btn.btn-primary")
    LOCATOR_ALERT_DANGER = Selector(
        By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    LOCATOR_BUTTON_CLOSE_PRIVACY_POLICY = Selector(By.CSS_SELECTOR, "button.close")


class RegisterAccountPage(BasePage):

    locator = RegisterAccountPageLocators

    def enter_first_name(self, fname):
        self.input_enter_text(self.locator.LOCATOR_INPUT_FIRST_NAME, fname)

    def enter_last_name(self, lname):
        self.input_enter_text(self.locator.LOCATOR_INPUT_LAST_NAME, lname)

    def enter_email(self, email):
        self.input_enter_text(self.locator.LOCATOR_INPUT_EMAIL, email)

    def enter_telephone(self, telephone):
        self.input_enter_text(self.locator.LOCATOR_INPUT_TELEPHONE, telephone)

    def enter_password(self, password):
        self.input_enter_text(self.locator.LOCATOR_INPUT_PASSWORD, password)

    def enter_password_confirm(self, password):
        self.input_enter_text(
            self.locator.LOCATOR_INPUT_PASSWORD_CONFIRM, password)

    def is_checked_agree(self):
        return self.find_element(self.locator.LOCATOR_CHECKBOX_AGREE).get_attribute('checked')

    def check_box_agree(self):
        if not self.is_checked_agree():
            self.find_element(self.locator.LOCATOR_CHECKBOX_AGREE).click()

    def uncheck_box_agree(self):
        if self.is_checked_agree():
            self.find_element(self.locator.LOCATOR_CHECKBOX_AGREE).click()

    def click_button_continue(self):
        self.find_element(self.locator.LOCATOR_BUTTON_CONTINUE).click()
    
    def click_privacy_policy(self):
        self.find_element(self.locator.LOCATOR_LINK_PRIVACY_POLICY).click()
    
    def close_privacy_policy(self):
        self.find_element(self.locator.LOCATOR_BUTTON_CLOSE_PRIVACY_POLICY).click()

    def submit_form(self, data, agree=True):
        self.enter_first_name(data.fname)
        self.enter_last_name(data.lname)
        self.enter_email(data.email)
        self.enter_telephone(data.phone)
        self.enter_password(data.password_1)
        self.enter_password_confirm(data.password_2)
        if agree:
            self.check_box_agree()
        self.click_button_continue()


if __name__ == '__main__':

    print(RegisterAccountPage.locator.locators)
