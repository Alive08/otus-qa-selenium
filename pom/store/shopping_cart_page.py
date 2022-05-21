from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class ShoppingCartPageLocators(BaseLocator):

    TITLE_SHOPPING_CART_PAGE = "Shopping Cart"

    LOCATOR_BUTTON_CONTINUE = Selector(By.LINK_TEXT, "Continue")
    LOCATOR_HEADER_SHOPPING_CART = Selector(By.CSS_SELECTOR, "#content > h1")
    LOCATOR_SHOPPING_CART_EMPTY = Selector(By.CSS_SELECTOR, "#content > p")


class ShoppingCartPage(BasePage):

    locator = ShoppingCartPageLocators

    def click_continue_button(self):
        return self.find_element(self.locator.LOCATOR_BUTTON_CONTINUE).click()


if __name__ == '__main__':

    print(ShoppingCartPage.locator.locators)
