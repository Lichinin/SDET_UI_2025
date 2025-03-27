import allure

from constants.constants import Constants
from helpers.assertion_helper import AssertionHelper


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест добавления Customer')
@allure.description('Проверка создания нового Customer и сообщения об успешном создании.')
def test_customer_add(manager_page, setup_customer, teardown_customer):
    page = manager_page
    page.click_add_customer_menu_button()
    page.fill_first_name_field(setup_customer['first_name'])
    page.fill_last_name_field()
    page.fill_post_code_field(setup_customer['code'])
    page.click_add_customer_submit_button()
    page.get_alert_message()
    AssertionHelper.assert_equals(
        page.logger,
        page.alert_message,
        Constants.EXPECTED_CUSTOMER_ADD_MESSAGE
    )


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест сортировкт Customers по First Name')
@allure.description('Сортировка Customers по First_Name и проверка корректности сортировки')
def test_customers_sort_by_name(manager_page):
    page = manager_page
    page.click_customers_menu_button()
    page.click_twice_first_name_column()
    page.get_customers_name()
    AssertionHelper.assert_equals(
        page.logger,
        page.actual_customers_name,
        page.sorted_customer_name
    )


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест удаления Customer')
@allure.description('Удаление Customer и проверка его отсутствия в списке Customers.')
def test_customer_delete(manager_page):
    page = manager_page
    page.click_customers_menu_button()
    page.get_customers_name()
    page.choice_customer_to_delete(page.actual_customers_name)
    page.click_delete_button(page.name_to_delete)
    page.get_customers_name()
    AssertionHelper.assert_entry(
        page.logger,
        page.actual_customers_name,
        page.name_to_delete
    )
