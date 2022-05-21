from collections import namedtuple

import pytest
from frame.utils import Utils
from pom.store.catalog_page import CatalogPage
from pom.store.main_page import MainPageLocators
from pom.element.store.menu_product import StoreMenuProductLocators
from pom.element.store.navbar import StoreNavbarLocators


@pytest.fixture(scope='class', autouse=True)
def page(request, driver, base_url):
    request.cls.page = CatalogPage(driver)
    request.cls.page.url = f'{base_url}/tablet'
    request.cls.page.open()


@pytest.mark.usefixtures('navbar', 'breadcrumb', 'menu_product', 'thumbnails')
class TestCatalogPage:


    def test_if_at_page(self):
        assert self.page.at_page('Tablets')

    @pytest.mark.parametrize('item, title', ((StoreNavbarLocators.LOCATOR_NAVBAR_DESKTOPS_PC, 'PC'),
                                             (StoreNavbarLocators.LOCATOR_NAVBAR_DESKTOPS_MAC, 'Mac'),
                                             (StoreNavbarLocators.LOCATOR_NAVBAR_COMPONENTS_MONITORS, 'Monitors'),
                                             (StoreNavbarLocators.LOCATOR_NAVBAR_DESKTOPS_ALL, 'Desktops')),
                             ids=StoreNavbarLocators.idfn)
    def test_navbar_with_subcats(self, item, title):
        self.navbar.click_item(item)
        assert self.page.at_page(title)

    @pytest.mark.parametrize('item, title', ((StoreNavbarLocators.LOCATOR_NAVBAR_TABLETS, 'Tablets'),
                                             (StoreNavbarLocators.LOCATOR_NAVBAR_SOFTWARE, 'Software'),
                                             (StoreNavbarLocators.LOCATOR_NAVBAR_PHONES,
                                              'Phones & PDAs'),
                                             (StoreNavbarLocators.LOCATOR_NAVBAR_CAMERAS, 'Cameras')),
                             ids=StoreNavbarLocators.idfn)
    def test_navbar_without_subcats(self, item, title):
        self.navbar.click_item(item)
        assert self.page.at_page(title)

    @pytest.mark.parametrize('item, title', ((StoreMenuProductLocators.LOCATOR_MENU_PRODUCT_LAPTOPS_MAC, 'Macs'),
                                             (StoreMenuProductLocators.LOCATOR_MENU_PRODUCT_DESKTOPS_PC, 'PC'),
                                             (StoreMenuProductLocators.LOCATOR_MENU_PRODUCT_COMPONENTS_MICE,
                                              'Mice and Trackballs'),
                                             (StoreMenuProductLocators.LOCATOR_MENU_PRODUCT_PHONES, 'Phones & PDAs')),
                             ids=StoreMenuProductLocators.idfn)
    def test_menu(self, item, title):
        self.menu_product.click_item(item)
        assert self.page.at_page(title)

    def test_breadcrumb_go_home(self):
        assert self.page.at_page('Tablets')
        self.breadcrumb.breadcrumb_go_home()
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_breadcrumb_walk(self):
        assert self.page.at_page('Tablets')
        self.menu_product.click.COMPONENTS_MONITORS
        assert self.page.at_page('Monitors')
        while not self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE):
            links = self.breadcrumb.get_breadcrumb_items()
            links.pop()
            links.pop().click()
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    @pytest.mark.parametrize('target', [Utils.skipped(l, ('LOCATOR_MENU_PRODUCT',
                                                          'LOCATOR_MENU_PRODUCT_MP3')
                                                      ) for l in StoreMenuProductLocators.locators],
                             ids=StoreMenuProductLocators.idfn)
    def test_breadcrumb_walk_menu(self, target):
        self.menu_product.click_item(target.locator)
        while not self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE):
            self.breadcrumb.breadcrumb_back()
        assert self.page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_view_list(self):
        self.menu_product.click.CAMERAS
        self.page.click_button_view_list()
        assert len(self.page.get_view_list_elements())

    def test_view_grid(self):
        self.menu_product.click.CAMERAS
        self.page.click_button_view_grid()
        assert len(self.page.get_view_grid_elements())

    @pytest.mark.parametrize('selected', (CatalogPage.select_sort_options.keys()))
    def test_select_sort(self, selected):
        self.page.select_sort_set_by_text(selected)
        assert self.page.get_sort_selected_option().text == selected

    @pytest.mark.parametrize('selected', (CatalogPage.select_show_options.keys()))
    def test_select_show(self, selected):
        self.page.select_show_set_by_text(selected)
        assert self.page.get_show_selected_option().text == selected

    def select_sort_data(self):
        options =  {'Default': 'Canon',
                'Name (A - Z)': 'Canon',
                'Name (Z - A)': 'Nikon',
                'Price (Low > High)': 'Canon',
                'Price (High > Low)': 'Nikon',
                'Rating (Highest)': 'Nikon',
                'Rating (Lowest)': 'Canon',
                'Model (A - Z)': 'Canon',
                'Model (Z - A)': 'Nikon'
                }
        Option = namedtuple('Option', ('text', 'value'))
        return [Option(*item) for item in options.items()]

    @pytest.mark.parametrize('selected', (select_sort_data(None)), ids=lambda v: v.text)
    def test_select_sort_cameras(self, selected):
        self.menu_product.click.CAMERAS
        self.page.select_sort_set_by_text(selected.text)
        assert self.page.get_sort_selected_option().text == selected.text
        assert selected.value in self.thumbnails.get_product_thumbnails().pop(0).text
