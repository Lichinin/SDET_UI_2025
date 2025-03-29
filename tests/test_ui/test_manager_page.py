import allure

from constants.constants import Constants


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест добавления Customer')
@allure.description('Проверка создания нового Customer и сообщения об успешном создании.')
def test_customer_add(manager_page, setup_customer, teardown_customer):
    manager_page.click_add_customer_menu_button()
    manager_page.fill_first_name_field(setup_customer['first_name'])
    manager_page.fill_last_name_field(setup_customer['last_name'])
    manager_page.fill_post_code_field(setup_customer['code'])
    manager_page.click_add_customer_submit_button()
    manager_page.get_alert_message()
    with allure.step('Проверка сообщения о создании пользователя'):
        assert manager_page.alert_message, Constants.EXPECTED_CUSTOMER_ADD_MESSAGE


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест сортировкт Customers по First Name')
@allure.description('Сортировка Customers по First_Name и проверка корректности сортировки')
def test_customers_sort_by_name(manager_page):
    manager_page.click_customers_menu_button()
    manager_page.click_twice_first_name_column()
    manager_page.get_customers_name()
    with allure.step('Проверка сортировки свиска Customer'):
        assert manager_page.actual_customers_name, manager_page.sorted_customer_name


@allure.epic('SimbirSoft SDET practicum')
@allure.suite('UI tests')
@allure.title('Тест удаления Customer')
@allure.description('Удаление Customer и проверка его отсутствия в списке Customers.')
def test_customer_delete(manager_page):
    manager_page.click_customers_menu_button()
    manager_page.get_customers_name()
    manager_page.choice_customer_to_delete(manager_page.actual_customers_name)
    manager_page.click_delete_button(manager_page.name_to_delete)
    manager_page.get_customers_name()
    with allure.step('Проверка отсутствия удаленного Customer в списке'):
        assert manager_page.name_to_delete not in manager_page.actual_customers_name
