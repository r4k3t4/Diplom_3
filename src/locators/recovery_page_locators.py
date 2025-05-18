from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    EMAIL_INPUT = By.XPATH, '//label[text()="Email"]/../input'  # поле ввода электронной почты
    SUBMIT_BUTTON = By.XPATH, '//form//button'  # кнопка Восстановить
    INFO_ABOUT_RECOVERY_CODE = By.XPATH, '//label[text()="Введите код из письма"]' # сообщение о восстановлении
    SHOW_PASSWORD_BUTTON = By.XPATH, '//div[contains(@class, "input__icon-action")]' # кнопка показать/скрыть пароль
    PASSWORD_FIELD = By.XPATH, '//label[text()="Пароль"]/..' # поле ввода пароля