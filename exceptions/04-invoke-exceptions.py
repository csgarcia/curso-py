def division(n=0):
    if n == 0:
        raise ZeroDivisionError("n cannot be zero", f"{n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    message, value = e.args
    print("Error occurred:", message)
    print("Invalid value:", value)
