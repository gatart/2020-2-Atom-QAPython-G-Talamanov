from ui.fixtures import *

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from api.client import ApiClient


@pytest.mark.ui
@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://target.my.com/')
    browser.maximize_window()
    yield browser
    browser.close()
    browser.quit()


@pytest.mark.api
@pytest.fixture(scope='function')
def api_client():
    user = 'talamanov01@mail.ru'
    password = 'qwerty123456'

    return ApiClient(user, password)
