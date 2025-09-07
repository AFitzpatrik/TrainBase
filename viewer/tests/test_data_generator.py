import string
import random

'''This file is used for generating data for playwright test across this project, so its always unique'''


class TestDataGenerator:
    @staticmethod
    def random_name_test(length=10):
        # Generates random name in "TEST-[Random 10 letter]" model. Length can be adjusted.
        return "TEST-" + "" .join(random.choices(string.ascii_letters, k=length))
