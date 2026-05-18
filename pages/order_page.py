from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        metro_option = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_STATION_OPTION))
        metro_option.click()
        # Телефон
        self.find_element(OrderPageLocators.PHONE_INPUT).send_keys(phone)
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
        options = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(OrderPageLocators.RENTAL_PERIOD_OPTION))
        options[rental_period].click()
        # Цвет
        if color == "black":
            self.click(OrderPageLocators.COLOR_BLACK)
        elif color == "grey":
            self.click(OrderPageLocators.COLOR_GREY)
        # Комментарий
        if comment:
            self.find_element(OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        # Кнопка «Заказать»
        self.click(OrderPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    def is_success_window_displayed(self):
        return self.find_element(OrderPageLocators.SUCCESS_HEADER).is_displayed()