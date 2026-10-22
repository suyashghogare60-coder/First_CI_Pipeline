def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total = total + int(digit) ** power

    return total == number


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(is_armstrong(number))