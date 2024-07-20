from tabulate import tabulate
import sys
import csv


def main():
    file_name = check_arguments(sys.argv)
    headers, table = get_headers_and_table(file_name)

    print(tabulate(table, headers, tablefmt="grid"))


def check_arguments(arguments: list):
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    elif len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    elif not arguments[1].endswith(".csv"):
        sys.exit("Error: Not a CSV file")
    elif arguments[1].startswith("../"):
        sys.exit("Error: File not in current directory")
    else:
        return arguments[1]


def get_headers_and_table(file_name: str):
    table = []

    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            headers = next(reader)
            table = [row for row in reader]

    except FileNotFoundError:
        sys.exit(f"Error: File '{file_name}' not found")

    except csv.Error as e:
        sys.exit(f"Error reading CSV file: {e}")

    return headers, table


if __name__ == "__main__":
    main()
