from basic_calculator import Calculator

class PremiumCalculator(Calculator):

    def power(self):
        return self.first_number ** self.second_number

    def square_root(self, number):
        if number < 0:
            return "\nError: Square root of a negative number is not defined."
        return number ** 0.5
    
    def radical(self):
        if self.second_number == 0:
            return "\nError: Cannot take the root of degree zero."
        elif self.first_number < 0 and self.second_number % 2 == 0:
            return "\nError: Even root of a negative number is not defined."
        return self.first_number ** (1/self.second_number)
    
    def remainder(self):
        if self.second_number == 0:
            return "\nError: Division by zero is not allowed."
        return self.first_number % self.second_number
