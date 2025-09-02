import string
from random import random
import pytest

'''This file is used for generating data for playwright test across this project'''

class TestDataGenerator:
    def random_name(length=7):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))