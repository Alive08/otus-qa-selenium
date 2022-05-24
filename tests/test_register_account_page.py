from time import sleep
import pytest
from frame.base_page import BASE_URL
from pom.store.register_account_page import RegisterAccountPage, RegisterAccountPageLocators
from pom.store.main_page import MainPage, MainPageLocators
from pom.element.store.common import CommonElements
from pom.element.store.account_dropdown import account_dropdown


@pytest.fixture(scope='class', autouse=True)
def page(request, driver):
    request.cls.driver = driver
    request.cls.url = RegisterAccountPageLocators.URL
    request.cls.page = RegisterAccountPage(driver, request.cls.url)
    return request.cls.page


class TestRegisterAccountPage:

    def test_go_to_register_from_main_page(self, page):
        page.go(BASE_URL)
        page.click(account_dropdown)
        page.click(account_dropdown.register)
        assert self.page.at_page(
            RegisterAccountPageLocators.TITLE_REGISTER_ACCOUNT)

    def test_read_privacy_policy(self, page):
        page.click_privacy_policy()
        page.close_privacy_policy()

    def test_check_agree(self, page):
        page.check_box_agree()
        assert page.is_checked_agree()
        page.uncheck_box_agree()
        assert not page.is_checked_agree()

    def test_submit_form_duplicate_data(self, page, account_valid):
        page.submit_form(account_valid)
        assert page.does_present(page.locator.LOCATOR_ALERT_DANGER)

    def test_submit_form_random_data(self, page, account_random):
        account_random.password_2 = account_random.password_1
        page.submit_form(account_random)
        page.click(account_dropdown)
        assert 'Your Account Has Been Created!' in page.page_src
        page.click(account_dropdown.logout)

    def test_submit_form_privacy_policy_unchecked(self, page, account_random):
        account_random.password_2 = account_random.password_1
        page.submit_form(account_random, agree=False)
        assert page.does_present(page.locator.LOCATOR_ALERT_DANGER)

    @pytest.mark.parametrize('field, expected', (('fname', RegisterAccountPageLocators.TEXT_FIRST_NAME_ERROR),
                                                 ('lname', RegisterAccountPageLocators.TEXT_LAST_NAME_ERROR),
                                                 ('email', RegisterAccountPageLocators.TEXT_EMAIL_ERROR),
                                                 ('phone', RegisterAccountPageLocators.TEXT_TELEPHONE_ERROR),
                                                 ('password_1', RegisterAccountPageLocators.TEXT_PASSWORD_ERROR)))
    def test_try_register_account_with_errors(self, page, account_random, field, expected):
        setattr(account_random, field, '')
        page.submit_form(account_random)
        assert expected in page.page_src

    def test_register_passwords_mismatch(self, page, account_random):
        account_random.password_2 = ''
        page.submit_form(account_random)
        assert page.locator.TEXT_PASSWORDS_MISMATCH in page.page_src
