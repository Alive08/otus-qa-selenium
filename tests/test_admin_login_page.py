import pytest
from pom.admin.login_page import AdminLoginPage, AdminLoginPageLocators


@pytest.fixture(scope='class', autouse=True)
def page(request, driver):
    request.cls.driver = driver
    request.cls.url = AdminLoginPageLocators.URL
    page = AdminLoginPage(driver, request.cls.url)
    page.open()
    return page


class TestAdminLoginPage:

    def test_if_at_page(self, page):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)

    @pytest.mark.parametrize('login,password,expected', (('user', 'bitnami', AdminLoginPageLocators.TITLE_ADMIN_PAGE),
                                                         ('user', 'bitnomi', AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)),
                             ids=('SUCCESS', 'FAIL'))
    def test_admin_login(self, login, password, expected, page: AdminLoginPage):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        page.admin_login_with(login, password)
        assert page.at_page(expected)

    def test_admin_login_successful(self, valid_creds, page: AdminLoginPage):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        page.admin_login_with(*valid_creds)
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_PAGE)

    def test_admin_login_failed(self, invalid_creds, page: AdminLoginPage):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        page.admin_login_with(*invalid_creds)
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        assert page.does_present_alert_danger()
        page.close_alert()
        assert page.does_not_present_alert_danger()

    def test_admin_reset_password_cancel(self, page: AdminLoginPage):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        page.click_forgotten_password_link()
        assert page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        page.click_forgotten_password_cancel_button()
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)

    def test_admin_reset_password_submit_invalid_email(self, page: AdminLoginPage):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        page.click_forgotten_password_link()
        assert page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        page.enter_email('user@otus.ru')
        page.click_forgotten_password_reset_button()
        assert page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        assert page.does_present_alert_danger()
        page.close_alert()
        page.click_forgotten_password_cancel_button()

    def test_admin_reset_password_submit_valid_email(self, page: AdminLoginPage):
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        page.click_forgotten_password_link()
        assert page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        page.enter_email('user@example.com')
        page.click_forgotten_password_reset_button()
        assert page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        assert page.does_present_alert_success()
        page.close_alert()
        assert page.does_not_present_alert_success()
