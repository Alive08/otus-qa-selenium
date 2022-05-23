from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class ShoppingCartButtonLocators(BaseLocator):

    LOCATOR_BUTTON_SHOPPING_CART = Selector(
        By.CSS_SELECTOR, "#cart > button")
    LOCATOR_TEXT_SHOPPING_CART_EMPTY = Selector(
        By.CSS_SELECTOR, "#cart > ul > li > p")
    LOCATOR_TEXT_SHOPPING_CART_NOT_EMPTY = Selector(
        By.CSS_SELECTOR, "#cart-total")


class ShoppingCartButton(BasePage):

    locator = ShoppingCartButtonLocators

    def click_shopping_cart_button(self):
        return self.find_element(self.locator.LOCATOR_BUTTON_SHOPPING_CART).click()

    def get_shopping_cart_total(self):
        return self.find_element(self.locator.LOCATOR_TEXT_SHOPPING_CART_NOT_EMPTY).text

    def is_shopping_cart_empty(self):
        return not self.find_element(self.locator.LOCATOR_TEXT_SHOPPING_CART_EMPTY)
    