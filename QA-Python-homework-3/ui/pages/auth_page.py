from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.locators import locators


class AuthPage(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        self.find(locator, timeout)
        element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        element.click()

    def input(self, put, locator):
        field = self.find(locator)
        field.clear()
        field.send_keys(put)
        return field

    def auth(self, login, password):
        self.click(locators.AuthPageLocators.BUTTON_LOCATOR)
        self.input(login, locators.AuthPageLocators.LOGIN_LOCATOR)
        element = self.input(password, locators.AuthPageLocators.PASSWORD_LOCATOR)
        element.send_keys(Keys.RETURN)

    def wait(self, timeout=None):

        if timeout is None:
            timeout = 10

        return WebDriverWait(self.driver, timeout)
