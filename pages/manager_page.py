import allure

from helpers.data_helper import DataHelper
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ManagerPage(BasePage):

    BUTTON_MENU_ADD_CUSTOMER = (
        By.CSS_SELECTOR, 'button[ng-click="addCust()"]'
    )
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    FIELD_LAST_NAME = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    FIELD_POST_CODE = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    FIELD_SEARCH_CUSTOMER = (
        By.CSS_SELECTOR,
        'input[ng-model="searchCustomer"]'
    )
    BUTTON_CONFIRM_ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[type="submit"]')
    BUTTON_MENU_CUSTOMERS = (By.CSS_SELECTOR, 'button[ng-click="showCust()"]')
    COLUMN_FIRST_NAME = (
        By.CSS_SELECTOR,
        'a[ng-click="sortType = \'fName\'; sortReverse = !sortReverse"]'
    )
    CUSTOMER_NAME = (By.CSS_SELECTOR, 'tr.ng-scope td:nth-child(1)')
    BUTTON_DELETE_CUSTOMER = (
        By.XPATH,
        '//tr[contains(@class, "ng-scope") and .//td[text()="{name}"]]//button[text()="Delete"]'
    )

    @allure.step('Нажать кнопку "Add Customer" в меню')
    def click_add_customer_menu_button(self):
        self.get_element(self.BUTTON_MENU_ADD_CUSTOMER).click()

    @allure.step('Заполнить поле "First Name"')
    def fill_first_name_field(self, first_name):
        field = self.get_element(self.FIELD_FIRST_NAME)
        self.click_and_clear(field)
        field.send_keys(first_name)

    @allure.step('Заполнить поле "Last Name"')
    def fill_last_name_field(self, last_name):
        field = self.get_element(self.FIELD_LAST_NAME)
        self.click_and_clear(field)
        field.send_keys(last_name)

    @allure.step('Заполнить поле "Post Code"')
    def fill_post_code_field(self, code):
        field = self.get_element(self.FIELD_POST_CODE)
        self.click_and_clear(field)
        field.send_keys(code)

    @allure.step('Нажать кнопку "Add Customer" под формой')
    def click_add_customer_submit_button(self):
        self.get_element(self.BUTTON_CONFIRM_ADD_CUSTOMER).click()

    @allure.step('Нажать кнопку "Customers" в меню')
    def click_customers_menu_button(self):
        self.get_element(self.BUTTON_MENU_CUSTOMERS).click()

    @allure.step('Кликнуть два раза по названию столбца "First Name"')
    def click_twice_first_name_column(self):
        self.get_element(self.COLUMN_FIRST_NAME).click()
        self.get_element(self.COLUMN_FIRST_NAME).click()

    @allure.step('Получить имена всех Customers')
    def get_customers_name(self):
        customers_name_elements = self.get_elements(self.CUSTOMER_NAME)
        self.actual_customers_name = [
            element.text for element in customers_name_elements
        ]
        self.sorted_customer_name = sorted(self.actual_customers_name)

    @allure.step('Выбрать пользователя для удаления')
    def choice_customer_to_delete(self, customers_name):
        self.name_to_delete = DataHelper.choice_name_to_delete(customers_name)

    @allure.step('Нажать кнопку "Delete"')
    def click_delete_button(self, name_to_delete):
        locator = (
            self.BUTTON_DELETE_CUSTOMER[0],
            self.BUTTON_DELETE_CUSTOMER[1].format(name=name_to_delete)
        )
        self.get_element(locator).click()

    @allure.step('Заполнить поле "Search"')
    def fill_search_field(self, name):
        field = self.get_element(self.FIELD_SEARCH_CUSTOMER)
        self.click_and_clear(field)
        field.send_keys(name)
