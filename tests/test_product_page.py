import pytest
from pom.store.product_page import ProductPage


@pytest.fixture(scope='class', autouse=True)
def page(request, driver):
    request.cls.page = ProductPage(driver)
    request.cls.page.open()


@pytest.mark.usefixtures('header', 'navbar', 'thumbnails')
class TestProductPage:

    def test_select_product_from_catalog(self):
        self.navbar.click.COMPONENTS_MONITORS
        product = self.thumbnails.get_product_thumbnails().pop()
        self.thumbnails.click_product_thumbnail_link(product)
        assert 'monitor/samsung-syncmaster-941bw' in self.page.current_url
        assert self.page.at_page('Samsung SyncMaster 941BW')

    @pytest.mark.parametrize('index, expr', ((0, 'macbook'),
                                             (1, 'iphone'),
                                             (2, 'test'),
                                             (3, 'canon-eos-5d')))
    def test_select_product_from_featured(self, index, expr):
        self.thumbnails.get_product_thumbnail_link(
            self.thumbnails.get_product_thumbnail(index)).click()
        assert expr in self.page.current_url

    def test_add_product_to_shopping_cart(self):
        self.thumbnails.get_product_thumbnail(1).click()
        assert self.page.at_page('iPhone')
        self.page.add_product_to_shopping_cart(quantity=1)
        assert self.page.get_product_price() in self.header.get_shopping_cart_total()

    @pytest.mark.parametrize('item', range(0, 4), ids=('MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D'))
    def test_view_product_images(self, item):
        self.thumbnails.click_product_thumbnail_link(
            self.thumbnails.get_product_thumbnail(item))
        for t in self.page.get_thumbnails():
            t.click()
            self.page.close_thumbnail_image()
