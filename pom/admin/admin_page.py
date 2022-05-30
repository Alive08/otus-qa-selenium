from selenium.webdriver.common.by import By
from frame.base_page import BasePage
from frame.node import Node
from frame.base_locator import BaseLocator, Selector


class AdminPageLocators(BaseLocator):

    LOCATOR_ADD = Selector(By.CSS_SELECTOR, "a[data-original-title='Add New']")
    LOCATOR_COPY = Selector(
        By.CSS_SELECTOR, "button[data-original-title='Copy'")
    LOCATOR_DELETE = Selector(
        By.CSS_SELECTOR, "button[data-original-title='Delete']")
    LOCATOR_SAVE = Selector(
        By.CSS_SELECTOR, "button[data-original-title='Save']")
    LOCATOR_CANCEL = Selector(
        By.CSS_SELECTOR, "a[data-original-title='Cancel']")
    LOCATOR_ALERT_DANGER_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    LOCATOR_ALERT_SUCCESS_MESSAGE = Selector(
        By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
    LOCATOR_BUTTON_ALERT_CLOSE = Selector(By.CSS_SELECTOR, "button.close")

    class tabs(Node):
        general = (By.LINK_TEXT, 'General')
        data = (By.LINK_TEXT, 'Data')
        links = (By.LINK_TEXT, 'Links')
        attribute = (By.LINK_TEXT, 'Attribute')
        option = (By.LINK_TEXT, 'Option')
        recurring = (By.LINK_TEXT, 'Recurring')
        discount = (By.LINK_TEXT, 'Discount')
        special = (By.LINK_TEXT, 'Special')
        image = (By.LINK_TEXT, 'Image')
        reward_points = (By.LINK_TEXT, 'Reward Points')
        seo = (By.LINK_TEXT, 'SEO')
        design = (By.LINK_TEXT, 'Design')


class AdminPage(BasePage):

    locator = AdminPageLocators

    def click_add(self):
        self.click(self.locator.LOCATOR_ADD)

    def click_copy(self):
        self.click(self.locator.LOCATOR_COPY)

    def click_delete(self):
        self.click(self.locator.LOCATOR_DELETE)

    def click_save(self):
        self.click(self.locator.LOCATOR_SAVE)

    def click_tab(self, tab):
        self.click(self.locator.tabs.get_item_by_name(tab.lower()))

    def does_present_alert_danger(self):
        return self.does_present(self.locator.LOCATOR_ALERT_DANGER_MESSAGE)

    def does_not_present_alert_danger(self):
        return self.does_not_present(self.locator.LOCATOR_ALERT_DANGER_MESSAGE)

    def does_present_alert_success(self):
        return self.does_present(self.locator.LOCATOR_ALERT_SUCCESS_MESSAGE)

    def does_not_present_alert_success(self):
        return self.does_not_present(self.locator.LOCATOR_ALERT_SUCCESS_MESSAGE)

    def close_alert(self):
        self.click(self.locator.LOCATOR_BUTTON_ALERT_CLOSE)
