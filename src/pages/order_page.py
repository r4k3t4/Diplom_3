import allure
from src.locators.order_locators import OrderLocators
from src.pages.base_page import BasePage
from src.config import Config


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Перейти на главную страницу')
    def go_to_main_page(self):
        self.click_element(OrderLocators.CONSTRUCTOR_BUTTON)
        self.wait_load_url(Config.URL)

    @allure.step('Открыть заказ')
    def open_order(self):
        self.click_element(OrderLocators.ORDER_ITEM)

    @allure.step('Проверить появление окна с деталями заказа')
    def check_visible_order_window(self):
        return self.check_is_visible_element(OrderLocators.MODAL_WINDOW)

    @allure.step('Получить список заказов')
    def get_history_orders(self):
        self.wait_for_element_clickable(OrderLocators.ALL_ORDERS_LIST)
        orders = [element.text.lstrip('#0') for element in self.get_elements(OrderLocators.ALL_ORDERS_LIST)]
        return orders

    @allure.step('Получить количество заказов за все время')
    def get_all_orders_count(self):
        return self.get_value_from_element(OrderLocators.ALL_ORDERS_COUNT)

    @allure.step('Проверить, что заказ в работе')
    def check_order_in_work(self, order):
        return self.wait_show_text_in_element(OrderLocators.ORDER_IN_WORK, order)