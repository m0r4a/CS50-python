def main():
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()

        if "/" in date:
            slash_split = date.split("/")
            if len(slash_split) == 3 and check_slash_split(slash_split):
                print(format_slash_split(slash_split))
                break

        elif " " in date:
            regular_date_split = date.split(" ")
            if len(regular_date_split) == 3 and check_regular_date_split(regular_date_split, months):
                print(format_regular_date_split(regular_date_split, months))
                break

        print("Invalid date format, please try again.")


def check_slash_split(slash_split):
    try:
        month, day, _ = map(int, slash_split)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except ValueError:
        pass
    return False


def format_slash_split(slash_split):
    month, day, year = map(int, slash_split)
    return f"{year:04}-{month:02}-{day:02}"


def check_regular_date_split(regular_date_split, months):
    try:
        month_name = regular_date_split[0]
        day = int(regular_date_split[1].replace(",", ""))
        if month_name in months and 1 <= day <= 31 and "," in regular_date_split[1]:
            return True
    except ValueError:
        pass
    return False


def format_regular_date_split(regular_date_split, months):
    month_name, day_str, year = regular_date_split
    month = months.index(month_name) + 1
    day = int(day_str.replace(",", ""))
    return f"{year:04}-{month:02}-{day:02}"


main()
