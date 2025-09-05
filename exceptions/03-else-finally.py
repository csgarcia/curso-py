try:
    n1 = int(input("Enter a number: "))
    # sdada # This is a NameError
except Exception as e:
    print("Invalid input. Please enter a valid integer.")
else:  # this block executes if no exceptions were raised
    print("Valid input received:", n1)
finally:  # this block always executes
    print("Execution completed.")
