import time

import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.logger = browser.logger

    @allure.step('Поиск элемента на странице')
    def get_element(self, locator: tuple, timeout=3):
        with allure.step(f'Поиск элемента "{locator}"'):
            try:
                self.browser.logger.info(f'* Get element "{repr(locator)}"')
                return WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(locator)
                )
            except Exception:
                allure.attach(
                    name="failure_screenshot",
                    body=self.browser.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG
                )
            self.logger.exception('Error: element not found!')
            raise

    @allure.step('Поиск нескольких элементов на странице')
    def get_elements(self, locator: tuple, timeout=3):
        with allure.step(f'Поиск элементов "{locator}"'):
            try:
                self.browser.logger.info(f'* Get elements {repr(locator)}')
                return WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_all_elements_located(locator)
                )
            except Exception:
                allure.attach(
                    name="failure_screenshot",
                    body=self.browser.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG
                )
            self.logger.exception('Error: elements not found!')
            raise

    @allure.step('Получаю текст allert')
    def get_alert_message(self):
        alert = self.browser.switch_to.alert
        return alert.text if alert.text else None
