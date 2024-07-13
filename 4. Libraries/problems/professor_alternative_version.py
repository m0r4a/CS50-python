'''
This is an alternative version of the professor's code.

I decided to keep this code because I though that it was a nice example
about my progress of using dictionaries.

But CS50 wanted to generate the problems while asking for them
instead of generating them all at once so I had to change the code.
'''


from random import randint


def main():
    level = get_level()
    problems = generate_problems(level)
    score = game(problems)
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))

        except ValueError:
            continue

        if level > 0 and level < 4:
            break

    return level


def generate_problems(level):
    problems = {}

    for _ in range(0, 11):
        x = generate_integer(level)
        y = generate_integer(level)
        problems[f"{x} + {y}"] = {'answer': (x + y)}

    return problems


def generate_integer(level):
    if level not in [1, 2, 3]:
        raise ValueError

    if level == 1:
        number_generated = randint(0, 9)
    elif level == 2:
        number_generated = randint(10, 99)
    else:
        number_generated = randint(100, 999)

    return number_generated


def game(problems):
    correct_answers = 0

    for key in problems.keys():
        answer = problems[key]['answer']

        for attempt in range(0, 4):
            if attempt == 3:
                print(f"{key} = {answer}")
                break

            try:
                user_answer = int(input(f"{key} = "))
            except ValueError:
                print("EEE")
                continue

            if user_answer == answer:
                correct_answers += 1
                break
            else:
                print("EEE")

    return correct_answers


if __name__ == "__main__":
    main()
