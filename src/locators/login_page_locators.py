from selenium.webdriver.common.by import By


class LoginPageLocators:
    #PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']/p"
    EMAIL_FIELD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default']/input"
    RECOVERY_PASSWORD_BUTTON = By.XPATH, ".//a[@href='/forgot-password']"
    SUBMIT_BUTTON = By.XPATH, "//form//button"
    EMAIL_INPUT = ('xpath', '//label[text()="Email"]/../input')  # поле ввода электронной почты
    PASSWORD_INPUT = ('xpath', '//label[text()="Пароль"]/../input')  # поле ввода пароля
    LOGIN_FORM = By.XPATH, '//h2[text()="Вход"]'  # форма авторизации