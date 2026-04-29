from basic_calculator import Calculator

class PremiumCalculator(BasicCalculator):
    def __init__(self, first_number, second_number, operation):
        super().__init__(first_number, second_number, operation)

    def power(self, first_number, second_number):
        return first_number ** second_number

    def square_root(self, number):
        return number ** 0.5
