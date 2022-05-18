from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class StoreHeaderLocators(BaseLocator):

    LOCATOR_HEADER = Selector(By.CSS_SELECTOR, "body > header")
    LOCATOR_IMG_LOGO = Selector(By.CSS_SELECTOR, "#logo")
    LOCATOR_INPUT_SEARCH = Selector(By.NAME, "search")
    LOCATOR_BUTTON_SEARCH = Selector(
        By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    LOCATOR_BUTTON_SHOPPING_CART = Selector(
        By.CSS_SELECTOR, "#cart > button")
    LOCATOR_TEXT_SHOPPING_CART_EMPTY = Selector(
        By.CSS_SELECTOR, "#cart > ul > li > p")
    LOCATOR_TEXT_SHOPPING_CART_NOT_EMPTY = Selector(
        By.CSS_SELECTOR, "#cart-total")


class StoreHeader(BasePage):

    locator = StoreHeaderLocators

    def click_logo(self):
        return self.find_element(self.locator.LOCATOR_IMG_LOGO).click()

    def click_search_button(self):
        return self.find_element(self.locator.LOCATOR_BUTTON_SEARCH).click()

    def click_shopping_cart_button(self):
        return self.find_element(self.locator.LOCATOR_BUTTON_SHOPPING_CART).click()

    def do_search(self, text):
        element = self.find_element(self.locator.LOCATOR_INPUT_SEARCH)
        element.click()
        element.clear()
        element.send_keys(text)
        self.click_search_button()

    def get_shopping_cart_total(self):
        return self.find_element(self.locator.LOCATOR_TEXT_SHOPPING_CART_NOT_EMPTY).text

    def is_shopping_cart_empty(self):
        return not self.find_element(self.locator.LOCATOR_TEXT_SHOPPING_CART_EMPTY)


if __name__ == '__main__':

    print(StoreHeader.locator.locators)
