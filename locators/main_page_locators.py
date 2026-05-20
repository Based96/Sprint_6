from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопки «Заказать»
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Вопросы и ответы
    QUESTION_BUTTON_0 = (By.ID, "accordion__heading-0")
    QUESTION_BUTTON_1 = (By.ID, "accordion__heading-1")
    QUESTION_BUTTON_2 = (By.ID, "accordion__heading-2")
    QUESTION_BUTTON_3 = (By.ID, "accordion__heading-3")
    QUESTION_BUTTON_4 = (By.ID, "accordion__heading-4")
    QUESTION_BUTTON_5 = (By.ID, "accordion__heading-5")
    QUESTION_BUTTON_6 = (By.ID, "accordion__heading-6")
    QUESTION_BUTTON_7 = (By.ID, "accordion__heading-7")

    ANSWER_0 = (By.ID, "accordion__panel-0")
    ANSWER_1 = (By.ID, "accordion__panel-1")
    ANSWER_2 = (By.ID, "accordion__panel-2")
    ANSWER_3 = (By.ID, "accordion__panel-3")
    ANSWER_4 = (By.ID, "accordion__panel-4")
    ANSWER_5 = (By.ID, "accordion__panel-5")
    ANSWER_6 = (By.ID, "accordion__panel-6")
    ANSWER_7 = (By.ID, "accordion__panel-7")

    # Логотипы
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Кнопка согласия с куками
    COOKIE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")