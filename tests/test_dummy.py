import pytest
from frame.browser import Browser
from pom.navbar import Navbar, Page


@pytest.fixture(scope='session')
def driver():
    driver = Browser('chrome')()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def page(driver):
    return Page(driver)

@pytest.mark.parametrize('item', [i for k in Navbar.items for i in k.items], ids=lambda x: x[1])
def test_navbar(page, item):
    pass