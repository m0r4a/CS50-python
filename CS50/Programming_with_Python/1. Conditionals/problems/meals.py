def main():

    time = input("What time is it?")

    if len(time.split(" ")) == 2:
        hourAndMeridiem = time.split(" ")

        hour_12 = convert(hourAndMeridiem[0])
        meridiem = hourAndMeridiem[1]

        if 7 <= hour_12 <= 8 and meridiem.startswith("a"):
            print("breakfast time")

        if 0 <= hour_12 <= 1 and meridiem.startswith("p"):
            print("lunch time")

        if 6 <= hour_12 <= 7 and meridiem.startswith("p"):
            print("dinner time")

    else:

        hour_24 = convert(time)

        if 7 <= hour_24 <= 8:
            print("breakfast time")

        if 12 <= hour_24 <= 13:
            print("lunch time")

        if 18 <= hour_24 <= 19:
            print("dinner time")


def convert(time):
    hour = time.split(":")
    minutes_to_number = float(hour[1]) / 60

    return minutes_to_number + float(hour[0])


if __name__ == "_main_":
    main()
