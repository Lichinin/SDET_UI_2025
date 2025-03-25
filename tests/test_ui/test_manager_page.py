# from helpers.assertion_helper import AssertionHelper


def test_form_filling(manager_page):
    page = manager_page
    page.click_add_customer_menu_button()
    page.fill_first_name_field()
    page.fill_last_name_field()
    page.fill_post_code_field()
    page.click_add_customer_submit_button()
    page.assert_sucessfull_creation()
    # AssertionHelper.assert_customer_creation
