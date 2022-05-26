import pytest
from pom.element.store.navbar import navbar
from pom.element.store.shopping_cart import ShoppingCartButton
from pom.element.store.thumbnails import ProductThumbnails
from pom.store.product_page import ProductPage, ProductPageLocators


@pytest.fixture(scope='class', autouse=True)
def page(request, driver) -> ProductPage:
    request.cls.driver = driver
    request.cls.url = ProductPageLocators.URL
    page = ProductPage(driver)
    page.open()
    return page


class TestProductPage:

    def test_select_product_from_catalog(self, page: ProductPage):
        page.hover(navbar.components)
        page.click(navbar.components.monitors)
        tn = ProductThumbnails(self.driver, self.url)
        product = tn.get_products().pop()
        tn.click_product_link(product)
        assert 'monitor/samsung-syncmaster-941bw' in page.current_url
        assert page.at_page('Samsung SyncMaster 941BW')

    @pytest.mark.parametrize('index, expr', ((0, 'macbook'),
                                             (1, 'iphone'),
                                             (2, 'test'),
                                             (3, 'canon-eos-5d')))
    def test_select_product_from_featured(self, index, expr, page: ProductPage):
        tn = ProductThumbnails(self.driver, self.url)
        tn.get_product_link(
            tn.get_product(index)).click()
        assert expr in page.current_url

    def test_add_product_to_shopping_cart(self, page: ProductPage):
        tn = ProductThumbnails(self.driver, self.url)
        tn.get_product(1).click()
        assert page.at_page('iPhone')
        page.add_product_to_shopping_cart(quantity=1)
        assert page.get_product_price() in ShoppingCartButton(
            self.driver, self.url).get_total()

    @pytest.mark.parametrize('item', range(0, 4), ids=('MacBook', 'iPhone', 'Apple Cinema 30"', 'Canon EOS 5D'))
    def test_view_product_images(self, item, page: ProductPage):
        tn = ProductThumbnails(self.driver, self.url)
        tn.click_product_link(tn.get_product(item))
        for t in page.get_thumbnails():
            t.click()
            page.close_thumbnail_image()
