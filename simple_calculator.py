from premium_calculator import PremiumCalculator

def math_problem_txt_reader(file_name):
    with open(file_name, "r") as file, \
        open("results.txt", "w") as results_file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 3:
                print(f"Invalid format in line: {line}. Expected format: first_number, second_number, operation number. Skipping.")
                continue 

            first_number_str, second_number_str, operation = parts

            first_number = number_checker(first_number_str)
            if first_number is None:
                continue

            second_number = number_checker(second_number_str)
            if second_number is None:
                continue

            calculator = PremiumCalculator(first_number, second_number, operation)

            if operation.strip() == "1":
                result = calculator.addition()
                results_file.write(f"{first_number} + {second_number} = {result}\n")
            elif operation.strip() == "2":
                result = calculator.subtraction()
                results_file.write(f"{first_number} - {second_number} = {result}\n")
            elif operation.strip() == "3":
                result = calculator.multiplication()
                results_file.write(f"{first_number} * {second_number} = {result}\n")
            elif operation.strip() == "4":
                result = calculator.division()
                results_file.write(f"{first_number} / {second_number} = {result}\n")
            elif operation.strip() == "5":
                result = calculator.power()
                results_file.write(f"{first_number} ** {second_number} = {result}\n")
            elif operation.strip() == "7":
                result = calculator.remainder()
                results_file.write(f"{first_number} % {second_number} = {result}\n")
            elif operation.strip() == "8":
                result = calculator.radical()
                results_file.write(f"√{first_number} (with index {second_number}) = {result}\n")
            else:
                print(f"Unsupported operation number in line: {line}. Skipping.")

        print("Math problems processed. Results saved to results.txt.")

def number_checker(number):
    try:
        return float(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None

def run_calculator():
    while True:
        operation = input(f"""Welcome! I'm a simple calculator. 
{ "-" * 50 }
    Choose an operation:
    1. Addition (+)
    2. Subtraction (-)
    3. Multiplication (*)
    4. Division (/)
    5. Power (**)
    6. Square Root (sqrt)
    7. Remainder (%)
    8. Radical (√)
    9. Exit
    10. Math problem txt reader (experimental)
{ "-" * 50 }
Enter your choice (1-10): """)
        
        if operation == "9":
            print("Thank you for using me! Goodbye!")
            break

        if operation in ["1", "2", "3", "4", "5", "7", "8"]:
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
                print(f"The remainder of {first_number} / {second_number} is: {result}")
            elif operation == "8":
                result = calculator.radical()
                print(f"The result of √{first_number} (with index {second_number}) is: {result}")
            
        elif operation == "10":
                file_name = input("Enter the file name (with .txt extension only): ")
                if not file_name.endswith(".txt"):
                    print("Invalid file name. Please enter a valid .txt file.")
                    continue
                else:
                    math_problem_txt_reader(file_name)

        elif operation == "6":
            number = number_checker(input("Enter the number: "))
            if number is None:
                continue
            calculator = PremiumCalculator(0, 0, operation)
            result = calculator.square_root(number)
            print(f"The square root of {number} is: {result}")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_calculator()

