from src.locators.main_page_locators import MainPageLocators
from src.pages.base_page import BasePage
import allure
from src.config import Config


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step(f'Current url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Перейти на страницу Авторизация')
    def go_to_personal_account(self):
        self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_load_url(Config.LOGIN_URL)

    @allure.step('Нажать кнопку Войти в аккаунт')
    def login_account(self):
        self.wait_for_element_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_load_url(Config.PERSONAL_ACCOUNT_URL)

    def go_to_orders_feed_page(self):
        self.wait_for_element_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_load_url(Config.ORDER_FEED_URL)

    @allure.step("Кликнуть на ингредиент")
    def view_ingredient(self):
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step("Проверить открытие окна с деталями ингредиента")
    def check_visible_ingredient_detail_windows(self):
        return self.check_is_visible_element(MainPageLocators.INGREDIENT_POPUP_WINDOW)

    @allure.step("Закрыть окно с деталями об ингредиенте")
    def close_ingredient_detail_windows(self):
        self.click_element(MainPageLocators.INGREDIENT_POPUP_WINDOW_CLOSE_BUTTON)

    @allure.step("Получить количество добавлений ингредиента")
    def get_ingredient_count(self):
        return self.get_value_from_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient_in_basket(self):
        element = self.find_element(MainPageLocators.INGREDIENT)
        target = self.find_element(MainPageLocators.BASKET_AREA)
        self.drag_and_drop(element, target)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_ingredient_in_basket()
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)
        self.wait_hide_text_in_element(MainPageLocators.ORDER_NUMBER, "9999")
        self.wait_for_element_visibility(MainPageLocators.ORDER_IDENTIFICATE)
        order = self.get_actually_text(MainPageLocators.ORDER_NUMBER)
        while order == '9999':
            order = self.get_actually_text(MainPageLocators.ORDER_NUMBER)
        self.wait_change_number_order()
        return order

    @allure.step('Проверить наличие, что заказа начали готовить')
    def check_displayed_order_status_text(self) -> bool:
        return self.wait_for_element_visibility(MainPageLocators.ORDER_STATUS_TEXT).is_displayed()