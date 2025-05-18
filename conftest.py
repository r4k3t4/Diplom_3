import pytest
from selenium import webdriver
from src.config import Config
from src.pages.login_page import LoginPage
from src.pages.main_page import MainPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(Config.URL)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(Config.URL)
    yield driver
    driver.quit()


@pytest.fixture()
def login_user(driver):
    MainPage(driver).go_to_personal_account()
    LoginPage(driver).login_user()
