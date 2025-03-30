import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


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
        'a[ng-click^="sortType = \'fName\'"]'
    )
    CUSTOMER_NAME = (By.CSS_SELECTOR, 'tr.ng-scope td:nth-child(1)')
    BUTTON_DELETE_CUSTOMER = (
        By.CSS_SELECTOR,
        'button[ng-click="deleteCust(cust)"]'
    )

    @allure.step('Нажать кнопку "Add Customer" в меню')
    def click_add_customer_menu_button(self):
        self.get_element(self.BUTTON_MENU_ADD_CUSTOMER).click()

    @allure.step('Заполнить поле по локатору: {locator[1]}')
    def fill_form(self, locator, value):
        field = self.get_element(locator)
        field.send_keys(value)

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

    @allure.step('Нажать кнопку "Delete"')
    def click_delete_button(self):
        self.get_element(self.BUTTON_DELETE_CUSTOMER).click()

    @allure.step('Очистить поле "Search"')
    def clear_search_field(self):
        field = self.get_element(self.FIELD_SEARCH_CUSTOMER)
        field.clear()
