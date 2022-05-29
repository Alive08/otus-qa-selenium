from selenium.webdriver.common.by import By
from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage

class AccountPageLocators(BaseLocator):

    TITLE = 'My Account'
    LOCATOR_BUTTON_CONTINUE = Selector(By.CSS_SELECTOR, '#content > div > div > a')


class AccountPage(BasePage):

    locator = AccountPageLocators

    def click_continue(self):
        self.click(self.locator.LOCATOR_BUTTON_CONTINUE)
