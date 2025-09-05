def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


sum(2, 5, 7)
