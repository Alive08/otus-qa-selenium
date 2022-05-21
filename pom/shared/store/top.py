from frame.common_locators import *
from frame.node import Node


class top:

    link = (css, "#top")
    cart = (css, "a[title='Shopping Cart']")
    checkout = (css, "a[title='Checkout']")

    class currency:
        link = (css, "#form-currency")
        button = (css, "button.btn.btn-link.dropdown-toggle")
        selected = (css, "strong")

        class menu(Node):
            link = (css, "ul.dropdown-menu")
            usd = (css, "button[name=USD]")
            eur = (css, "button[name=EUR]")
            gbp = (css, "button[name=GBP]")

    class account(Node):

        link = (css, "a[title='My Account']")
        login = (link_text, "Login")
        register = (link_text, "Register")
        my_account = (link_text, "My Account")
        order_history = (link_text, "Order History")
        transactions = (link_text, "Transactions")
        downloads = (link_text, "Downloads")
        logout = (link_text, "Logout")
