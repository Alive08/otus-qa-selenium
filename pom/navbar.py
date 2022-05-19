from enum import Enum
from frame.browser import Browser
from frame.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


css = By.CSS_SELECTOR
id = By.ID
link_text = By.LINK_TEXT
plink_text = By.PARTIAL_LINK_TEXT


class Node:

    @classmethod
    @property
    def items(cls):
        return [getattr(cls, k) for k in cls.__dict__ if not k.startswith('_') and not k in ('items', 'link')]

    @classmethod
    @property
    def item_names(cls):
        return [k for k in cls.__dict__.keys() if not k.startswith('_') and not k in ('items', 'link')]


class Item:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class Navbar(Node):

    link = (css, '#menu')

    class desktops(Node):
        link = (link_text, 'Desktops')
        pc = (plink_text, 'PC')
        mac = (plink_text, 'Mac')
        all = (link_text, 'Show All Desktops')

    class laptops(Node):
        link = (link_text, 'Laptops & Notebooks')
        macs = (plink_text, 'Macs')
        windows = (plink_text, 'Windows')
        all = (link_text, 'Show All Laptops & Notebooks')

    class components(Node):
        link = (link_text, 'Components')
        mice = (plink_text, 'Mice and Trackballs')
        monitors = (plink_text, 'Monitors')
        printers = (plink_text, 'Printers')
        scanners = (plink_text, 'Scanners')
        webcameras = (plink_text, 'Web Cameras')
        all = (link_text, 'Show All Components')

    class tablets(Node):
        link = (link_text, 'Tablets')

    class software(Node):
        link = (link_text, 'Software')

    class phones(Node):
        link = (link_text, 'Phones & PDAs')

    class cameras(Node):
        link = (link_text, 'Cameras')

    class mp3(Node):
        link = (link_text, 'MP3 Players')


class Page:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.navbar = Navbar

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


if __name__ == '__main__':

    wd = Browser('chrome')()
    wd.get('http://127.0.0.1:8081')

    p = Page(wd)

    # for i in Navbar.items:
    #     p.click(i)
    #     for j in i.items:
    #         p.hover(i)
    #         p.click(j)

    l = [(i,j) for i in Navbar.items for j in i.items] + [i for i in Navbar.items]
    for item in l:
        print(item)

    # wd.quit()
