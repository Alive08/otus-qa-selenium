from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from frame.base_locator import Locator, Selector, BaseLocator, Click

TIMEOUT_MESSAGE = "Can't find element(s) by locator {} in {} s"
TIMEOUT = 3
DEFAULT_URL = 'http://127.0.0.1:8081'


class BasePage:

    locator = BaseLocator

    def __init__(self, driver, url=DEFAULT_URL):
        self.driver = driver
        self.url = url
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

    def input_enter_text(self, locator, text):
        element = self.find_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
        return element

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


class BaseMenu(BasePage):

    locator = BaseLocator

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.click = Click(self)

    def __getattr__(self, attr):
        return self.click_item(self.locator.mapper(attr).locator)

    def find_item(self, selector):
        return self.find_nested_item(selector, self.locator.root)

    def click_item(self, selector):
        self.click_nested_item(selector, self.locator.root)

    def find_nested_item(self, selector: Selector, top: Selector) -> Locator:
        parent = None
        l = self.locator.find_by_selector(selector.selector)
        if l:
            parent = self.locator.find_by_name(l.name.rsplit('_', 1).pop(0))
            # if parent:
            #     if parent.locator == top:
            #         parent = None
        return parent, l

    def click_nested_item(self, selector, top):
        parent, l = self.find_nested_item(selector, top)
        if parent:
            self.find_element(parent.locator).click()
        self.find_element(l.locator).click()

    def find_nested_element(self, text, top):
        _, l = self.find_nested_item(text, top)
        return self.find_element(l.locator)
