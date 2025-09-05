try:
    n1 = int(input("Enter a number: "))
    # sdada # This is a NameError
except ValueError as e:
    print("Invalid input. Please enter a valid integer.")
except NameError as e:
    print("A NameError occurred:", e)
