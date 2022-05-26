import pytest
from pom.element.store.common import CommonElements, CommonElementsLocators
from pom.element.store.shopping_cart import ShoppingCartButton
from pom.store.main_page import MainPage, MainPageLocators
from pom.store.shopping_cart_page import (ShoppingCartPage,
                                          ShoppingCartPageLocators)

from conftest import skip_if


@pytest.fixture(scope='class', autouse=True)
def page(request, driver) -> MainPage:
    request.cls.driver = driver
    request.cls.url = MainPageLocators.URL
    page = MainPage(driver, request.cls.url)
    page.open()
    return page


class TestMainPage:

    def test_if_at_page(self, page: MainPage):
        assert page.at_page(page.locator.TITLE_MAIN_PAGE)

    def test_checkout_with_empty_cart(self):
        common_elements = CommonElements(self.driver, self.url)
        common_elements.click_checkout()
        page = ShoppingCartPage(self.driver, self.url)
        assert page.at_page(
            ShoppingCartPageLocators.TITLE_SHOPPING_CART_PAGE)
        assert page.is_empty()
        page.click_continue_button()
        assert page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_click_on_empty_shopping_cart(self):
        cart = ShoppingCartButton(self.driver)
        cart.click_button()
        assert cart.is_empty()

    def test_click_on_powered_by(self, base_url, page: MainPage):
        CommonElements(self.driver).click_powered_by()
        assert page.at_page(CommonElementsLocators.TITLE_OPENCART_SITE)
        page.url = base_url

    def test_copyright_should_present(self, page):
        assert CommonElementsLocators.TEXT_COPYRIGHT in page.find_element(
            CommonElementsLocators.LOCATOR_COPYRIGHT).text

    @skip_if('headless')
    def test_slideshow_next_prev_click(self, page: MainPage):
        target = 'Samsung Galaxy Tab 10.1'
        page.click_slideshow_next()
        page.click_slideshow_prev()
        page.click_slideshow()
        assert page.at_page(target)
        page.back()
        assert page.at_page(MainPageLocators.TITLE_MAIN_PAGE)
        page.click_slideshow_prev()
        page.click_slideshow_next()
        page.click_slideshow()
        assert page.at_page(target)
