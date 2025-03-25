from helpers.assertion_helper import AssertionHelper


def test_form_filling(manager_page):
    page = manager_page
    page.click_add_customer_menu_button()
    page.fill_first_name_field()
    page.fill_last_name_field()
    page.fill_post_code_field()
    page.click_add_customer_submit_button()
    page.get_alert_message()
    AssertionHelper.assert_alert_message(
        page.alert_message,
        'Customer added successfully with customer id :6'
    )
