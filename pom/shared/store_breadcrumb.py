from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class StoreBreadcrumbLocators(BaseLocator):

    LOCATOR_BREADCRUMB = Selector(By.CSS_SELECTOR, "#product-category > ul.breadcrumb")
    LOCATOR_BREADCRUMB_ITEM = Selector(By.CSS_SELECTOR, "#product-category > ul.breadcrumb > * a")
    LOCATOR_BREADCRUMB_HOME = Selector(
        By.CSS_SELECTOR, "#product-category > ul > li:nth-child(1) > a")


class StoreBreadcrumb(BasePage):

    locator = StoreBreadcrumbLocators

    def breadcrumb_go_home(self):
        # home = self.get_breadcrumb().find_element(*self.locator.LOCATOR_BREADCRUMB_HOME)
        # hover = ActionChains(self.driver).move_to_element(home).pause(0.5).click(home)
        # hover.perform()
        # # self.get_breadcrumb().find_element(*self.locator.LOCATOR_BREADCRUMB_HOME).click()
        self.find_element(self.locator.LOCATOR_BREADCRUMB_HOME).click()

    def get_breadcrumb(self):
        return self.find_element(self.locator.LOCATOR_BREADCRUMB, time=5)

    def get_breadcrumb_items(self):
        return self.get_breadcrumb().find_elements(*StoreBreadcrumbLocators.LOCATOR_BREADCRUMB_ITEM)

    def breadcrumb_back(self):
        el = self.get_breadcrumb_items()
        el.pop()
        el.pop().click()


if __name__ == '__main__':

    print(StoreBreadcrumb.locator.locators)
