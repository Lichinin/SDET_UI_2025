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
        with allure.step(f'Поиск эелемента "{locator}"'):
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

    @allure.step('Прокрутка страницы до элемента')
    def scroll_to_element(self, element):
        try:
            self.browser.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                element
            )
            time.sleep(0.5)
        except Exception as e:
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.error(f'Ошибка прокрутки элемента: {e}')
            raise

    @allure.step('Клик по полю и его очистка')
    def click_and_clear(self, field, scroll_first=False):
        if scroll_first:
            self.scroll_to_element(field)
        try:
            field.click()
            field.clear()
        except Exception as e:
            self.logger.error(f"Ошибка при клике и очистке элемента: {e}")
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            self.logger.exception('Error: cannot click and clear!')

    @allure.step('Получаю текст aller')
    def get_alert_message(self):
        try:
            alert = self.browser.switch_to.alert
            self.alert_message = alert.text
        except Exception as e:
            self.logger.error(f"Ошибка при работе с alert: {e}")
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
