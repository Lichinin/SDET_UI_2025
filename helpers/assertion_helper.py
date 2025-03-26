
class AssertionHelper:
    @staticmethod
    def assert_alert_message(actual, excepted):
        assert actual, excepted

    @staticmethod
    def assert_sorting_by_name(actual, excepted):
        assert actual, excepted

    @staticmethod
    def assert_customer_delition(customers, deleted_customer):
        assert deleted_customer not in customers
