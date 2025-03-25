from faker import Faker

fake = Faker()


class DataHelper:
    @staticmethod
    def generate_post_code(length=10):
        return fake.random_number(digits=length)

    @staticmethod
    def generate_first_name(code):
        pairs = [int(str(code)[i:i+2]) for i in range(0, len(str(code)), 2)]
        result = []
        for number in pairs:
            letter_index = number % 26
            letter = chr(letter_index + 97)
            result.append(letter)

        return ''.join(result)
