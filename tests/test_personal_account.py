import allure

from src.config import Config
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage

from src.pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_go_to_personal_account(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.login_account()
        assert main_page.get_current_url() == Config.PERSONAL_ACCOUNT_URL

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_go_to_order_history(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.login_account()
        profile_page = PersonalAccountPage(driver)
        profile_page.click_order_history_button()
        assert main_page.get_current_url() == Config.ORDER_HISTORY_URL

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_personal_account(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.login_account()
        profile_page = PersonalAccountPage(driver)
        profile_page.logout()
        login_page = LoginPage(driver)
        assert login_page.check_visible_login_form()
