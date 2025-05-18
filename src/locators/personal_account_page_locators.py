from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PROFILE_INFO = By.XPATH, "//div[@class='Account_contentBox__2CPm3']"  # информация о профиле пользователя
    ORDER_HISTORY_BUTTON = By.XPATH, '//a[text()="История заказов"]'  # кнопка перехода в историю заказов
    EXIT_BUTTON = By.XPATH, '//button[text()="Выход"]'  # кнопка Выйти из профиля
    ORDERS_HISTORY_LIST = By.XPATH, '//p[contains(text(), "#")]'  # история заказов пользователя

