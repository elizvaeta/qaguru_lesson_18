import allure
from allure_commons.types import AttachmentType
from selene import browser, have


class Cart:

    def set_cookie(self, cookie_customer):
        browser.open('/')
        browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookie_customer})

    def open_page(self):
        browser.open('/cart')

    def should_have_items(self, *product_names):
        with allure.step('Открытие корзины с товарами'):
            allure.attach(
                body=browser.driver.get_screenshot_as_png(),
                name='FRONTEND: Cart screenshot',
                attachment_type=AttachmentType.PNG
            )

            for index, product_name in enumerate(product_names):
                browser.element(f'table.cart>tbody>tr:nth-child({index + 1})').element('.product-name').should(
                    have.text(product_name[index]))

    def should_be_empty(self):
        with allure.step('Открытие пустой корзины'):
            allure.attach(
                body=browser.driver.get_screenshot_as_png(),
                name='FRONTEND: Cart screenshot',
                attachment_type=AttachmentType.PNG
            )

            browser.element('.cart-qty').should(have.text('0'))


cart = Cart()
