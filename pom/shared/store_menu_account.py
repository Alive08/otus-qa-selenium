from frame.base_locator import BaseLocator, Selector
from frame.base_page import BaseMenu
from selenium.webdriver.common.by import By


class StoreMenuAccountLocators(BaseLocator):

    LOCATOR_MENU_ACCOUNT = Selector(By.CSS_SELECTOR, ".list-group")
    LOCATOR_MENU_ACCOUNT_LOGIN = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(1)")
    LOCATOR_MENU_ACCOUNT_REGISTER = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(2)")
    LOCATOR_MENU_ACCOUNT_FORGOTTEN_PASSWORD = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(3)")
    LOCATOR_MENU_ACCOUNT_MY_ACCOUNT = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(4)")
    LOCATOR_MENU_ACCOUNT_ADDRESS_BOOK = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(5)")
    LOCATOR_MENU_ACCOUNT_WISH_LIST = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(6)")
    LOCATOR_MENU_ACCOUNT_ORDER_HISTORY = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(7)")
    LOCATOR_MENU_ACCOUNT_DOWNLOADS = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(8)")
    LOCATOR_MENU_ACCOUNT_RECURRING_PAYMENTS = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(9)")
    LOCATOR_MENU_ACCOUNT_REWARD_POINTS = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(10)")
    LOCATOR_MENU_ACCOUNT_RETURNS = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(11)")
    LOCATOR_MENU_ACCOUNT_TRANSACTIONS = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(12)")
    LOCATOR_MENU_ACCOUNT_NEWSLETTER = Selector(
        By.CSS_SELECTOR, "#column-right > div > a:nth-child(13)")
    LOCATOR_MENU_ACCOUNT_LOGOUT = Selector(
        By.CSS_SELECTOR, "#column-right > div > a[href$='account/logout']")


class StoreMenuAccount(BaseMenu):

    locator = StoreMenuAccountLocators


if __name__ == '__main__':

    print(StoreMenuAccount.locator.locators)
