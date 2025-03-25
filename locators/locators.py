from selenium.webdriver.common.by import By


class Selectors:

    BUTTON_MENU_ADD_CUSTOMER = (
        By.CSS_SELECTOR, 'button[ng-click="addCust()"]'
    )
    FIELD_FIRST_NAME = (By.CSS_SELECTOR, 'input[ng-model="fName"]')
    FIELD_LAST_NAME = (By.CSS_SELECTOR, 'input[ng-model="lName"]')
    FIELD_POST_CODE = (By.CSS_SELECTOR, 'input[ng-model="postCd"]')
    BUTTON_CONFIRM_ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[type="submit"]')
