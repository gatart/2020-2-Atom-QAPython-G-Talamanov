import pytest

from ui.pages.auth_page import AuthPage
from ui.pages.company_page import CompanyPage
from ui.pages.segment_page import SegmentPage


@pytest.mark.ui
@pytest.fixture
def auth_page(driver):
    return AuthPage(driver=driver)


@pytest.mark.ui
@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.mark.ui
@pytest.fixture
def company_page(driver):
    return CompanyPage(driver=driver)


@pytest.mark.ui
@pytest.fixture(scope='function')
def auto_auth(auth_page):
    auth_page.auth("talamanov01@mail.ru", "qwerty123456")
    return auth_page.driver
