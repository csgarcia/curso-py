n1 = input("Enter first number ")
n2 = input("Enter second number ")

n1 = int(n1)  # Convert input to integer
n2 = int(n2)  # Convert input to integer

sum = n1 + n2
sub = n1 - n2
prod = n1 * n2
div = n1 / n2

message = f"""
For the givin numbers: {n1} and {n2}
The results are:
Sum: {sum}
Subtraction: {sub}
Multiplication: {prod}
Division: {div}
"""

print(message)
