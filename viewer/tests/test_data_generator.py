import string
import random
from playwright.async_api import async_playwright

'''This file is used for generating data for playwright test across this project, so its always unique'''


class TestDataGenerator:
    @staticmethod
    def random_name_test(length=10):
        return "TEST-" + "" .join(random.choices(string.ascii_letters, k=length))
