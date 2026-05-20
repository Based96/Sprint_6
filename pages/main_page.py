from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(Urls.MAIN_PAGE)

    def close_cookie_popup(self):
        try:
            self.click(MainPageLocators.COOKIE_BUTTON, timeout=3)
        except:
            pass

    def get_question_locator(self, index):
        questions = [
            MainPageLocators.QUESTION_BUTTON_0,
            MainPageLocators.QUESTION_BUTTON_1,
            MainPageLocators.QUESTION_BUTTON_2,
            MainPageLocators.QUESTION_BUTTON_3,
            MainPageLocators.QUESTION_BUTTON_4,
            MainPageLocators.QUESTION_BUTTON_5,
            MainPageLocators.QUESTION_BUTTON_6,
            MainPageLocators.QUESTION_BUTTON_7,]
        return questions[index]

    def get_answer_locator(self, index):
        answers = [
            MainPageLocators.ANSWER_0,
            MainPageLocators.ANSWER_1,
            MainPageLocators.ANSWER_2,
            MainPageLocators.ANSWER_3,
            MainPageLocators.ANSWER_4,
            MainPageLocators.ANSWER_5,
            MainPageLocators.ANSWER_6,
            MainPageLocators.ANSWER_7,]
        return answers[index]

    def click_question(self, index):
        question_locator = self.get_question_locator(index)
        question = self.find_element(question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question)
        self.wait_for_visibility(question_locator, timeout=3)
        self.click(question_locator)

    def get_answer_text(self, index):
        answer_locator = self.get_answer_locator(index)
        answer = self.wait_for_visibility(answer_locator, timeout=5)
        return answer.text

    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click(MainPageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click(MainPageLocators.LOGO_YANDEX)
