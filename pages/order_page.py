from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_first_form(self, name, surname, address, metro_station, phone):
        # Имя
        self.find_element(OrderPageLocators.NAME_INPUT).send_keys(name)
        # Фамилия
        self.find_element(OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        # Адрес
        self.find_element(OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        # Станция метро
        metro_input = self.find_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro_station)
        # Ждём появления выпадающего списка и кликаем
        self.click(OrderPageLocators.METRO_STATION_OPTION, timeout=5)
        # Телефон
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        # Далее
        self.click(OrderPageLocators.NEXT_BUTTON)

    def fill_second_form(self, date, rental_period, color, comment):
        # Дата
        date_input = self.find_element(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        # Срок аренды
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        # Ждём появления списка опций и кликаем нужную
        options = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTION, timeout=5)
        options[rental_period].click()
        # Цвет
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)
        # Комментарий
        if comment:
            self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        # Кнопка «Заказать»
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_success_window_displayed(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_HEADER)