import pytest
from pom.admin.login_page import AdminLoginPage, AdminLoginPageLocators


@pytest.fixture(scope='class', autouse=True)
def page(request, driver, base_url):
    request.cls.page = AdminLoginPage(driver)
    request.cls.page.url = f'{base_url}/{AdminLoginPageLocators.URL_ADMIN_LOGIN_PAGE}'
    request.cls.page.open()


class TestAdminLoginPage:

    def test_if_at_page(self):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)

    @pytest.mark.parametrize('login,password,expected', (('user', 'bitnami', AdminLoginPageLocators.TITLE_ADMIN_PAGE),
                                                         ('user', 'bitnomi', AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)),
                             ids=('SUCCESS', 'FAIL'))
    def test_admin_login(self, login, password, expected):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        self.page.enter_login(login)
        self.page.enter_password(password)
        self.page.click_on_login_button()
        assert self.page.at_page(expected)

    def test_admin_login_successful(self, valid_creds):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        self.page.enter_login(valid_creds.login)
        self.page.enter_password(valid_creds.password)
        self.page.click_on_login_button()
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_PAGE)

    def test_admin_login_failed(self, invalid_creds):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        self.page.enter_login(invalid_creds.login)
        self.page.enter_password(invalid_creds.password)
        self.page.click_on_login_button()
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        assert self.page.find_element(
            AdminLoginPageLocators.LOCATOR_ALERT_DANGER_MESSAGE)
        self.page.click_on_close_alert_button()
        assert self.page.does_not_present(
            AdminLoginPageLocators.LOCATOR_ALERT_DANGER_MESSAGE)

    def test_admin_reset_password_cancel(self):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        self.page.click_on_forgotten_password_link()
        assert self.page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        self.page.click_on_forgotten_password_cancel_button()
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)

    def test_admin_reset_password_submit_invalid_email(self):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        self.page.click_on_forgotten_password_link()
        assert self.page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        self.page.enter_email('user@otus.ru')
        self.page.click_on_forgotten_password_reset_button()
        assert self.page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        assert self.page.find_element(
            AdminLoginPageLocators.LOCATOR_ALERT_DANGER_MESSAGE)
        self.page.click_on_close_alert_button()
        self.page.click_on_forgotten_password_cancel_button()

    def test_admin_reset_password_submit_valid_email(self):
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        self.page.click_on_forgotten_password_link()
        assert self.page.at_page(
            AdminLoginPageLocators.TITLE_FORGOTTEN_PASSWORD_PAGE)
        self.page.enter_email('user@example.com')
        self.page.click_on_forgotten_password_reset_button()
        assert self.page.at_page(AdminLoginPageLocators.TITLE_ADMIN_LOGIN_PAGE)
        assert self.page.find_element(
            AdminLoginPageLocators.LOCATOR_ALERT_SUCCESS_MESSAGE)
        self.page.click_on_close_alert_button()
        assert self.page.does_not_present(
            AdminLoginPageLocators.LOCATOR_ALERT_SUCCESS_MESSAGE)
