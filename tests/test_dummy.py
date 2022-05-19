import pytest
from frame.browser import Browser
from pom.navbar import Navbar, Page
import inspect

@pytest.fixture(scope='session')
def driver():
    driver = Browser('chrome')()
    driver.get('http://127.0.0.1:8081')
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def page(driver):
    return Page(driver)

@pytest.mark.parametrize('p, l', [(i,j) for i in Navbar.items for j in [i, *i.items]])
def test_navbar(page, p, l):
    page.click(p)
    page.click(l)
