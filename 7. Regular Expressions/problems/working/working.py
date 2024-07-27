import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    hour_1, hour_2 = parse_hour(s)
    hour_1_converted = change_format(hour_1)
    hour_2_converted = change_format(hour_2)
    return f"{hour_1_converted[0]:02}:{hour_1_converted[1]:02} to {hour_2_converted[0]:02}:{hour_2_converted[1]:02}"


def parse_hour(hour: str) -> list[str]:
    pattern = r'^((?:1[0-2])|(?:0?\d)):?([0-6][0-9])? (AM|PM) to ((?:1[0-2])|(?:0?\d)) ?:?([0-5][0-9])? ?(PM|AM)$'

    if matches := re.search(pattern, hour):
        hour_1 = [matches.group(i) for i in range(1, 4)]
        hour_2 = [matches.group(i) for i in range(4, 7)]
        return hour_1, hour_2
    else:
        raise ValueError


def change_format(hour_list: list) -> str:
    hour = int(hour_list[0])
    minutes = hour_list[1]
    meridiem = hour_list[2]

    if minutes == None:
        minutes = 00
    if meridiem == "AM" and hour == 12:
        hour = 0
    elif meridiem == "PM" and hour != 12:
        hour += 12

    return (hour, minutes, meridiem)


if __name__ == "__main__":
    main()
