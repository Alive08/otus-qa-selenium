from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By


class SearchStringLocators(BaseLocator):
    
    LOCATOR_INPUT_SEARCH = Selector(By.NAME, "search")
    LOCATOR_BUTTON_SEARCH = Selector(
        By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
        

class SearchString(BasePage):

    locator = SearchStringLocators

    def click_search_button(self):
        return self.find_element(self.locator.LOCATOR_BUTTON_SEARCH).click()

    def do_search(self, text):
        element = self.find_element(self.locator.LOCATOR_INPUT_SEARCH)
        element.click()
        element.clear()
        element.send_keys(text)
        self.click_search_button()
