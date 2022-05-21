from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class StoreBreadcrumbLocators(BaseLocator):

    LOCATOR_BREADCRUMB = Selector(By.CSS_SELECTOR, "ul.breadcrumb")
    LOCATOR_BREADCRUMB_ITEM = Selector(By.CSS_SELECTOR, "ul.breadcrumb > * a")
    LOCATOR_BREADCRUMB_HOME = Selector(
        By.CSS_SELECTOR, "ul.breadcrumb > * a[href$='common/home']")


class StoreBreadcrumb(BasePage):

    locator = StoreBreadcrumbLocators

    def breadcrumb_go_home(self):
        self.find_element(self.locator.LOCATOR_BREADCRUMB_HOME).click()

    def get_breadcrumb(self):
        return self.find_element(self.locator.LOCATOR_BREADCRUMB)

    def get_breadcrumb_items(self):
        return self.get_breadcrumb().find_elements(*StoreBreadcrumbLocators.LOCATOR_BREADCRUMB_ITEM)

    def breadcrumb_back(self):
        el = self.get_breadcrumb_items()
        el.pop()
        el.pop().click()


if __name__ == '__main__':

    print(StoreBreadcrumb.locator.locators)
