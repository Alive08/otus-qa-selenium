import pytest
from pom.main_page import MainPageLocators
from pom.search_page import SearchPage, SearchPageLocators


@pytest.fixture(scope='class', autouse=True)
def page(request, driver):
    request.cls.page = SearchPage(driver)
    request.cls.page.open()


@pytest.mark.usefixtures('header')
class TestSearchFromMainPage:

    def test_if_at_page(self):
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_click_search_button_no_text(self):
        self.header.click_search_button()
        assert self.page.at_page(SearchPageLocators.TITLE_SEARCH_PAGE)
        assert SearchPageLocators.LOCATOR_TEXT_SEARCH_FAIL in self.page.page_src

    @pytest.mark.parametrize('text, fail', (('iphone', False), ('xiaomi', True)), ids=('success', 'fail'))
    def test_search_product(self, text, fail):
        self.header.do_search(text)
        assert self.page.at_page(f"Search - {text}")
        if fail:
            assert SearchPageLocators.LOCATOR_TEXT_SEARCH_FAIL in self.page.page_src
        else:
            assert SearchPageLocators.LOCATOR_TEXT_SEARCH_FAIL not in self.page.page_src

    def test_add_product_to_shopping_cart(self):
        pass


class TestSearchPage:
    # TBD
    pass
