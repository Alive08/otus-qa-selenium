from frame.base_locator import BaseLocator, Selector
from frame.base_page import BaseMenu
from selenium.webdriver.common.by import By


class StoreMenuProductLocators(BaseLocator):

    # _XPATH_LEFT_MENU = "//*[@id='column-left']//a[contains(text(), '{}')]"
    # _XPATH_LEFT_MENU = "//*[@id='column-left']//a[text()='{}')]"

    LOCATOR_MENU_PRODUCT = Selector(By.CSS_SELECTOR, "#column-left")

    LOCATOR_MENU_PRODUCT_DESKTOPS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='desktops']")
    LOCATOR_MENU_PRODUCT_DESKTOPS_PC = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='desktops/pc']")
    LOCATOR_MENU_PRODUCT_DESKTOPS_MAC = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='desktops/mac']")

    LOCATOR_MENU_PRODUCT_LAPTOPS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='laptop-notebook']")
    LOCATOR_MENU_PRODUCT_LAPTOPS_MAC = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='laptop-notebook/macs']")
    LOCATOR_MENU_PRODUCT_LAPTOPS_WIN = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='laptop-notebook/windows']")

    LOCATOR_MENU_PRODUCT_COMPONENTS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='component']")
    LOCATOR_MENU_PRODUCT_COMPONENTS_MICE = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='component/mouse']")
    LOCATOR_MENU_PRODUCT_COMPONENTS_MONITORS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='component/monitor']")
    LOCATOR_MENU_PRODUCT_COMPONENTS_PRINTERS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='component/printer']")
    LOCATOR_MENU_PRODUCT_COMPONENTS_SCANNERS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='component/scanner']")
    LOCATOR_MENU_PRODUCT_COMPONENTS_WEBCAMERA = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='component/web-camera']")

    LOCATOR_MENU_PRODUCT_TABLETS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='tablet']")

    LOCATOR_MENU_PRODUCT_SOFTWARE = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='software']")

    LOCATOR_MENU_PRODUCT_PHONES = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='smartphone']")

    LOCATOR_MENU_PRODUCT_CAMERAS = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='camera']")

    LOCATOR_MENU_PRODUCT_MP3 = Selector(
        By.CSS_SELECTOR, "#column-left > * a[href$='mp3-players']")


class StoreMenuProduct(BaseMenu):

    locator = StoreMenuProductLocators

if __name__ == '__main__':

    print(StoreMenuProduct.locator.locators)
