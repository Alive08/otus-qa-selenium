from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class BreadcrumbLocators(BaseLocator):

    LOCATOR_BREADCRUMB = Selector(By.CSS_SELECTOR, "ul.breadcrumb")
    LOCATOR_BREADCRUMB_ITEM = Selector(By.CSS_SELECTOR, "ul.breadcrumb > * a")
    LOCATOR_BREADCRUMB_HOME = Selector(
        By.CSS_SELECTOR, "ul.breadcrumb > * a[href$='common/home']")


class Breadcrumb(BasePage):

    locator = BreadcrumbLocators

    def go_home(self):
        self.find_element(self.locator.LOCATOR_BREADCRUMB_HOME).click()

    def get_self(self):
        return self.find_element(self.locator.LOCATOR_BREADCRUMB)

    def get_items(self):
        return self.get_self().find_elements(*self.locator.LOCATOR_BREADCRUMB_ITEM)

    def back(self):
        el = self.get_breadcrumb_items()
        el.pop()
        el.pop().click()


if __name__ == '__main__':

    print(Breadcrumb.locator.locators)
