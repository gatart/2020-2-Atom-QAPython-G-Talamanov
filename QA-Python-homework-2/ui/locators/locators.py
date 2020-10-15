from selenium.webdriver.common.by import By


class AuthPageLocators:
    BUTTON_LOCATOR = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
    LOGIN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    PASSWORD_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    AUTH_LOCATOR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[3]/div/div[1]')


class CompanyLocators:
    COMPANY_BUTTON = (By.XPATH, '//div[@class="button-module-textWrapper-3LNyYP"]')
    TYPE_LOCATOR = (By.XPATH, '//div[@cid="view567"]')
    LINK_LOCATOR = (By.XPATH, '//input[@placeholder="Введите ссылку"]')
    FORMAT_LOCATOR = (By.XPATH, '//*[@id="patterns_4"]/span')
    UPLOAD = (By.XPATH, '//input[@data-test="image_240x400"]')
    LOAD_BUTTON = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[3]/input')
    MAKE_BUTTON = (By.XPATH, '//div[2]/div[3]/div[1]/div[1]/button/div')
    COMPANY_NAME = (By.XPATH, '//input[@class="input__inp js-form-element"]')
    CHECK = (By.XPATH, ' //a[@title="Company is who"]')


class SegmentLocators:
    SEGMENT_LOCATOR = (By.XPATH, '//a[@href="/segments"]')
    CREATE_LOCATOR_2 = (By.XPATH, '//button[@class="button button_submit"]')
    CREATE_LOCATOR_1 = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    TYPE_LOCATOR = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[8]')
    CHECKBOX_LOCATOR = (By.XPATH, '//input[@class="adding-segments-source__checkbox js-main-source-checkbox"]')
    BUTTON_1_LOCATOR = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[5]/div[1]/button/div')
    NAME_LOCATOR = (By.XPATH, '//input[@maxlength="60" and @class="input__inp js-form-element" ] ')
    BUTTON_2_LOCATOR = (By.XPATH, '//div[@class="button__text"]')
    SEARCH = (By.XPATH, '//input[@placeholder="Поиск по названию или id..."]')
    LIST = (By.XPATH, '/html/body/div[6]/div/div/div/ul/li')
    DELETE_CHECKBOX_LOCATOR = (By.XPATH, '//input[@type="checkbox"]')
    ACTION_LOCATOR = (By.XPATH, '//div[@class="select-module-arrow-3jahBj"]')
    DELETE_LOCATOR = (By.XPATH, '//li[@title="Удалить"]')
    SEGMENT_1 = (By.XPATH, '//a[@title="Super-puper-hyper-dooper section"]')
    SEGMENT_2 = (By.XPATH, '//a[@title="Super-puper-puper-hyper-dooper section"]')
