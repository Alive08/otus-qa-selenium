import pytest
from pom.register_account_page import RegisterAccountPage, RegisterAccountPageLocators


@pytest.fixture(scope='class', autouse=True)
def page(request, driver, base_url):
    request.cls.page = RegisterAccountPage(driver)
    request.cls.page.url = f'{base_url}/{RegisterAccountPageLocators.URL_REGISTER_ACCOUNT}'
    request.cls.page.open()


@pytest.mark.usefixtures('top', 'header', 'menu_account')
class TestRegisterAccountPage:

    def test_go_to_register_from_main_page(self):
        self.header.click_logo()
        self.top.menu.REGISTER
        assert self.page.at_page(
            RegisterAccountPageLocators.TITLE_REGISTER_ACCOUNT)

    def test_read_privacy_policy(self):
        self.page.click_privacy_policy()
        self.page.close_privacy_policy()

    def test_check_agree(self):
        self.page.check_box_agree()
        assert self.page.is_checked_agree()
        self.page.uncheck_box_agree()
        assert not self.page.is_checked_agree()

    def test_submit_form_duplicate_data(self, account_valid):
        self.page.submit_form(account_valid)
        assert self.page.does_present(self.page.locator.LOCATOR_ALERT_DANGER)

    def test_submit_form_random_data(self, account_random):
        account_random.password_2 = account_random.password_1
        self.page.submit_form(account_random)
        assert self.page.does_not_present(
            self.page.locator.LOCATOR_ALERT_DANGER)
        self.menu_account.LOGOUT

    def test_submit_form_privacy_policy_unchecked(self, account_random):
        account_random.password_2 = account_random.password_1
        self.page.submit_form(account_random, agree=False)
        assert self.page.does_present(self.page.locator.LOCATOR_ALERT_DANGER)

    @pytest.mark.parametrize('field, expected', (('fname', RegisterAccountPageLocators.TEXT_FIRST_NAME_ERROR),
                                                 ('lname', RegisterAccountPageLocators.TEXT_LAST_NAME_ERROR),
                                                 ('email', RegisterAccountPageLocators.TEXT_EMAIL_ERROR),
                                                 ('phone', RegisterAccountPageLocators.TEXT_TELEPHONE_ERROR),
                                                 ('password_1', RegisterAccountPageLocators.TEXT_PASSWORD_ERROR)))
    def test_try_register_account_with_errors(self, account_random, field, expected):
        setattr(account_random, field, '')
        self.page.submit_form(account_random)
        assert expected in self.page.page_src

    def test_register_passwords_mismatch(self, account_random):
        account_random.password_2 = ''
        self.page.submit_form(account_random)
        assert RegisterAccountPageLocators.TEXT_PASSWORDS_MISMATCH in self.page.page_src
