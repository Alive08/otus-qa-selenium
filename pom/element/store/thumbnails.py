from frame.base_page import BasePage
from frame.base_locator import BaseLocator, Selector
from selenium.webdriver.common.by import By


class ProductThumbnailsLocators(BaseLocator):

    LOCATOR_PRODUCT_THUMBNAILS = Selector(By.CSS_SELECTOR, ".product-thumb")
    LOCATOR_PRODUCT_THUMBNAIL_IMAGE = Selector(
        By.CSS_SELECTOR, ".product-thumb .image img")
    LOCATOR_PRODUCT_THUMBNAIL_HREF = Selector(
        By.CSS_SELECTOR, ".product-thumb .image a")
    LOCATOR_PRODUCT_THUMBNAIL_CAPTION_HREF = Selector(
        By.CSS_SELECTOR, ".product-thumb .caption h4 a")
    LOCATOR_PRODUCT_THUMBNAIL_CAPTION_DESCRIPTION = Selector(
        By.CSS_SELECTOR, "div.caption > p:nth-child(2)")
    LOCATOR_PRODUCT_THUMBNAIL_PRICE = Selector(
        By.CSS_SELECTOR, ".product-thumb p.price")
    LOCATOR_PRODUCT_THUMBNAIL_BUTTON_ADD_TO_CART = Selector(
        By.CSS_SELECTOR, ".button-group > button:nth-child(1)")
    LOCATOR_PRODUCT_THUMBNAIL_BUTTON_ADD_TO_WISH_LIST = Selector(
        By.CSS_SELECTOR, ".button-group > button:nth-child(2)")
    LOCATOR_PRODUCT_THUMBNAIL_BUTTON_ADD_TO_COMPARE = Selector(
        By.CSS_SELECTOR, ".button-group > button:nth-child(3)")


class ProductThumbnails(BasePage):

    locator = ProductThumbnailsLocators

    def get_products(self):
        return self.find_elements(self.locator.LOCATOR_PRODUCT_THUMBNAILS)

    def get_product(self, index):
        return self.get_products()[index]

    def get_product_link(self, product):
        return product.find_element(*self.locator.LOCATOR_PRODUCT_THUMBNAIL_HREF)

    def get_product_price(self, product):
        return product.find_element(*self.locator.LOCATOR_PRODUCT_THUMBNAIL_PRICE)

    def get_product_description(self, product):
        return product.find_element(*self.locator.LOCATOR_PRODUCT_THUMBNAIL_CAPTION_DESCRIPTION)

    def click_product_link(self, product):
        self.get_product_link(product).click()


if __name__ == '__main__':

    print(ProductThumbnails.locator.locators)
