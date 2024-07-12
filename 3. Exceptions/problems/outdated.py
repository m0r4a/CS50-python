def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

# Recieve: '9/8/1636' or 'September 8, 1636'
# Output: YYYY-MM-DD
# If fail: repeat input
# If win: print and finish

    while True:
        date = input("Date: ").strip()

        slashSplit = date.split("/")
        regularDateSplit = date.split(" ")

        if len(slashSplit) > 2:
            if check_slashSplit(slashSplit):
                format_slashSplit(slashSplit)
                break

        elif len(regularDateSplit) > 2:
            if check_RegularDateSplit(regularDateSplit, months):
                format_RegularDateSplit(regularDateSplit, months)
                break
        else:
            pass


def check_slashSplit(slashSplit):
    try:
        var = bool(int(slashSplit[0]) <= 12 and int(slashSplit[1]) <= 31)

    except ValueError:
        var = False

    return var


def format_slashSplit(slashSplit):
    print(f"{slashSplit[2]}-{int(slashSplit[0]):02}-{int(slashSplit[1]):02}")


def check_RegularDateSplit(regularDateSplit: list[str], months: list[str]):
    try:
        months.index(regularDateSplit[0])

        var = bool("," in regularDateSplit[1]
                   and int(regularDateSplit[2]) <= 31)

    except ValueError:
        var = False

    return var


def format_RegularDateSplit(regularDateSplit: list[str], months: list[str]):
    month_number = (months.index(regularDateSplit[0]) + 1)
    day_number = int(regularDateSplit[1].replace(",", ""))
    print(f"{regularDateSplit[2]}-{month_number:02}-{day_number:02}")


main()
