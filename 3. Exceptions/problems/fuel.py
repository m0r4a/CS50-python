def main():
    fraction = get_fraction()
    percentage = get_percentage(fraction)

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:

        fraction = input("Fraction: ")

        try:
            numerator, denominator = map(int, fraction.split("/"))
            if numerator <= denominator and denominator != 0:
                return numerator / denominator

        except (ValueError, ZeroDivisionError):
            pass


def get_percentage(fraction):
    percentage = round((fraction * 100))
    return percentage


main()
