import allure
from pages.main_page import MainPage


class TestQuestions:

    @allure.title("Проверка вопроса №0: «Сколько это стоит? И как оплатить?»")
    @allure.description("Клик на стрелку вопроса №0 и проверка, что открылся правильный текст ответа")
    def test_question_0(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(0)
        answer_text = page.get_answer_text(0)
        assert answer_text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title("Проверка вопроса №1: «Хочу сразу несколько самокатов! Так можно?»")
    @allure.description("Клик на стрелку вопроса №1 и проверка, что открылся правильный текст ответа")
    def test_question_1(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(1)
        answer_text = page.get_answer_text(1)
        assert "Пока что у нас так: один заказ — один самокат." in answer_text

    @allure.title("Проверка вопроса №2: «Как рассчитывается время аренды?»")
    @allure.description("Клик на стрелку вопроса №2 и проверка, что открылся правильный текст ответа")
    def test_question_2(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(2)
        answer_text = page.get_answer_text(2)
        assert "Допустим, вы оформляете заказ на 8 мая." in answer_text

    @allure.title("Проверка вопроса №3: «Можно ли заказать самокат прямо на сегодня?»")
    @allure.description("Клик на стрелку вопроса №3 и проверка, что открылся правильный текст ответа")
    def test_question_3(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(3)
        answer_text = page.get_answer_text(3)
        assert "Только начиная с завтрашнего дня." in answer_text

    @allure.title("Проверка вопроса №4: «Можно ли продлить заказ или вернуть самокат раньше?»")
    @allure.description("Клик на стрелку вопроса №4 и проверка, что открылся правильный текст ответа")
    def test_question_4(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(4)
        answer_text = page.get_answer_text(4)
        assert "Пока что нет!" in answer_text

    @allure.title("Проверка вопроса №5: «Вы привозите зарядку вместе с самокатом?»")
    @allure.description("Клик на стрелку вопроса №5 и проверка, что открылся правильный текст ответа")
    def test_question_5(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(5)
        answer_text = page.get_answer_text(5)
        assert "Самокат приезжает к вам с полной зарядкой." in answer_text

    @allure.title("Проверка вопроса №6: «Можно ли отменить заказ?»")
    @allure.description("Клик на стрелку вопроса №6 и проверка, что открылся правильный текст ответа")
    def test_question_6(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(6)
        answer_text = page.get_answer_text(6)
        assert "Да, пока самокат не привезли." in answer_text

    @allure.title("Проверка вопроса №7: «Я жизу за МКАДом, вам привезёте?»")
    @allure.description("Клик на стрелку вопроса №7 и проверка, что открылся правильный текст ответа")
    def test_question_7(self, driver):
        page = MainPage(driver)
        page.open()
        page.close_cookie_popup()
        page.click_question(7)
        answer_text = page.get_answer_text(7)
        assert "Да, обязательно. Всем самокатов!" in answer_text
