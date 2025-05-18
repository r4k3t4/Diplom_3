from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import allure

from src.locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        with allure.step(f"Click element with locator {locator}"):
            self.find_element(locator).click()

    def select_element(self, locator):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=20):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_visibility(self, locator, timeout=20):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться ожидаемого Url')
    def wait_load_url(self, url):
        WebDriverWait(self.driver, 20).until(EC.url_to_be(url))

    @allure.step('Вернуть аттрибут элемента')
    def get_attribute_from_element(self, locator, attribute):
        return self.wait_for_element_visibility(locator).get_attribute(attribute)

    @allure.step('Проверить видимость элемента')
    def check_is_visible_element(self, locator):
        try:
            self.wait_for_element_visibility(locator)
            return True
        except TimeoutException:
            return False

    @allure.step('Выполнить действие перетаскивания')
    def drag_and_drop(self, element, target):
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Подождать исчезновения текста в элементe')
    def wait_hide_text_in_element(self, locator, text):
        WebDriverWait(self.driver, 50).until_not(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Подождать изменение номера')
    def wait_change_number_order(self):
        self.wait_hide_text_in_element(MainPageLocators.ORDER_NUMBER, "9999")
        self.click_element(MainPageLocators.CLOSE_MODAL_WINDOW)

    @allure.step('Найти все элементы')
    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Подождать появления текста в элементe')
    def wait_show_text_in_element(self, locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))
            return True
        except TimeoutException:
            return False

    @allure.step('Получить текущий текст')
    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    @allure.step('Вернуть text элемента')
    def get_value_from_element(self, locator):
        self.wait_for_element_visibility(locator)
        return self.find_element(locator).text