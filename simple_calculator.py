from premuim_calculator import PremiumCalculator

def number_checker(number):
    try:
        return float(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def run_calculator():
    print(f"""Welcome! I'm a simple calculator. 
{ "-" * 50 }
    Choose an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Power (**)
    6. Square Root (sqrt)
    7. Remainder (%)
    8. Exit
{ "-" * 50 }""")

    while True:
        operation = input("Enter your choice (1-8): ")

        if operation == "8":
            print("Thank you for using me! Goodbye!")
            break

        if operation in ["1", "2", "3", "4", "5", "7"]:
            first_number = number_checker(input("Enter the first number: "))
            if first_number is None:
                continue
            second_number = number_checker(input("Enter the second number: "))
            if second_number is None:
                continue
            calculator = PremiumCalculator(first_number, second_number, operation)

            if operation == "1":
                result = calculator.addition()
                print(f"The result of {first_number} + {second_number} is: {result}")
            elif operation == "2":
                result = calculator.subtraction()
                print(f"The result of {first_number} - {second_number} is: {result}")
            elif operation == "3":
                result = calculator.multiplication()
                print(f"The result of {first_number} * {second_number} is: {result}")
            elif operation == "4":
                result = calculator.division()
                print(f"The result of {first_number} / {second_number} is: {result}")
            elif operation == "5":
                result = calculator.power()
                print(f"The result of {first_number} ** {second_number} is: {result}")
            elif operation == "7":
                result = calculator.remainder()
                print(f"The result of {first_number} % {second_number} is: {result}")
        
        elif operation == "6":
            number = number_checker(input("Enter the number: "))
            if number is None:
                continue
            calculator = PremiumCalculator(0, 0, operation)
            result = calculator.square_root(number)
            print(f"The square root of {number} is: {result}")

        else:
            print("Invalid choice. Please try again.")

run_calculator()