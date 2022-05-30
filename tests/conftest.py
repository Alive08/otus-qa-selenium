import random
from collections import namedtuple
from dataclasses import dataclass

import pytest
from faker import Faker
from frame.browser import Browser
from frame.utils import Utils
from pom.element.store.product import product
from pom.store.register_account_page import RegisterAccountPage, RegisterAccountPageLocators
from pom.element.store.account import account

# BASE_URL = f"http://{Utils.get_ip()}:8081"

BASE_URL = 'http://127.0.0.1:8081'

MAX_TIMEOUT = 5

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
    driver.implicitly_wait(MAX_TIMEOUT)

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


@pytest.fixture(scope='session')
def account_valid(driver):
    data = AccountData('Denzel', 'Washington',
                       'denzel.washington@holliwood.com',
                       '+1 234 5678 90',
                       'helloUser', 'helloUser')
    page = RegisterAccountPage(driver, RegisterAccountPageLocators.URL)
    page.open()
    page.submit_form(data, agree=True)
    try:
        page.click(account.logout, time=0.25)
    except:
        pass
    return data


@pytest.fixture
def account_random():
    faker = Faker()
    return AccountData(
        fname=faker.first_name(),
        lname=faker.last_name(),
        email=faker.email(),
        phone=faker.phone_number(),
        password_1=faker.password(),
        password_2=faker.password()
    )


@dataclass
class ProductData:
    name: str
    description: str
    meta_tag_title: str
    model: str
    price: int
    quantity: int
    manufacturer: str
    categories: str


@pytest.fixture
def product_random():
    faker = Faker()
    return ProductData(
        name=faker.word(),
        description=faker.paragraph(),
        meta_tag_title=faker.pystr(),
        model=faker.word(),
        price=faker.pyint(),
        quantity=faker.pyint(),
        manufacturer='None',
        categories=random.choice(product.item_names)
    )


@pytest.fixture(autouse=True)
def back_to_base(request, base_url):
    yield
    try:
        request.instance.driver.get(base_url + request.instance.url)
    except:
        pass


@pytest.fixture(scope='session')
def account_admin_valid():
    return ('user', 'bitnami')
