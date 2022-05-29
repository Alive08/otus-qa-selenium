import pytest
from frame.base_page import Currency
from pom.element.store.account import account
from pom.element.store.account_dropdown import account_dropdown
from pom.element.store.currency import currency
from pom.element.store.navbar import navbar
from pom.element.store.thumbnails import ProductThumbnails
from pom.store.account_login_page import AccountLoginPage
from pom.store.account_page import AccountPage, AccountPageLocators
from pom.store.main_page import MainPage, MainPageLocators
from pom.store.register_account_page import (RegisterAccountPage,
                                             RegisterAccountPageLocators)

from tests.conftest import AccountData


class TestUserScenarios:

    @pytest.mark.parametrize('cur', (c.name for c in Currency))
    def test_change_currency(self, driver, cur):
        page = MainPage(driver, MainPageLocators.URL)
        page.open()
        page.click(currency.button)
        page.click(getattr(currency, cur.lower()))
        assert page.find_element(currency.selected).text == Currency[cur].value
        page.click(navbar.tablets)
        assert page.at_page('Tablets')
        tn = ProductThumbnails(driver)
        assert tn.get_price_currency(tn.get_product(0)) == Currency[cur].value

    def test_register_user_account(self, driver, account_random: AccountData):
        page = RegisterAccountPage(driver, RegisterAccountPageLocators.URL)
        page.open()
        account_random.password_2 = account_random.password_1  # valid input
        page.submit_form(account_random, agree=True)
        assert page.at_page(RegisterAccountPageLocators.TEXT_ACCOUNT_CREATED)
        page.click(account.logout)
        AccountPage(driver).click_continue()
        assert page.at_page(MainPageLocators.TITLE_MAIN_PAGE)

    def test_user_login_and_logout(self, driver, account_valid: AccountData):
        page = MainPage(driver, MainPageLocators.URL)
        page.open()
        page.click(account_dropdown)
        page.click(account_dropdown.login)
        AccountLoginPage(driver).login_with(
            account_valid.email, account_valid.password_1)
        assert page.at_page(AccountPageLocators.TITLE)
        page.click(account_dropdown)
        page.click(account_dropdown.logout)
        AccountPage(driver).click_continue()
        assert page.at_page(MainPageLocators.TITLE_MAIN_PAGE)
