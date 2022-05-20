from frame.base_page import BasePage
from frame.common_locators import *
from pom.shared.store.navbar import Navbar


class MainPage(BasePage):

    # locators

    class slideshow:
        link = (css, "#slideshow0")
        next = (css, ".slideshow .swiper-button-next")
        prev = (css, ".slideshow .swiper-button-prev")

    class featured:
        link = (css, "#featured")

    class carousel:
        link = (css, "#carousel0")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.navbar = Navbar
        self.driver.get(self.url)


if __name__ == '__main__':

    for i in Navbar.items:
        print(Navbar.item_name(i))
        print('---')
        for p in i.items:
            print(i.item_name(p))
