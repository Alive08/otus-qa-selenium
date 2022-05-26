from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from frame.base_locator import Locator, Selector, BaseLocator, Click
from frame.utils import Utils

TIMEOUT_MESSAGE = "Can't find element(s) by locator {} in {} s"
TIMEOUT = 3
# BASE_URL = f'http://{Utils.get_ip()}:8081'

BASE_URL = 'http://127.0.0.1:8081'


class BasePage:

    locator = BaseLocator

    def __init__(self, driver, url=''):
        self.driver = driver
        self.url = BASE_URL + url
        self.__wait = lambda timeout=TIMEOUT: WebDriverWait(
            driver, timeout=timeout)

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
        ActionChains(self.driver).move_to_element(element).perform()
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

    def does_not_present(self, locator, time=TIMEOUT):
        return self.__wait(time).until_not(EC.presence_of_element_located(locator),
                                           message=TIMEOUT_MESSAGE.format(locator, time))
