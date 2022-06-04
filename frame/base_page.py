from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from frame.base_locator import Locator, Selector, BaseLocator
from frame.utils import Utils

TIMEOUT_MESSAGE = "Can't find element(s) by locator {} in {} s"
TIMEOUT = 3

BASE_URL = f'http://{Utils.get_ip()}:8081'

# BASE_URL = 'http://127.0.0.1:8081'


class Currency(Enum):
    USD = '$'
    EUR = '€'
    GBP = '£'


class BasePage:

    locator = BaseLocator

    def __init__(self, driver, url='', open=False):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.url = BASE_URL + url
        self.__wait = lambda timeout=TIMEOUT: WebDriverWait(
            driver, timeout=timeout)
        if open:
            self.open()

    @property
    def locators(self):
        return [p for p in self.locator.__dict__.items() if p[0].startswith('LOCATOR_')]

    @property
    def title(self):
        return self.driver.title

    @property
    def page_src(self):
        return self.driver.page_source

    @property
    def current_url(self):
        return self.driver.current_url

    def go(self, url):
        return self.driver.get(url)

    def open(self):
        return self.driver.get(self.url)

    def at_page(self, title):
        return self.driver.title == title

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
        return element

    def enter_text_with_dropdown(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.click()
        element.send_keys(text)
        try:
            # handle input with a dropdown
            self.click(Selector(By.PARTIAL_LINK_TEXT, text))
        except:
            element.clear()
        return element

    def click(self, locator, time=TIMEOUT):
        try:
            locator = locator.self
        except:
            pass
        self.__wait(time).until(EC.element_to_be_clickable(locator)).click()

    def hover(self, locator, time=TIMEOUT):
        try:
            locator = locator.self
        except:
            pass
        element = self.find_element(locator, time)
        self.actions.move_to_element(element).perform()
        return element

    def click_element(self, element):
        element.click()

    def find_element(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.presence_of_element_located(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def find_elements(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.presence_of_all_elements_located(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def is_visible(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.visibility_of_element_located(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def are_visible(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.visibility_of_all_elements_located(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def is_not_visible(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.invisibility_of_element_located(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def does_present(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.presence_of_element_located(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def does_not_present(self, locator, time=0.2):
        try:
            self.does_present(locator, time=time)
        except TimeoutException:
            return True
        else:
            return False

    def is_clickable(self, locator, time=TIMEOUT):
        return self.__wait(time).until(EC.element_to_be_clickable(locator),
                                       message=TIMEOUT_MESSAGE.format(locator, time))

    def does_alert_present(self, time=0.5):
        return self.__wait(time).until(EC.alert_is_present())

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to_alert().dismiss()
