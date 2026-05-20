from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница заказа «Для кого самокат»
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_OPTION = (By.XPATH, "//div[@class='select-search__select']//li")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница заказа «Про аренду»
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[@class='Dropdown-control']")
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option']")
    COLOR_BLACK = (By.XPATH, "//input[@id='black']")
    COLOR_GREY = (By.XPATH, "//input[@id='grey']")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    # Окно подтверждения заказа
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Окно «Заказ оформлен»
    SUCCESS_HEADER = (By.XPATH, "//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    CHECK_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")