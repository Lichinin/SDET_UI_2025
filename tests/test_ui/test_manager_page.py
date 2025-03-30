import allure

from constants.constants import Constants
from helpers.data_helper import DataHelper
from pages.manager_page import ManagerPage


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
class TestManagerPage:
    @allure.title('Тест добавления Customer')
    @allure.description(
        'Проверка создания нового Customer и сообщения об успешном создании.'
    )
    def test_customer_add(self, manager_page: ManagerPage, customer_data):
        manager_page.click_add_customer_menu_button()
        manager_page.fill_form(
            manager_page.FIELD_FIRST_NAME,
            customer_data['first_name']
        )
        manager_page.fill_form(
            manager_page.FIELD_LAST_NAME,
            customer_data['first_name']
        )
        manager_page.fill_form(
            manager_page.FIELD_POST_CODE,
            customer_data['first_name']
        )
        manager_page.click_add_customer_submit_button()
        with allure.step('Проверка сообщения о создании пользователя'):
            assert (
                manager_page.get_alert_message().startswith(
                    Constants.EXPECTED_CUSTOMER_ADD_MESSAGE
                )
            )

    @allure.title('Тест сортировки Customers по First Name')
    @allure.description(
        'Сортировка Customers по First_Name и проверка корректности сортировки'
    )
    def test_customers_sort_by_name(self, manager_page: ManagerPage):
        manager_page.click_customers_menu_button()
        manager_page.click_twice_first_name_column()
        with allure.step('Проверка сортировки списка Customer'):
            actual_customers_name = manager_page.get_customers_name()
            assert (
                actual_customers_name
                == sorted(actual_customers_name)
            )

    @allure.title('Тест удаления Customer')
    @allure.description(
        'Удаление Customer и проверка его отсутствия в списке Customers.'
    )
    def test_customer_delete(self, manager_page: ManagerPage):
        manager_page.click_customers_menu_button()
        customer_to_delete = DataHelper.choice_name_to_delete(
            manager_page.get_customers_name()
        )
        manager_page.fill_form(
            manager_page.FIELD_SEARCH_CUSTOMER,
            customer_to_delete
        )
        manager_page.click_delete_button()
        manager_page.clear_search_field()
        with allure.step('Проверка отсутствия удаленного Customer в списке'):
            assert customer_to_delete not in manager_page.get_customers_name()
