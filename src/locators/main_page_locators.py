from selenium.webdriver.common.by import By


class MainPageLocators:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, ".//a[@href='/account']/p"
    ORDER_FEED_BUTTON = By.XPATH, '//p[text()="Лента Заказов"]'
    INGREDIENT = By.XPATH, '//a[contains(@class,"BurgerIngredient")]'
    INGREDIENT_POPUP_WINDOW = By.XPATH, '//section[contains (@class, "modal_opened")]'
    INGREDIENT_POPUP_WINDOW_CLOSE_BUTTON = By.XPATH, '//button[contains(@class, "modal__close")]'
    INGREDIENT_COUNTER = By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]'
    BASKET_AREA = By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket")]'
    CREATE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDER_NUMBER = By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]'
    CLOSE_MODAL_WINDOW = By.XPATH, '//button[contains(@class, "modal")]'
    ORDER_STATUS_TEXT = By.XPATH, '//p[text()="Ваш заказ начали готовить"]'
    SECTION_ORDER = By.XPATH, '//section[contains(@class, "modal_opened")]'
    ORDER_IDENTIFICATE = By.XPATH, '//p[text()="идентификатор заказа"]'
