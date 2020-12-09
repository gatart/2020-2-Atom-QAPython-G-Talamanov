from ui.pages.auth_page import AuthPage
from ui.locators import locators
from selenium.common.exceptions import TimeoutException


class SegmentPage(AuthPage):
    def create(self, name):
        self.click(locators.SegmentLocators.SEGMENT_LOCATOR, timeout=10)

        try:  # Комп долго грузит страницу, поэтому timeout=30
            self.click(locators.SegmentLocators.CREATE_LOCATOR_1, timeout=20)
        except TimeoutException:
            self.click(locators.SegmentLocators.CREATE_LOCATOR_2)
            self.click(locators.SegmentLocators.TYPE_LOCATOR)

        self.click(locators.SegmentLocators.CHECKBOX_LOCATOR)
        self.click(locators.SegmentLocators.BUTTON_1_LOCATOR)
        self.input(name, locators.SegmentLocators.NAME_LOCATOR)
        self.click(locators.SegmentLocators.BUTTON_2_LOCATOR)

