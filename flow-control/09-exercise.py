

print("Welcome to the calculator!")
print("The valid operations are (sum, subtract, multiply, divide) or 'exit' to quit")
operation_command = ""  # could be sum, subtract, multiply, divide
first_number = 0
second_number = 0
result = 0

first_number = input("Enter the first number: ")
if first_number.lower() == "exit":
    print("Exiting the calculator.")
    exit()
while True:
    first_number = result if result != 0 else float(first_number)
    operation_command = input("Enter the operation: ")
    if operation_command == "exit":
        print("Exiting the calculator.")
        break
    second_number = input("Enter the next number to operate: ")
    if second_number.lower() == "exit":
        print("Exiting the calculator.")
        break
    second_number = float(second_number)
    if operation_command == "sum":
        result = first_number + second_number
    elif operation_command == "subtract":
        result = first_number - second_number
    elif operation_command == "multiply":
        result = first_number * second_number
    elif operation_command == "divide":
        result = first_number / second_number
    else:
        print("Invalid operation. Please try again.")
        break
 
    print(
        f"The result of {first_number} {operation_command} {second_number} is: {result}")
