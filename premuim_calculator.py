from basic_calculator import Calculator

class PremiumCalculator(Calculator):
    def __init__(self, first_number, second_number, operation):
        self.first_number = first_number
        self.second_number = second_number
        self.operation = operation
        super().__init__(first_number, second_number, operation)

    def power(self):
        return self.first_number ** self.second_number

    def square_root(self, number):
        if number < 0:
            return "Error: Square root of a negative number is not defined."
        return number ** 0.5
    
    def radical(self):
        if self.second_number == 0:
            return "Error: Cannot take the root of degree zero."
        elif self.first_number < 0 and self.second_number % 2 == 0:
            return "Error: Even root of a negative number is not defined."
        return self.first_number ** (1/self.second_number)
    
    def remainder(self):
        if self.second_number == 0:
            return "Error: Division by zero is not allowed."
        return self.first_number % self.second_number
