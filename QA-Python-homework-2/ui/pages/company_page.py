import os
import time
from ui.pages.auth_page import AuthPage

from ui.locators import locators


class CompanyPage(AuthPage):
    def create(self, name):
        self.click(locators.CompanyLocators.COMPANY_BUTTON, timeout=20)
        self.click(locators.CompanyLocators.TYPE_LOCATOR)
        self.input("test.com", locators.CompanyLocators.LINK_LOCATOR)
        self.click(locators.CompanyLocators.FORMAT_LOCATOR)
        el = self.find(locators.CompanyLocators.UPLOAD)
        time.sleep(10)
        path = os.path.join('\\', 'c:\\', 'PyCharm', 'technoatom-qa-python', '2020-2-Atom-QAPython-G-Talamanov',
                            'QA-Python-homework-2', 'data', 'Smisol.jpg')
        el.send_keys(path)

        self.click(locators.CompanyLocators.LOAD_BUTTON)
        self.input(name, locators.CompanyLocators.COMPANY_NAME)
        self.click(locators.CompanyLocators.MAKE_BUTTON)
