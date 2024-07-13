from random import randint


def main():
    level = get_level()
    score = game(level)
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if 1 <= level <= 3:
            return level


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


def game(level):
    correct_answers = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        problem = f"{x} + {y}"

        for attempt in range(3):
            try:
                user_answer = int(input(f"{problem} = "))
            except ValueError:
                print("EEE")
                continue

            if user_answer == answer:
                correct_answers += 1
                break
            else:
                print("EEE")

        if attempt == 2:
            print(f"{problem} = {answer}")

    return correct_answers


if __name__ == "__main__":
    main()
