from datetime import date
from re import search
from inflect import engine
import sys


def main():
    user_date = date_parser(input("Date of Birth: "))
    time_passed = date.today() - user_date
    minutes = (time_passed.days * 24 * 60)
    worded_minutes = engine().number_to_words(minutes, andword="")
    print(f"{worded_minutes.capitalize()} minutes")


def date_parser(string: str) -> date:
    pattern = r"^(\d{4})-(0\d|1[012])-([012]\d|3[01])$"

    if match := search(pattern, string):
        full_date = [int(match.group(i)) for i in range(1, 4)]
        return date(full_date[0], full_date[1], full_date[2])
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
