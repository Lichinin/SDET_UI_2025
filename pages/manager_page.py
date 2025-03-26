import allure

from locators.locators import Selectors
from pages.base_page import BasePage


class ManagerPage(BasePage):

    def click_add_customer_menu_button(self):
        self.get_element(Selectors.BUTTON_MENU_ADD_CUSTOMER).click()

    def fill_first_name_field(self, first_name):
        field = self.get_element(Selectors.FIELD_FIRST_NAME)
        self.click_and_clear(field)
        field.send_keys(first_name)

    def fill_last_name_field(self):
        field = self.get_element(Selectors.FIELD_LAST_NAME)
        self.click_and_clear(field)
        field.send_keys('lname')

    def fill_post_code_field(self, code):
        field = self.get_element(Selectors.FIELD_POST_CODE)
        self.click_and_clear(field)
        field.send_keys(code)

    def click_add_customer_submit_button(self):
        self.get_element(Selectors.BUTTON_CONFIRM_ADD_CUSTOMER).click()

    def click_customers_menu_button(self):
        self.get_element(Selectors.BUTTON_MENU_CUSTOMERS).click()

    def click_twice_first_name_column(self):
        self.get_element(Selectors.COLUMN_FIRST_NAME).click()
        self.get_element(Selectors.COLUMN_FIRST_NAME).click()

    def get_customers_name(self):
        customers_name_elements = self.get_elements(Selectors.CUSTOMER_NAME)
        self.actual_customers_name = [element.text for element in customers_name_elements]
        self.sorted_customer_name = sorted(self.actual_customers_name)