from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminCommonElementsLocators(BaseLocator):

    LOCATOR_LOGO = Selector(By.CSS_SELECTOR, "#header-logo")
    LOCATOR_LOGOUT = Selector(
        By.CSS_SELECTOR, '#header > div > ul > li:nth-child(2) > a')


class AdminCommonElements(BasePage):

    locator = AdminCommonElementsLocators

    def click_logo(self):
        self.click(self.locator.LOCATOR_LOGO)

    def click_logout(self):
        self.click(self.locator.LOCATOR_LOGOUT)
