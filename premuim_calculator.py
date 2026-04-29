from basic_calculator import Calculator

class PremiumCalculator(BasicCalculator):
    def __init__(self):
        super().__init__()

    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        return a ** 0.5
    