def factorial(number):
    if number == 0:
        result = 1
    else:
        result = number * factorial(number - 1)

    return result
