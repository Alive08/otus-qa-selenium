from frame.common_locators import *


class header:

    link = (css, "body > header")
    logo = (css, "#logo")

    class search:
        input = (name, "search")
        button = (css, "button.btn.btn-default.btn-lg")

    class cart:
        button = (css, "#cart > button")
        empty = (css, "#cart > ul > li > p")
        not_empty = (css, "#cart-total")
