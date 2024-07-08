import re


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    pattern = re.compile(r"\d+.\d")
    formattedNumber = pattern.search(d).group(0)
    floatNumber = float(formattedNumber)

    return floatNumber


def percent_to_float(p):
    pattern = re.compile(r"\d\d")
    cleanNumber = int(pattern.search(p).group(0))
    correctNumber = cleanNumber / 100

    return correctNumber


main()
