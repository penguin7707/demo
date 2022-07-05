from selenium.webdriver.common.by import By

LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
LOGIN_EMAIL = (By.NAME, 'email')
LOGIN_PASSWORD = (By.NAME, 'password')
LOGIN_BUTTON2_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
'''Ждем появления элемента на страницы для потверждения загрузки страницы'''
LOGIN = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]/div/div')


LOGOUT_BUTTON1_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
LOGOUT_BUTTON2_LOCATOR = (By.XPATH, '//a[contains(@href, "logout")]')

PROFILE_BUTTON = (By.XPATH, '//a[contains(@href, "profile")]')
NAME_PHONE_EMAIL = (By.CLASS_NAME, 'input__inp.js-form-element')
MORE_BUTTON = (By.XPATH, '//div[contains(@class, "clickable-button__spinner")]')
DELETE_BUTTON = (By.XPATH, '//div[contains(@class, "clickable-button_email_remove")]')
SAVE_BUTTON = (By.CLASS_NAME, 'button__text')

CHANGE_PAGE1 = (By.XPATH, '//a[contains(@href, "profile")]')
CHANGE_PAGE2 = (By.XPATH, '//a[contains(@href, "billing")]')



