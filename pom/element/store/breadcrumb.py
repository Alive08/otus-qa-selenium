import allure
from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BreadcrumbLocators(BaseLocator):

    LOCATOR_BREADCRUMB = Selector(By.CSS_SELECTOR, "ul.breadcrumb")
    LOCATOR_BREADCRUMB_ITEM = Selector(By.CSS_SELECTOR, "ul.breadcrumb > * a")
    LOCATOR_BREADCRUMB_HOME = Selector(
        By.CSS_SELECTOR, "ul.breadcrumb > * a[href$='common/home']")


class Breadcrumb(BasePage):

    locator = BreadcrumbLocators

    @allure.step("go to home page using breadcrumb")
    def go_home(self):
        # self.click(self.locator.LOCATOR_BREADCRUMB_HOME)# - does not work with chromedriver
        self.actions.click(self.find_element(self.locator.LOCATOR_BREADCRUMB)).send_keys(
            Keys.TAB).send_keys(Keys.ENTER).perform()

    @allure.step("check if breadcrumb is at home page")
    def at_home(self, ele):
        return self.find_element(self.locator.LOCATOR_BREADCRUMB_HOME) == ele

    @allure.step("locate the breadcrumb")
    def get_self(self):
        return self.find_element(self.locator.LOCATOR_BREADCRUMB)

    @allure.step("get all breadcrumb's items")
    def get_items(self):
        return self.get_self().find_elements(*self.locator.LOCATOR_BREADCRUMB_ITEM)

    @allure.step("go back using breadcrumb")
    def back(self):
        els = self.get_items()
        els.pop()  # remove current page
        ele = els.pop()
        if self.at_home(ele):
            self.go_home()
        else:
            ele.click()


if __name__ == '__main__':

    print(Breadcrumb.locator.locators)
