class Calculator:
    def __init__(self, first_number, second_number, operation):
        self.first_number = first_number
        self.second_number = second_number
        self.operation = operation
    
    def addition(self):
        return self.first_number + self.second_number
    
    def subtraction(self):
        return self.first_number - self.second_number
    
    def multiplication(self):
        return self.first_number * self.second_number
    
    def division(self):
        if self.second_number == 0:
            return "Error: Division by zero is not allowed."
        return self.first_number / self.second_number 
        