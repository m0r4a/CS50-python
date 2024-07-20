import sys


def main():
    check_length(sys.argv)

    file_name = sys.argv[1]

    check_python_file(file_name)

    lines = get_lines(file_name)

    print(len(lines))


def check_length(arguments: list):
    if len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")


def check_python_file(file_name: str):
    if not file_name.endswith(".py"):
        sys.exit("Error: Not a Python file")


def get_lines(file_name: str):
    lines = []
    try:
        with open(file_name) as file:
            for line in file:
                if line_is_valid(line):
                    lines.append(line)

    except FileNotFoundError:
        sys.exit(f"Error: File '{file_name}' does not exist")
    except Exception as e:
        sys.exit(f"Error: An unexpected error occurred: {e}")

    return lines


def line_is_valid(line: str):
    stripped_line = line.strip()

    if stripped_line == "":
        return False
    elif stripped_line.startswith("#"):
        return False
    else:
        return True


if __name__ == "__main__":
    main()
