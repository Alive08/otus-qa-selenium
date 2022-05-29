from frame.base_locator import BaseLocator
from frame.base_page import BasePage
from frame.node import Node
from selenium.webdriver.common.by import By


class AdminProductPageLocators(BaseLocator):

    class product(Node):

        name = (By.CSS_SELECTOR, "#form-product > * #input-name1")
        description = (By.CSS_SELECTOR, "#form-product > * div.note-editable > p")
        meta_tag_title = (By.CSS_SELECTOR, "#form-product > * #input-meta-title1")
        model = (By.CSS_SELECTOR, "#form-product > * #input-model")
        price = (By.CSS_SELECTOR, "#form-product > * #input-price")
        quantity = (By.CSS_SELECTOR, "#form-product > * #input-quantity")
        manufacturer = (By.CSS_SELECTOR, "#form-product > * #input-manufacturer")
        categories = (By.CSS_SELECTOR, "#form-product > * #input-category")

    class filter(Node):

        name = (By.CSS_SELECTOR, "#filter-product > * #input-name")
        model = (By.CSS_SELECTOR, "#filter-product > * #input-model")
        price = (By.CSS_SELECTOR, "#filter-product > * #input-price")
        quantity = (By.CSS_SELECTOR, "#filter-product > * input-quantity")
        status = (By.CSS_SELECTOR, "#filter-product > * input-status")
        button = (By.CSS_SELECTOR, "#filter-product > * #button-filter")

    class product_row(Node):

        self = (By.CSS_SELECTOR, "#form-product > * table > tbody > tr")
        checkbox = (By.CSS_SELECTOR, "#form-product > * table > tbody > tr > td > input[type='checkbox']")
        no_result = (By.CSS_SELECTOR, "#form-product > * table > tbody  > tr > td[colspan='8']")
        

class AdminProductPage(BasePage):

    locator = AdminProductPageLocators

    def set_product_name(self, name):
        self.enter_text(self.locator.product.name, name)

    def set_product_description(self, description):
        self.enter_text(self.locator.product.description, description)

    def set_meta_tag_title(self, tag):
        self.enter_text(self.locator.product.meta_tag_title, tag)

    def set_product_model(self, model):
        self.enter_text(self.locator.product.model, model)

    def set_product_price(self, price):
        self.enter_text(self.locator.product.price, price)

    def set_product_quantity(self, quantity):
        self.enter_text(self.locator.product.quantity, quantity)

    def set_product_category(self, category):
        self.enter_text_with_dropdown(
            self.locator.product.categories, category)

    def set_product_manufacturer(self, manufacturer):
        self.enter_text_with_dropdown(
            self.locator.product.manufacturer, manufacturer)

    def set_filter_name(self, name):
        self.enter_text(self.locator.filter.name, name)
    
    def set_filter_model(self, model):
        self.enter_text(self.locator.filter.model, model)

    def set_filter_price(self, price):
        self.enter_text(self.locator.filter.model, price)

    def set_filter_quantity(self, quantity):
        self.enter_text(self.locator.filter.model, quantity)

    def set_filter_status(self, status):
        # TBD
        pass

    def click_filter(self):
        self.click(self.locator.filter.button)
    
    def get_products(self):
        if self.does_not_present(self.locator.product_row.no_result):
            return self.find_elements(self.locator.product_row.self)

    def is_product_selected(self, product):
        return product.find_element(*self.locator.product_row.checkbox).get_attribute('checked')

    def select_product(self, product):
        if not self.is_product_selected(product):
            product.find_element(*self.locator.product_row.checkbox).click()

    def unselect_product(self, product):
        if self.is_product_selected(product):
            product.find_element(*self.locator.product_row.checkbox).click()

