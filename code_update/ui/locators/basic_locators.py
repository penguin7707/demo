from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    LOGIN_EMAIL = (By.NAME, 'email')
    LOGIN_PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON2_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')


class MainPage:
    SEGMENTS = (By.XPATH, '//a[contains(@href, "/segments")]')
    DASHBOARD = (By.XPATH, '//a[contains(@href, "/dashboard")]')


class SegmentPage:
    CREATE_BUTTON1 = (By.XPATH, '//a[contains(@href, "/segments/segments_list/new")]')
    CREATE_BUTTON2 = (By.XPATH, '//div[contains(@class, "button_")]')
    SEGMENT_TYPE = (By.XPATH, '//div[contains(@class, "block-left")]/div[.="Приложения и игры в соцсетях"]')
    MORE_BUTTON = (By.XPATH, '//div[contains(@class, "expand")]')
    PAID_BUTTON = (By.XPATH, '//span[contains(@data-loc-ru, "Платившие")]')
    ADD_SEGMENT = (By.XPATH, '//div[contains(@class ,"adding-segments-modal__btn-wrap")]/button[contains(@class, '
                             '"submit")]/div')
    SEGMENT_NAME = (By.XPATH, '//div[contains(@class, "input_create-segment-form")]/div/input')
    CREATE_SEGMENT = (By.XPATH, '//div[contains(@class, "button__")]')
    DO_BUTTON = (By.XPATH, '//div[contains(@class, "segmentsTable-module")]/span[contains(@class, '
                           '"select-module-itemInner")]')
    DELETE_BUTTON = (By.XPATH, '//li[contains(@title, "Удалить")]')


class DashboardPage:
    CREATE_DASHBOARD = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]/div/div')
    TRAFFIC = (By.XPATH, '// div[contains(@class, "traffic")] ')
    URL = (By.XPATH, '//input[contains(@class, "mainUrl-module")]')
    FORMAT = (By.XPATH, '//div[contains(@id, "patterns_banner_4")]/span')
    NAME = (By.XPATH, '// div[contains(@class, "input_campaign-name")] /div/input')
    INPUT = (By.XPATH, '//div[contains(@class, "roles-module-buttonWrap")]/div/input')
    SAVE_IMAGE = (By.XPATH, '//input[contains(@class, "image-cropper__save")]')
    CREATE = (By.XPATH, '//div[contains(@class, "save-button")]/button')