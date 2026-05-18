import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import Urls


class TestOrder:

    @pytest.mark.parametrize("name, surname, address, metro_station, phone, date, rental_period, color, comment", [
        ("Игорь", "Иванов", "ул. Селезнева, д. 1", "Курская", "89001234567", "15.05.2026", 1, "black", "Позвонить за час"),
        ("Вероника", "Иванова", "ул. Ставропольская, д. 100", "Речной Вокзал", "89007654321", "20.05.2026", 3, "grey", ""),])
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
        ("Игорь", "Иванов", "ул. Селезнева, д. 1", "Курская", "89001234567", "15.05.2026", 1, "black", "Позвонить за час"),
        ("Вероника", "Петрова", "ул. Ставропольская, д. 10", "Речной вокзал", "89007654321", "20.05.2026", 3, "grey", ""),])
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