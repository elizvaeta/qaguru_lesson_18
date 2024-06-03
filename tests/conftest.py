import allure
import pytest
import requests
from selene import browser

BASE_URL = 'https://demowebshop.tricentis.com'


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser.config.base_url = BASE_URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def cookie_customer():
    with allure.step('Получение cookie посетителя'):
        response = requests.get(url=BASE_URL)
        cookie_customer = response.cookies.get('Nop.customer')

    yield cookie_customer
