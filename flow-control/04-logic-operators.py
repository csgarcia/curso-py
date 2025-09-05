# and, or and not operators

gas = True
on = True

if gas and on:
    print("The car is running.")
else:
    print("The car is not running.")


if gas or on:
    print("The car is running.")
else:
    print("The car is not running.")

if not gas:
    print("The car is not running because there is no gas.")


# Operators of short circuiting
age = 18

# this is executed from left to right
# when false is found, the rest of the expression is not evaluated
if not gas and on and age > 17:
    print("The car is running, but you are not allowed to drive.")

# in the case of "or" when a false is found, the rest of the expression is evaluated
