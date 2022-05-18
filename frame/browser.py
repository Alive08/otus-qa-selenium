from enum import Enum

from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager

DRIVER_PATH = '/home/user/Downloads/webdrivers'

COMMON_OPTIONS = ('--no-sandbox', '--disable-infobars',
                  '--disable-extensions', '--disable-gpu')


class BaseBrowser:

    def __init__(self, options=None):
        self._set_options(options)

    # set common options for different browsers
    def _set_options(self, options):
        for option in *COMMON_OPTIONS, *options:
            self._options.add_argument(option)


class BrowserChrome(BaseBrowser):

    def __init__(self, options=None):
        self._options = ChromeOptions()
        super().__init__(options)

    def __call__(self):
        return webdriver.Chrome(
            service=ChromeService(
                ChromeDriverManager().install()),
            options=self._options)


class BrowserFirefox(BaseBrowser):

    def __init__(self, options=None):
        self._options = FirefoxOptions()
        super().__init__(options)

    def __call__(self):
        return webdriver.Firefox(
            service=FirefoxService(
                GeckoDriverManager().install()),
            options=self._options)

class BrowserEdge(BaseBrowser):

    def __init__(self, options=None):
        self._options = EdgeOptions()
        super().__init__(options)

    def __call__(self):
        return webdriver.Edge(
            service=EdgeService(
                EdgeChromiumDriverManager().install()),
            options=self._options)

class BrowserOpera(BaseBrowser):

    def __init__(self, options=None):
        self._options = ChromeOptions()
        super().__init__(options)
        self._options.binary_location = '/snap/opera/current/usr/bin/opera'
        # https://github.com/operasoftware/operachromiumdriver/issues/96
        self._options.add_experimental_option('w3c', True)

    def __call__(self):
        return webdriver.Opera(executable_path=OperaDriverManager().install(), options=self._options)


class BrowserYandex(BaseBrowser):

    def __init__(self, options=None):
        self._options = ChromeOptions()
        super().__init__(options)
        self._options.binary_location = '/opt/yandex/browser-beta/yandex-browser-beta'

    def __call__(self):
        return webdriver.Chrome(
            service=ChromeService(f'{DRIVER_PATH}/yandexdriver'),
            options=self._options)


class BROWSERS(Enum):
    chrome = BrowserChrome
    firefox = BrowserFirefox
    edge = BrowserEdge
    opera = BrowserOpera
    yandex = BrowserYandex


class Browser:

    def __init__(self, name, options=None):
        self.__name = name
        try:
            self.__browser = BROWSERS[name].value(options=options)
        except KeyError:
            raise AssertionError(f'Unsupported browser: {self.__name}')

    def __call__(self, *args, **kwargs):
        return self.__browser(*args, **kwargs)
