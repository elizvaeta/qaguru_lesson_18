from helpers.cart_api import cart_api
from pages.cart_page import cart


def test_cart_should_have_item(cookie_customer):
    cart.set_cookie(cookie_customer=cookie_customer)
    cart_api.add_product(product_id=31, cookie_customer=cookie_customer)

    cart.open_page()

    cart.should_have_items('14.1-inch Laptop')


def test_cart_should_have_many_items(cookie_customer):
    cart.set_cookie(cookie_customer=cookie_customer)
    cart_api.add_product(product_id=31, cookie_customer=cookie_customer)
    cart_api.add_product(product_id=13, cookie_customer=cookie_customer)

    cart.open_page()

    cart.should_have_items('14.1-inch Laptop', 'Computing and Internet')
