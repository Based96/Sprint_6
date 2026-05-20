from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator))

    def click(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        return element.text

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def send_keys(self, locator, text, timeout=5):
        element = self.find_element(locator, timeout)
        element.send_keys(text)
        return element

    def wait_for_url(self, url, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def wait_for_url_contains(self, url_part, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(url_part))

    def wait_for_visibility(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def switch_to_new_window(self, original_window):
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    def is_element_displayed(self, locator, timeout=5):
        element = self.find_element(locator, timeout)
        return element.is_displayed()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)