from pom.admin.admin_page import AdminPage
from pom.admin.login_page import AdminLoginPage, AdminLoginPageLocators
from pom.admin.product_page import AdminProductPage
from pom.element.admin.common import AdminCommonElements
from pom.element.admin.navigation import navigation

from tests.conftest import ProductData
import time

class TestAdminScenarios:

    def test_add_product(self, driver, account_admin_valid, product_random: ProductData):
        AdminLoginPage(driver, AdminLoginPageLocators.URL,
                       open=True).admin_login_with(*account_admin_valid)
        admin_page = AdminPage(driver)
        product_page = AdminProductPage(driver)
        admin_page.click(navigation.catalog)
        admin_page.click(navigation.catalog.products)
        admin_page.click_add()

        admin_page.click_tab('General')
        product_page.set_product_name(f'test_{product_random.name}')
        product_page.set_product_description(product_random.description)
        product_page.set_meta_tag_title(product_random.name)

        admin_page.click_tab('Data')
        product_page.set_product_model(product_random.name)
        product_page.set_product_price(product_random.price)
        product_page.set_product_quantity(product_random.quantity)

        admin_page.click_tab('Links')
        product_page.set_product_category(
            product_random.categories.capitalize())
        product_page.set_product_manufacturer(product_random.manufacturer)

        admin_page.click_save()

        assert admin_page.does_present_alert_success()
        admin_page.close_alert()
        AdminCommonElements(driver).click_logout()

    def test_delete_product(self, driver, account_admin_valid):
        AdminLoginPage(driver, AdminLoginPageLocators.URL,
                       open=True).admin_login_with(*account_admin_valid)
        admin_page = AdminPage(driver)
        product_page = AdminProductPage(driver)

        admin_page.click(navigation.catalog)
        admin_page.click(navigation.catalog.products)

        product_page.set_filter_name('test_')
        product_page.click_filter()
        products = product_page.get_products()
        if products:
            for p in products:
                product_page.select_product(p)
            admin_page.click_delete()
            if admin_page.does_alert_present():
                admin_page.alert_accept()

        assert admin_page.does_present_alert_success()
        admin_page.close_alert()
        AdminCommonElements(driver).click_logout()
