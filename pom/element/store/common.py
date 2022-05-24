from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class CommonElementsLocators(BaseLocator):

    LOCATOR_IMG_LOGO = Selector(By.CSS_SELECTOR, "#logo")
    LOCATOR_LINK_SHOPPING_CART = Selector(
        By.CSS_SELECTOR, "a[title='Shopping Cart']")
    LOCATOR_LINK_WISH_LIST = Selector(By.CSS_SELECTOR, "a[title*='Wish List']")
    LOCATOR_LINK_CHECKOUT = Selector(By.CSS_SELECTOR, "a[title='Checkout']")
    LOCATOR_COPYRIGHT = Selector(By.CSS_SELECTOR, "footer p")
    LOCATOR_POWERED_BY = Selector(By.CSS_SELECTOR, "footer p > a")
    TEXT_COPYRIGHT = 'Your Store © 2022'
    TITLE_OPENCART_SITE = "OpenCart - Open Source Shopping Cart Solution"


class CommonElements(BasePage):

    locator = CommonElementsLocators

    def click_logo(self):
        return self.find_element(self.locator.LOCATOR_IMG_LOGO).click()

    def click_checkout(self):
        self.find_element(self.locator.LOCATOR_LINK_CHECKOUT).click()

    def click_wish_list(self):
        self.find_element(self.locator.LOCATOR_LINK_WISH_LIST).click()

    def click_shopping_cart(self):
        self.find_element(self.locator.LOCATOR_LINK_SHOPPING_CART).click()

    def click_powered_by(self):
        self.find_element(self.locator.LOCATOR_POWERED_BY).click()
