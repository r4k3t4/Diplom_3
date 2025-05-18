import allure
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage
from src.pages.recovery_page import RecoveryPage


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_password_recovery_page(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_personal_account()
        login_page = LoginPage(driver)
        login_page.go_to_recovery_password()
        recovery_page = RecoveryPage(driver)
        assert recovery_page.find_save_button()

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_recovery_password_form(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_personal_account()
        login_page = LoginPage(driver)
        login_page.go_to_recovery_password()
        recovery_page = RecoveryPage(driver)
        recovery_page.filling_recovery_form()
        assert recovery_page.find_save_button()

    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_check_show_password_button(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_personal_account()
        login_page = LoginPage(driver)
        login_page.go_to_recovery_password()
        recovery_page = RecoveryPage(driver)
        recovery_page.filling_recovery_form()
        recovery_page.hide_or_show_password()
        assert recovery_page.check_active_password_field()