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
