from selenium.webdriver.common.by import By
from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage


class DropdownCurrencyLocators(BaseLocator):

    LOCATOR_FORM_CURRENCY = Selector(By.CSS_SELECTOR, "#form-currency")
    LOCATOR_BUTTON_DROPDOWN_CURRENCY = Selector(
        By.CSS_SELECTOR, "button.btn.btn-link.dropdown-toggle")
    LOCATOR_DROPDOWN_CURRENCY = Selector(
        By.CSS_SELECTOR, "ul.dropdown-menu")
    LOCATOR_DROPDOWN_CURRENCY_USD = Selector(
        By.CSS_SELECTOR, "button[name=USD]")
    LOCATOR_DROPDOWN_CURRENCY_EUR = Selector(
        By.CSS_SELECTOR, "button[name=EUR]")
    LOCATOR_DROPDOWN_CURRENCY_GBP = Selector(
        By.CSS_SELECTOR, "button[name=GBP]")
    LOCATOR_DROPDOWN_CURRENCY_SELECTED = Selector(By.CSS_SELECTOR, "strong")


class DropdownCurrency(BasePage):

    locator = DropdownCurrencyLocators
