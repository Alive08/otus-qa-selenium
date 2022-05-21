from frame.base_locator import BaseLocator, Selector
from frame.base_page import BaseMenu, BasePage
from selenium.webdriver.common.by import By


class StoreTopLocators(BaseLocator):

    LOCATOR_TOP = Selector(By.CSS_SELECTOR, "#top")
    LOCATOR_FORM_CURRENCY = Selector(By.CSS_SELECTOR, "#form-currency")
    LOCATOR_BUTTON_DROPDOWN_CURRENCY = Selector(
        By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle")
    LOCATOR_DROPDOWN_LIST_CURRENCY = Selector(
        By.CSS_SELECTOR, "ul.dropdown-menu")
    LOCATOR_DROPDOWN_LIST_CURRENCY_USD = Selector(
        By.CSS_SELECTOR, "button[name=USD]")
    LOCATOR_DROPDOWN_LIST_CURRENCY_EUR = Selector(
        By.CSS_SELECTOR, "button[name=EUR]")
    LOCATOR_DROPDOWN_LIST_CURRENCY_GBP = Selector(
        By.CSS_SELECTOR, "button[name=GBP]")
    LOCATOR_SELECTED_CURRENCY = Selector(By.CSS_SELECTOR, "strong")

    LOCATOR_SHOPPING_CART = Selector(
        By.CSS_SELECTOR, "a[title='Shopping Cart']")
    LOCATOR_CHECKOUT = Selector(By.CSS_SELECTOR, "a[title='Checkout']")


class StoreTopMenuAccountLocators(BaseLocator):

    LOCATOR_ACCOUNT_MENU = Selector(By.CSS_SELECTOR, "a[title='My Account']")
    LOCATOR_ACCOUNT_MENU_LOGIN = Selector(By.LINK_TEXT, "Login")
    LOCATOR_ACCOUNT_MENU_REGISTER = Selector(By.LINK_TEXT, "Register")
    LOCATOR_ACCOUNT_MENU_MY_ACCOUNT = Selector(By.LINK_TEXT, "My Account")
    LOCATOR_ACCOUNT_MENU_ORDER_HISTORY = Selector(
        By.LINK_TEXT, "Order History")
    LOCATOR_ACCOUNT_MENU_TRANSACTIONS = Selector(By.LINK_TEXT, "Transactions")
    LOCATOR_ACCOUNT_MENU_DOWNLOADS = Selector(By.LINK_TEXT, "Downloads")
    LOCATOR_ACCOUNT_MENU_LOGOUT = Selector(By.LINK_TEXT, "Logout")


class StoreTopMenuAccount(BaseMenu):

    locator = StoreTopMenuAccountLocators


class StoreTop(BasePage):

    locator = StoreTopLocators

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.menu = StoreTopMenuAccount(self.driver, self.url)

    def click_checkout(self):
        self.find_element(self.locator.LOCATOR_CHECKOUT).click()


if __name__ == '__main__':

    print(StoreTop.locator.locators)
