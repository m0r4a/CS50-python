from random import randrange
import sys


def main():

    level = ask_num("Level: ")
    guess = ask_num("Guess: ")

    random_num = randrange(1, level + 1)

    if guess < random_num:
        print("Too small!")
    elif guess > random_num:
        print("Too large!")
    else:
        print("Just right!")
        sys.exit()


def ask_num(prompt: str):
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                pass
            else:
                break

        except ValueError:
            pass
    return number


main()
