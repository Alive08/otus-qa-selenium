from frame.common_locators import *


class breadcrumb:
    link = (css, "ul.breadcrumb")
    item = (css, "ul.breadcrumb > * a")
    home = (css, "ul.breadcrumb > * a[href$='common/home']")
