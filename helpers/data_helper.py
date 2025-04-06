import string

import allure
from faker import Faker

fake = Faker()


class DataHelper:
    @staticmethod
    @allure.step('Сгенерировать 10-значное число')
    def generate_post_code(length=10):
        return fake.random_number(digits=length)

    @staticmethod
    @allure.step('Сгенерировать First_Name на основе Post_Code')
    def generate_first_name(code):
        pairs = [int(str(code)[i:i+2]) for i in range(0, len(str(code)), 2)]
        return ''.join(
            string.ascii_lowercase[number % len(string.ascii_lowercase)] for number in pairs
        )

    @staticmethod
    @allure.step('Сгенерировать last_name')
    def generate_last_name():
        return fake.last_name()

    @staticmethod
    @allure.step('Выбрать пользователя для удаления на основе расчетов')
    def choice_name_to_delete(name_list):
        customers_name_length = {name: len(name) for name in name_list}
        average_length = (
            sum(customers_name_length.values()) / len(customers_name_length)
        )
        closest_name = (
            min(customers_name_length.keys(),
                key=lambda name: abs(
                    customers_name_length[name] - average_length
                ))
        )
        return closest_name
