import allure
from src.locators.recovery_page_locators import RecoveryPageLocators
from src.pages.base_page import BasePage
from src.data import get_exist_user_data


class RecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнить форму восстановления пароля')
    def filling_recovery_form(self):
        email, password = get_exist_user_data()
        self.find_element(RecoveryPageLocators.EMAIL_INPUT).send_keys(email)
        self.click_element(RecoveryPageLocators.SUBMIT_BUTTON)

    @allure.step('Проверить видимость формы восстановления пароля')
    def find_save_button(self):
        return self.wait_for_element_visibility(RecoveryPageLocators.SUBMIT_BUTTON)

    @allure.step('Проверить активность поля')
    def check_active_password_field(self):
        if 'status_active' in self.get_attribute_from_element(RecoveryPageLocators.PASSWORD_FIELD, 'class'):
            return True
        else:
            return False

    @allure.step('Кликнуть на Показать/Скрыть пароль')
    def hide_or_show_password(self):
        self.wait_for_element_clickable(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)
        self.click_element(RecoveryPageLocators.SHOW_PASSWORD_BUTTON)
