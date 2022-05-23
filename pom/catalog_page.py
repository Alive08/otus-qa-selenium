from frame.base_locator import BaseLocator, Selector
from frame.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CatalogPageLocators(BaseLocator):

    LOCATOR_SELECT_SORT = Selector(By.CSS_SELECTOR, "#input-sort")
    LOCATOR_SELECT_SORT_DEFAULT = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(2)")
    LOCATOR_SELECT_SORT_BY_NAME_AZ = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(2)")
    LOCATOR_SELECT_SORT_BY_NAME_ZA = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(3)")
    LOCATOR_SELECT_SORT_BY_PRICE_LOHI = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(4)")
    LOCATOR_SELECT_SORT_BY_PRICE_HILO = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(5)")
    LOCATOR_SELECT_SORT_BY_RATING_HI = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(6)")
    LOCATOR_SELECT_SORT_BY_RATING_LO = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(7)")
    LOCATOR_SELECT_SORT_BY_MODEL_AZ = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(8)")
    LOCATOR_SELECT_SORT_BY_MODEL_ZA = Selector(
        By.CSS_SELECTOR, "#input-sort > option:nth-child(9)")

    LOCATOR_SELECT_SHOW = Selector(By.CSS_SELECTOR, "#input-limit")
    LOCATOR_SELECT_SHOW_15 = Selector(
        By.CSS_SELECTOR, "#input-limit > option:nth-child(1)")
    LOCATOR_SELECT_SHOW_25 = Selector(
        By.CSS_SELECTOR, "#input-limit > option:nth-child(2)")
    LOCATOR_SELECT_SHOW_50 = Selector(
        By.CSS_SELECTOR, "#input-limit > option:nth-child(3)")
    LOCATOR_SELECT_SHOW_75 = Selector(
        By.CSS_SELECTOR, "#input-limit > option:nth-child(4)")
    LOCATOR_SELECT_SHOW_100 = Selector(
        By.CSS_SELECTOR, "#input-limit > option:nth-child(5)")

    LOCATOR_BUTTON_VIEW_LIST = Selector(By.CSS_SELECTOR, "#list-view")
    LOCATOR_BUTTON_VIEW_GRID = Selector(By.CSS_SELECTOR, "#grid-view")

    LOCATOR_LAYOUT_LIST = Selector(
        By.CSS_SELECTOR, "div.product-layout.product-list")
    LOCATOR_LAYOUT_GRID = Selector(
        By.CSS_SELECTOR, "div.product-layout.product-grid")

    LOCATOR_LINK_PRODUCT_COMPARE = Selector(
        By.PARTIAL_LINK_TEXT, "Product Compare ")


class CatalogPage(BasePage):

    locator = CatalogPageLocators

    select_sort_options = {'Default': locator.LOCATOR_SELECT_SORT_DEFAULT,
                           'Name (A - Z)': locator.LOCATOR_SELECT_SORT_BY_MODEL_AZ,
                           'Name (Z - A)': locator.LOCATOR_SELECT_SORT_BY_MODEL_ZA,
                           'Price (Low > High)': locator.LOCATOR_SELECT_SORT_BY_PRICE_LOHI,
                           'Price (High > Low)': locator.LOCATOR_SELECT_SORT_BY_PRICE_HILO,
                           'Rating (Highest)': locator.LOCATOR_SELECT_SORT_BY_RATING_HI,
                           'Rating (Lowest)': locator.LOCATOR_SELECT_SORT_BY_RATING_LO,
                           'Model (A - Z)': locator.LOCATOR_SELECT_SORT_BY_MODEL_AZ,
                           'Model (Z - A)': locator.LOCATOR_SELECT_SORT_BY_MODEL_ZA
                           }

    select_show_options = {'15': locator.LOCATOR_SELECT_SHOW_15,
                           '25': locator.LOCATOR_SELECT_SHOW_25,
                           '50': locator.LOCATOR_SELECT_SHOW_50,
                           '75': locator.LOCATOR_SELECT_SHOW_75,
                           '100': locator.LOCATOR_SELECT_SHOW_100
                           }

    def get_select_sort(self):
        return Select(self.find_element(CatalogPageLocators.LOCATOR_SELECT_SORT))

    def get_select_show(self):
        return Select(self.find_element(CatalogPageLocators.LOCATOR_SELECT_SHOW))

    def select_sort_set_by_text(self, text):
        self.get_select_sort().select_by_visible_text(text)

    def select_show_set_by_text(self, text):
        self.get_select_show().select_by_visible_text(text)

    def get_show_selected_option(self):
        return self.get_select_show().first_selected_option

    def get_sort_selected_option(self):
        return self.get_select_sort().first_selected_option

    def click_button_view_list(self):
        self.find_element(self.locator.LOCATOR_BUTTON_VIEW_LIST).click()

    def click_button_view_grid(self):
        self.find_element(self.locator.LOCATOR_BUTTON_VIEW_GRID).click()

    def get_view_list_elements(self):
        return self.find_elements(self.locator.LOCATOR_LAYOUT_LIST)

    def get_view_grid_elements(self):
        return self.find_elements(self.locator.LOCATOR_LAYOUT_GRID)


if __name__ == '__main__':

    print(CatalogPage.locator.locators)
