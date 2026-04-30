from basic_calculator import Calculator

class PremiumCalculator(Calculator):
    def __init__(self, first_number, second_number, operation):
        super().__init__(first_number, second_number, operation)

    def power(self, first_number, second_number):
        return first_number ** second_number

    def square_root(self, number):
        if number < 0:
            return "Error: Square root of a negative number is not defined."
        return number ** 0.5
    
    def remainder(self, first_number, second_number):
        if second_number == 0:
            return "Error: Division by zero is not allowed."
        return first_number % second_number
