from premuim_calculator import PremiumCalculator

def run_calculator():
    print(f"""Welcome! I'm a simple calculator. 
{ "-" * 50 }
    Choose an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Power (**)
    6. Root (sqrt)
    7. Remainder (%)
    8. Exit
{ "-" * 50 }""")

    while True:
        operation = input("Enter your choice (1-8): ")

        if operation == "8":
            print("Thank you for using me! Goodbye!")
            break

        if operation in ["1", "2", "3", "4", "5", "7"]:
            pass

run_calculator()