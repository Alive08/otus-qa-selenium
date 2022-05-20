import pytest
from frame.browser import Browser
from pom.main_page import MainPage, Navbar


@pytest.fixture(scope='session')
def base_url():
    return 'http://127.0.0.1:8081'


@pytest.fixture(scope='session')
def driver():
    driver = Browser('chrome')()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def page(request, driver, base_url):
    page = MainPage(driver, base_url)
    if request.cls is not None:
        request.cls.page = page
    return page


@pytest.fixture
def back_to_base(request):
    yield
    request.cls.page.open()


@pytest.fixture(scope='class', autouse=True)
def page(driver, base_url):
    return MainPage(driver, base_url)


class TestMainPage:

    @pytest.fixture(scope='class')
    def mypage(self, page, base_url):
        page.url = f'{base_url}'
        page.open()

    def test_slideshow(self, page, base_url):
        page.go(base_url)
        target = 'Samsung Galaxy Tab 10.1'
        page.hover(page.slideshow.next).click()
        page.hover(page.slideshow.prev).click()
        page.hover(page.slideshow).click()
        assert page.at_page(target)
        page.back()
        assert page.at_page('Your Store')

    @pytest.mark.parametrize('p, l', [(p, l) for p in Navbar.items for l in [p, *p.items]], ids=lambda x: Navbar.item_name(x))
    def test_navbar(self, page, p, l):
        page.click(p)
        page.click(l)
