from selenium.webdriver.common.by import By


class OrderLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, '//p[text()="Конструктор"]'
    ORDER_ITEM = By.XPATH, '//li[contains(@class, "OrderHistory_listItem")]'
    MODAL_WINDOW = By.XPATH, '//section[contains (@class, "modal_opened")]'
    ALL_ORDERS_LIST = By.XPATH, '//p[contains(text(), "#")]'
    ALL_ORDERS_COUNT = By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class, "OrderFeed_number")]'
    ORDER_IN_WORK = By.XPATH, '//ul[contains(@class, "orderListReady")]/li'