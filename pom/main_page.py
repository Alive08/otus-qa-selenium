from frame.base_page import BasePage
from frame.common_locators import *
from pom.shared.store.header import header
from pom.shared.store.navbar import navbar
from pom.shared.store.top import top


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
        self.navbar = navbar
        self.top = top
        self.header = header
        self.open()


if __name__ == '__main__':

    for i in navbar.items:
        print(navbar.item_name(i))
        print('---')
        for p in i.items:
            print(i.item_name(p))
