import allure


class AssertionHelper:
    @staticmethod
    @allure.step('Проверить равенство значений')
    def assert_equals(logger, expected, actual):
        logger.info('* Check assertion')
        try:
            assert expected == actual, (
                f"Expected: '{expected}', Actual: '{actual}'"
            )
            logger.info('*** Test completed successful ***')
        except AssertionError as e:
            logger.exception(e)
            logger.info('!!! Test failed !!!')
            raise

    @staticmethod
    @allure.step('Проверить вхождение элемента в список')
    def assert_entry(logger, list, value):
        logger.info('* Check assertion')
        try:
            assert value not in list, (
                f'"{value}" must not be in "{list}"'
            )
            logger.info('*** Test completed successful ***')
        except AssertionError as e:
            logger.exception(e)
            logger.info('!!! Test failed !!!')
            raise
