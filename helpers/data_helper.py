import allure
from faker import Faker

from constants.constants import Constants

fake = Faker()


class DataHelper:
    @staticmethod
    @allure.step('Генерация 10-значного числа')
    def generate_post_code(length=10):
        return fake.random_number(digits=length)

    @staticmethod
    @allure.step('Генерация First_Name на основе Post_Code')
    def generate_first_name(code):
        pairs = [int(str(code)[i:i+2]) for i in range(0, len(str(code)), 2)]
        result = []
        for number in pairs:
            letter_index = number % Constants.ALPHABET_SIZE
            letter = chr(letter_index + Constants.ASCII_LOWERCASE_A)
            result.append(letter)

        return ''.join(result)

    @staticmethod
    @allure.step('Генерация last_name')
    def generate_last_name():
        return fake.last_name()

    @staticmethod
    @allure.step('Выбор пользователя для удаления на основе расчетов')
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
