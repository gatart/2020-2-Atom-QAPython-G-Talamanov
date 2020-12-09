import pytest
from selenium.webdriver.common.keys import Keys
from ui.locators import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from base import BaseCase


@pytest.mark.ui
class TestAuth(BaseCase):
    @pytest.mark.skip(reason='no need')
    def test_good_auth(self):
        self.auth_page.auth('talamanov01@mail.ru', 'qwerty123456')
        wait = WebDriverWait(self.driver, timeout=12)
        wait.until(EC.presence_of_element_located(locators.AuthPageLocators.AUTH_LOCATOR))
        wait.until(EC.visibility_of_element_located(locators.AuthPageLocators.AUTH_LOCATOR))

    @pytest.mark.skip(reason='no need')
    def test_bad_auth(self):
        self.auth_page.auth('talamanov01@mail.ru', 'hgfjhagjdfsd')
        assert "Invalid login or password" in self.driver.page_source


@pytest.mark.ui
class TestCompany(BaseCase):
    def test_creation(self, auto_auth):
        self.driver = auto_auth
        self.company_page.create("Company is who")
        self.company_page.find(locators.CompanyLocators.CHECK)


@pytest.mark.ui
class TestSegment(BaseCase):
    @pytest.mark.skip(reason='no need')
    def test_creation(self, auto_auth):
        self.driver = auto_auth
        self.segment_page.create("Super-puper-hyper-dooper section")
        self.segment_page.find(locators.SegmentLocators.SEGMENT_1)

    @pytest.mark.skip(reason='no need')
    def test_deletion(self, auto_auth):
        self.driver = auto_auth
        self.segment_page.create("Super-puper-puper-hyper-dooper section")
        element = self.segment_page.input("Super-puper-puper-hyper-dooper section", locators.SegmentLocators.SEARCH)
        element.send_keys(Keys.RETURN)
        self.segment_page.click(locators.SegmentLocators.LIST)
        self.segment_page.click(locators.SegmentLocators.DELETE_CHECKBOX_LOCATOR)
        self.segment_page.click(locators.SegmentLocators.ACTION_LOCATOR)
        self.segment_page.click(locators.SegmentLocators.DELETE_LOCATOR)
        with pytest.raises(TimeoutException):
            self.segment_page.find(locators.SegmentLocators.SEGMENT_2)
