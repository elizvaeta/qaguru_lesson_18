import allure
import requests
from allure_commons.types import AttachmentType

from tests.conftest import BASE_URL


class CartApi:

    def add_product(self, product_id, cookie_customer):
        url = BASE_URL + f'/addproducttocart/catalog/{product_id}/1/1'

        cookies = {
            'Nop.customer': cookie_customer
        }

        with allure.step(f'Добавление товара {product_id} в корзину'):
            response = requests.post(
                url=url,
                cookies=cookies
            )

            print(response.json())

            allure.attach(
                body=response.content,
                name='API: add product to cart',
                attachment_type=AttachmentType.TEXT
            )


cart_api = CartApi()
