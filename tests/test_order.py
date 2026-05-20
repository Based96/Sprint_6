import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls
from data import OrderData

class TestOrder:

    @pytest.mark.parametrize("name, surname, address, metro_station, phone, date, rental_period, color, comment", [
        (OrderData.NAME_1, OrderData.SURNAME_1, OrderData.ADDRESS_1, OrderData.METRO_STATION_1, OrderData.PHONE_1,
         OrderData.DATE_1, OrderData.RENTAL_PERIOD_1, OrderData.COLOR_1, OrderData.COMMENT_1),
        (OrderData.NAME_2, OrderData.SURNAME_2, OrderData.ADDRESS_2, OrderData.METRO_STATION_2, OrderData.PHONE_2,
         OrderData.DATE_2, OrderData.RENTAL_PERIOD_2, OrderData.COLOR_2, OrderData.COMMENT_2),])
    @allure.title("Заказ самоката через кнопку вверху страницы")
    @allure.description("Проверка полного позитивного сценария заказа самоката с разными данными")

    def test_order_top_button(self, driver, name, surname, address, metro_station, phone, date, rental_period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.close_cookie_popup()

        main_page.click_order_button_top()
        order_page.fill_first_form(name, surname, address, metro_station, phone)
        order_page.fill_second_form(date, rental_period, color, comment)
        order_page.confirm_order()

        assert order_page.is_success_window_displayed()

    @pytest.mark.parametrize("name, surname, address, metro_station, phone, date, rental_period, color, comment", [
        (OrderData.NAME_1, OrderData.SURNAME_1, OrderData.ADDRESS_1, OrderData.METRO_STATION_1, OrderData.PHONE_1,
         OrderData.DATE_1, OrderData.RENTAL_PERIOD_1, OrderData.COLOR_1, OrderData.COMMENT_1),
        (OrderData.NAME_2, OrderData.SURNAME_2, OrderData.ADDRESS_2, OrderData.METRO_STATION_2, OrderData.PHONE_2,
         OrderData.DATE_2, OrderData.RENTAL_PERIOD_2, OrderData.COLOR_2, OrderData.COMMENT_2),])
    @allure.title("Заказ самоката через кнопку внизу страницы")
    @allure.description("Проверка полного позитивного сценария заказа самоката с разными данными через нижнюю кнопку")
    def test_order_bottom_button(self, driver, name, surname, address, metro_station, phone, date, rental_period, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.open()
        main_page.close_cookie_popup()

        main_page.click_order_button_bottom()
        order_page.fill_first_form(name, surname, address, metro_station, phone)
        order_page.fill_second_form(date, rental_period, color, comment)
        order_page.confirm_order()

        assert order_page.is_success_window_displayed()

    @allure.title("Клик на логотип Самоката ведёт на главную страницу")
    @allure.description("Проверка редиректа на главную страницу при клике на логотип Самоката")
    def test_logo_scooter_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.close_cookie_popup()

        main_page.click_order_button_top()
        main_page.click_logo_scooter()

        main_page.wait_for_url(Urls.MAIN_PAGE)
        assert main_page.get_current_url() == Urls.MAIN_PAGE

    @allure.title("Клик на логотип Яндекса - открывает Яндекс в новой вкладке")
    @allure.description("Проверка открытия главной страницы Яндекса в новой вкладке при клике на логотип Яндекса")
    def test_logo_yandex_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.close_cookie_popup()

        original_window = driver.current_window_handle

        main_page.click_logo_yandex()

        main_page.switch_to_new_window(original_window)

        main_page.wait_for_url_contains(Urls.YA_REDIRECT, timeout=15)
        assert Urls.YA_REDIRECT in main_page.get_current_url()