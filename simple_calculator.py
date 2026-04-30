from premuim_calculator import PremiumCalculator

operation = input("Welcome! I'm a simple calculator.\n" + "-" * 50 + "\nEnter operation (+, -, *, /): ")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

calculator = PremiumCalculator(first_number, second_number, operation)

if operation == "+":
    print(f"The result is: {calculator.addition()}")
elif operation == "-":
    print(f"The result is: {calculator.subtraction()}")
elif operation == "*":
    print(f"The result is: {calculator.multiplication()}")
elif operation == "/":
    print(f"The result is: {calculator.division()}")
else:
    print("Invalid operation!")