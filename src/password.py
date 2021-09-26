import string
import random


class Password:
    def __init__(self, length: int):
        self.length = length

    @property
    def generate(self):
        return "".join(
            random.choices(
                string.ascii_letters + string.digits + string.punctuation, k=self.length
            )
        )

    @staticmethod
    def is_valid(password):
        """Validate if a password is valid"""
        lis = [1, 1, 1, 1]
        for i in password:
            if i.isupper():
                lis[0] = 2
            elif i.islower():
                lis[1] = 2
            elif i.isdigit():
                lis[2] = 2
            elif i in string.punctuation:
                lis[3] = 2
        if 1 not in lis:
            return True

    @property
    def verification(self):
        """Generate a valid password"""
        while True:
            password = self.generate
            if self.is_valid(password):
                break
        return password
