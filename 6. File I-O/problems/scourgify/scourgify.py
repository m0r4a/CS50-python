import sys
import csv


def main():
    input_file, output_file = check_arguments(sys.argv)
    students = get_students(input_file)
    create_csv(students, output_file)


def check_arguments(arguments: list):
    if len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    elif len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    elif not arguments[1].endswith(".csv"):
        sys.exit("Error: Input file not a CSV file")
    elif not arguments[2].endswith(".csv"):
        sys.exit("Error: Output file not a CSV file")
    elif arguments[1].startswith("../"):
        sys.exit("Error: File not in current directory")
    else:
        return arguments[1], arguments[2]


def get_students(input_file: str):
    students = []

    try:
        with open(input_file) as file:
            reader = csv.reader(file)
            _ = next(reader)
            for row in reader:
                house = row[1]
                last, first = row[0].split(",")
                students.append([first.strip(), last.strip(), house.strip()])

    except FileNotFoundError:
        sys.exit(f"Error: File '{input_file}' not found")

    except csv.Error as e:
        sys.exit(f"Error reading CSV file: {e}")

    return students


def create_csv(students: list, output_file: str):
    with open(output_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for first, last, house in students:
            writer.writerow({"first": first, "last": last, "house": house})


if __name__ == "__main__":
    main()
