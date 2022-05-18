from frame.base_locator import BaseLocator, Selector
from frame.base_page import BaseMenu
from selenium.webdriver.common.by import By


class StoreNavbarLocators(BaseLocator):

    # _XPATH_NAVBAR = "//*[@id='menu']//a[contains(text(),'{}')]"
    # _XPATH_NAVBAR = "//*[@id='menu']//a[text()='{}']"

    LOCATOR_NAVBAR = Selector(By.CSS_SELECTOR, "ul.nav.navbar-nav")

    LOCATOR_NAVBAR_DESKTOPS = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(1) > a")
    LOCATOR_NAVBAR_DESKTOPS_PC = Selector(
        By.CSS_SELECTOR, "#menu > *  li:nth-child(1) > * li:nth-child(1) > a")
    LOCATOR_NAVBAR_DESKTOPS_MAC = Selector(
        By.CSS_SELECTOR, "#menu > *  li:nth-child(1) > * li:nth-child(2) > a")
    LOCATOR_NAVBAR_DESKTOPS_ALL = Selector(
        By.CSS_SELECTOR, "#menu > * ul > li:nth-child(1) > div > a")

    LOCATOR_NAVBAR_LAPTOPS = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(2) > a")
    LOCATOR_NAVBAR_LAPTOPS_MAC = Selector(
        By.CSS_SELECTOR, "#menu > *  li:nth-child(2) > * li:nth-child(1) > a")
    LOCATOR_NAVBAR_LAPTOPS_WIN = Selector(
        By.CSS_SELECTOR, "#menu > *  li:nth-child(2) > * li:nth-child(2) > a")
    LOCATOR_NAVBAR_LAPTOPS_ALL = Selector(
        By.CSS_SELECTOR, "#menu > * ul > li:nth-child(2) > div > a")

    LOCATOR_NAVBAR_COMPONENTS = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(3) > a")
    LOCATOR_NAVBAR_COMPONENTS_MICE = (
        By.CSS_SELECTOR, "#menu > *  li:nth-child(3) > * li:nth-child(1) > a")
    LOCATOR_NAVBAR_COMPONENTS_MONITORS = Selector(
        By.CSS_SELECTOR, "#menu > * li:nth-child(3) > * li:nth-child(2) > a")
    LOCATOR_NAVBAR_COMPONENTS_PRINTERS = Selector(
        By.CSS_SELECTOR, "#menu > * li:nth-child(3) > * li:nth-child(3) > a")
    LOCATOR_NAVBAR_COMPONENTS_SCANNERS = Selector(
        By.CSS_SELECTOR, "#menu > * li:nth-child(3) > * li:nth-child(4) > a")
    LOCATOR_NAVBAR_COMPONENTS_WEBCAMERA = Selector(
        By.CSS_SELECTOR, "#menu > * li:nth-child(3) > * li:nth-child(5) > a")
    LOCATOR_NAVBAR_COMPONENTS_ALL = Selector(
        By.CSS_SELECTOR, "#menu > * ul > li:nth-child(3) > div > a")

    LOCATOR_NAVBAR_TABLETS = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(4) > a")

    LOCATOR_NAVBAR_SOFTWARE = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(5) > a")

    LOCATOR_NAVBAR_PHONES = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(6) > a")

    LOCATOR_NAVBAR_CAMERAS = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(7) > a")

    LOCATOR_NAVBAR_MP3 = Selector(
        By.CSS_SELECTOR, "#menu > * > ul > li:nth-child(8) > a")


class StoreNavbar(BaseMenu):

    locator = StoreNavbarLocators

if __name__ == '__main__':

    print(StoreNavbar.locator.locators)
