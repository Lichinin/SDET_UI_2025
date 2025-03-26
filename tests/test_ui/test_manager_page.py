from helpers.assertion_helper import AssertionHelper


def test_customer_add(manager_page, setup_customer):
    page = manager_page
    page.click_add_customer_menu_button()
    page.fill_first_name_field(setup_customer['first_name'])
    page.fill_last_name_field()
    page.fill_post_code_field(setup_customer['code'])
    page.click_add_customer_submit_button()
    page.get_alert_message()
    AssertionHelper.assert_alert_message(
        page.alert_message,
        'Customer added successfully with customer id :6'
    )


def test_customers_sort_by_name(manager_page):
    page = manager_page
    page.click_customers_menu_button()
    page.click_twice_first_name_column()
    page.get_customers_name()
    AssertionHelper.assert_sorting_by_name(
        page.actual_customers_name,
        page.sorted_customer_name
    )


def test_customer_delete(manager_page):
    page = manager_page
    page.click_customers_menu_button()
    page.get_customers_name()
    page.choice_customer_to_delete(page.actual_customers_name)
    page.click_delete_button(page.name_to_delete)
    page.get_customers_name()
    AssertionHelper.assert_customer_delition(
        page.actual_customers_name,
        page.name_to_delete
    )