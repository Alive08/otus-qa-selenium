from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class StoreFooterLocators(BaseLocator):

    LOCATOR_FOOTER = Selector(By.CSS_SELECTOR, "body > footer")
    # todo: links at the page bottom
    TEXT_COPYRIGHT = 'Your Store © 2022'
    LOCATOR_COPYRIGHT = Selector(By.CSS_SELECTOR, "footer p")
    LOCATOR_POWERED_BY = Selector(By.CSS_SELECTOR, "footer p > a")
    TITLE_OPENCART_SITE = "OpenCart - Open Source Shopping Cart Solution"


class StoreFooter(BasePage):

    locator = StoreFooterLocators

    def click_powered_by(self):
        self.find_element(self.locator.LOCATOR_POWERED_BY).click()
        assert self.at_page(self.locator.TITLE_OPENCART_SITE)


if __name__ == '__main__':

    print(StoreFooter.locator.locators)
