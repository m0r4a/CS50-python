def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if plate_checker(plate):
        return True
    else:
        return False


def plate_checker(plate):
    return starts_with_two_letters(plate) and right_lenght(plate) and right_numbers(plate) and no_punctuation(plate)


def starts_with_two_letters(plate):
    return plate[:2].isalpha()


def right_lenght(plate):
    return 1 < len(plate) < 7


def right_numbers(plate):
    numbers = ""
    numbers_started = False

    for letter in plate:
        if letter.isnumeric():
            numbers += letter
            numbers_started = True

        if numbers_started and letter.isalpha():
            return False

        var = bool(numbers.startswith("0"))

    return not var


def no_punctuation(plate):
    return plate.isalnum()


main()
