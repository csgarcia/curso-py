class CustomError(Exception):
    "A custom exception class."

    def __init__(self, message, code):
        self.message = message
        self.code = code

    def __str__(self):
        return f"CustomError ({self.code}) {self.message}"


def division(n=0):
    if n == 0:
        raise CustomError("n cannot be zero", 805)
    return 5 / n


try:
    division()
except CustomError as e:
    print("Error occurred:", e)
