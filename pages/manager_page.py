import allure

from locators.locators import Selectors
from pages.base_page import BasePage


class ManagerPage(BasePage):

    def click_add_customer_menu_button(self):
        self.get_element(Selectors.BUTTON_MENU_ADD_CUSTOMER).click()

    def fill_first_name_field(self):
        field = self.get_element(Selectors.FIELD_FIRST_NAME)
        self.click_and_clear(field)
        field.send_keys('fname')

    def fill_last_name_field(self):
        field = self.get_element(Selectors.FIELD_LAST_NAME)
        self.click_and_clear(field)
        field.send_keys('lname')

    def fill_post_code_field(self):
        field = self.get_element(Selectors.FIELD_POST_CODE)
        self.click_and_clear(field)
        field.send_keys('0101010101')

    def click_add_customer_submit_button(self):
        self.get_element(Selectors.BUTTON_CONFIRM_ADD_CUSTOMER).click()

    def assert_sucessfull_creation(self):
        try:
            alert = self.browser.switch_to.alert
            message = alert.text
        except Exception as e:
            self.logger.error(f"Ошибка при работе с alert: {e}")
            allure.attach(
                name="failure_screenshot",
                body=self.browser.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
        self.assert_equals(
            'Customer added successfully with customer id :6',
            message
        )
