import allure
from src.locators.personal_account_page_locators import PersonalAccountLocators
from src.pages.base_page import BasePage
from src.config import Config


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.wait_load_url(Config.ORDER_HISTORY_URL)

    @allure.step('Выйти из профиля')
    def logout(self):
        self.wait_for_element_clickable(PersonalAccountLocators.EXIT_BUTTON)
        self.click_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Перейти к истории заказов')
    def go_to_orders_history(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Получить список заказов пользователя')
    def get_history_orders(self):
        self.go_to_orders_history()
        self.wait_for_element_visibility(PersonalAccountLocators.ORDERS_HISTORY_LIST)
        orders = [element.text.lstrip('#0') for element in self.get_elements(PersonalAccountLocators.ORDERS_HISTORY_LIST)]
        return orders

    @allure.step('Перейти на страницу Лента заказов')
    def go_to_orders_feed_page(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)
        self.wait_load_url(Config.ORDER_HISTORY_URL)
