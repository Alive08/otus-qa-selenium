from selenium.webdriver.common.by import By
from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage


class DropdownAccountLocators(BaseLocator):

    LOCATOR_DROPDOWN_ACCOUNT = Selector(By.CSS_SELECTOR, "a[title='My Account']")
    LOCATOR_DROPDOWN_ACCOUNT_LOGIN = Selector(By.LINK_TEXT, "Login")
    LOCATOR_DROPDOWN_ACCOUNT_REGISTER = Selector(By.LINK_TEXT, "Register")
    LOCATOR_DROPDOWN_ACCOUNT_MY_ACCOUNT = Selector(By.LINK_TEXT, "My Account")
    LOCATOR_DROPDOWN_ACCOUNT_ORDER_HISTORY = Selector(
        By.LINK_TEXT, "Order History")
    LOCATOR_DROPDOWN_ACCOUNT_TRANSACTIONS = Selector(By.LINK_TEXT, "Transactions")
    LOCATOR_DROPDOWN_ACCOUNT_DOWNLOADS = Selector(By.LINK_TEXT, "Downloads")
    LOCATOR_DROPDOWN_ACCOUNT_LOGOUT = Selector(By.LINK_TEXT, "Logout")


class DropdownAccount(BasePage):

    locator = DropdownAccountLocators

    