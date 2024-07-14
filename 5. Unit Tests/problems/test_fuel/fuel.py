def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    fuel = gauge(percentage)
    print(fuel)


def convert(fraction):
    x, y = map(int, fraction.split("/"))

    if y == 0:
        raise ZeroDivisionError
    elif x > y:
        raise ValueError

    percentage = round((x / y) * 100)

    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
