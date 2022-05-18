import pytest
from pom.main_page import MainPage, MainPageLocators
from pom.shared.store_footer import StoreFooterLocators
from pom.shared.store_header import StoreHeaderLocators
from pom.shopping_cart_page import ShoppingCartPageLocators

from conftest import skip_if


@pytest.fixture(scope='class', autouse=True)
def page(request, driver):
    request.cls.page = MainPage(driver)
    request.cls.page.open()


@pytest.mark.usefixtures('top', 'header', 'footer')
class TestMainPage:

    def test_if_at_page(self):
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_checkout_with_empty_cart(self):
        self.top.click_checkout()
        assert self.page.at_page(
            ShoppingCartPageLocators.TITLE_SHOPPING_CART_PAGE)
        assert self.page.find_element(
            ShoppingCartPageLocators.LOCATOR_HEADER_SHOPPING_CART)
        assert self.page.find_element(
            ShoppingCartPageLocators.LOCATOR_SHOPPING_CART_EMPTY)
        self.page.find_element(
            ShoppingCartPageLocators.LOCATOR_BUTTON_CONTINUE).click()
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_click_on_empty_shopping_cart(self):
        self.header.click_shopping_cart_button()
        assert self.page.find_element(
            StoreHeaderLocators.LOCATOR_TEXT_SHOPPING_CART_EMPTY)

    def test_click_on_powered_by(self, base_url):
        self.footer.click_powered_by()
        assert self.page.at_page(StoreFooterLocators.TITLE_OPENCART_SITE)
        self.page.url = base_url

    def test_copyright_should_present(self):
        assert StoreFooterLocators.TEXT_COPYRIGHT in self.page.find_element(
            StoreFooterLocators.LOCATOR_COPYRIGHT).text

    @skip_if('headless')
    def test_slideshow_next_prev_click(self):
        target = 'Samsung Galaxy Tab 10.1'
        self.page.click_slideshow_next()
        self.page.click_slideshow_prev()
        self.page.click_slideshow()
        assert self.page.at_page(target)
        self.page.back()
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)
        self.page.click_slideshow_prev()
        self.page.click_slideshow_next()
        self.page.click_slideshow()
        assert self.page.at_page(target)
