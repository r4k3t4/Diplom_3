
import allure
from src.data import get_exist_user_data
from src.locators.login_page_locators import LoginPageLocators
from src.pages.base_page import BasePage
from src.config import Config


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_on_recovery_button(self):
        self.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step(f'Current url')
    def get_current_url(self):
        return self.driver.current_url

    def enter_recovery_data(self):
        email = get_exist_user_data()
        self.wait_for_element_visibility(LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.click_element(LoginPageLocators.SUMBIT_BUTTON)

    def click_recovery_password_button(self, locator):
        self.wait_for_element_clickable(locator).click()

    def find_save_button(self):
        self.wait_for_element_clickable(LoginPageLocators.SUMBIT_BUTTON)

    @allure.step('Перейти на страницу Восстановление пароля')
    def go_to_recovery_password(self):
        self.click_element(LoginPageLocators.RECOVERY_PASSWORD_BUTTON)

    @allure.step('Авторизоваться пользователем')
    def login_user(self):
        email, password = get_exist_user_data()
        self.wait_load_url(Config.LOGIN_URL)
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click_element(LoginPageLocators.SUBMIT_BUTTON)
        #self.wait_for_element_visibility(PersonalAccountLocators.EXIT_BTN)

    @allure.step('Проверить видимость формы авторизации')
    def check_visible_login_form(self):
        return self.check_is_visible_element(LoginPageLocators.LOGIN_FORM)

