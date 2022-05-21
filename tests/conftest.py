from dataclasses import dataclass
import os
import random
from collections import namedtuple

from faker import Faker
import pytest
from frame.browser import Browser
from frame.utils import Utils
from pom.admin.login_page import AdminLoginPage
from pom.store.catalog_page import CatalogPage
from pom.store.main_page import MainPage
from pom.store.product_page import ProductPage
from pom.store.register_account_page import RegisterAccountPage
from pom.store.search_page import SearchPage
from pom.element.store.breadcrumb import StoreBreadcrumb
from pom.element.store.footer import StoreFooter
from pom.element.store.header import StoreHeader
from pom.element.store.menu_account import StoreMenuAccount
from pom.element.store.menu_product import StoreMenuProduct
from pom.element.store.navbar import StoreNavbar
from pom.element.store.thumbnails import StoreProductThumbnails
from pom.element.store.top import StoreTop

BASE_URL = f"http://{Utils.get_ip()}:8081"

USER_OPTIONS = ('--headless',
                '--start-maximized',
                '--start-fullscreen')


def pytest_addoption(parser):
    parser.addoption("--base-url", default=BASE_URL)
    parser.addoption("--browser", default="chrome",
                     choices=('chrome', 'firefox', 'edge', 'opera', 'yandex'))
    parser.addoption("--headless", action="store_true")
    parser.addoption("--start-maximized", action="store_true")
    parser.addoption("--start-fullscreen", action="store_true")


option = None


def pytest_configure(config):
    global option
    option = config.option


def skip_if(opt):
    return pytest.mark.skipif(
        getattr(option, opt, None),
        reason=f"Incompatible with {opt}"
    )


def skip_if_not(opt):
    return pytest.mark.skipif(
        not getattr(option, opt, None),
        reason=f"Only with {opt}"
    )


@pytest.fixture(scope='session')
def base_url(request):
    return request.config.getoption("--base-url")


Creds = namedtuple('Creds', ('login', 'password'))


@pytest.fixture(scope='session')
def valid_creds():
    return Creds('user', 'bitnami')


@pytest.fixture(scope='session')
def invalid_creds():
    return Creds('user', 'bitnomi')


@pytest.fixture(scope='session')
def driver(request):
    options = {}
    for option in USER_OPTIONS:
        if request.config.getoption(option):
            options.update({option: True})

    driver = Browser(request.config.getoption("--browser"),
                     options=options)()

    yield driver

    driver.close()
    driver.quit()


@dataclass
class AccountData:
    fname: str
    lname: str
    email: str
    phone: str
    password_1: str
    password_2: str


@pytest.fixture
def account_valid():
    return AccountData('Denzel', 'Washington', 'denzel.washington@holliwood.com', '+1 234 5678 90', 'helloUser', 'helloUser')


@pytest.fixture
def account_random():
    fake = Faker()
    return AccountData(
        fname=fake.first_name(),
        lname=fake.last_name(),
        email=fake.email(),
        phone=fake.phone_number(),
        password_1=fake.password(),
        password_2=fake.password()
    )


@pytest.fixture
def wd(request, driver):
    request.cls.wd = driver


@pytest.fixture(autouse=True)
def back_to_base(request):
    yield
    request.cls.page.open()


@pytest.fixture(scope='class')
def top(request, driver):
    request.cls.top = StoreTop(driver)


@pytest.fixture(scope='class')
def header(request, driver):
    request.cls.header = StoreHeader(driver)


@pytest.fixture(scope='class')
def footer(request, driver):
    request.cls.footer = StoreFooter(driver)


@pytest.fixture(scope='class')
def navbar(request, driver):
    request.cls.navbar = StoreNavbar(driver)


@pytest.fixture(scope='class')
def breadcrumb(request, driver):
    request.cls.breadcrumb = StoreBreadcrumb(driver)


@pytest.fixture(scope='class')
def thumbnails(request, driver):
    request.cls.thumbnails = StoreProductThumbnails(driver)


@pytest.fixture(scope='class')
def menu_product(request, driver):
    request.cls.menu_product = StoreMenuProduct(driver)


@pytest.fixture(scope='class')
def menu_account(request, driver):
    request.cls.menu_account = StoreMenuAccount(driver)
