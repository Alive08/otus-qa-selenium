from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT_MESSAGE = "Can't find element(s) by locator {} in {} s"
TIMEOUT = 3


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.__wait = lambda timeout=TIMEOUT: WebDriverWait(
            driver, timeout=timeout)

    @property
    def title(self):
        return self.driver.title

    @property
    def page_src(self):
        return self.driver.page_source

    @property
    def current_url(self):
        return self.driver.current_url

    def open(self):
        return self.driver.get(self.url)

    def at_page(self, title):
        return self.driver.title == title

    def go(self, url):
        return self.driver.get(url)

    def back(self):
        return self.driver.back()

    def forward(self):
        return self.driver.forward()

    def refresh(self):
        return self.driver.refresh()

    def click(self, locator):
        try:
            locator = locator.link
        except:
            pass
        self.driver.find_element(*locator).click()

    def hover(self, locator):
        try:
            locator = locator.link
        except:
            pass
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).perform()
        return element

    def input_enter_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

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
