from pyfiglet import Figlet
from random import shuffle
import sys


def main():
    if len(sys.argv) == 1:
        string = input("Input: ")
        print_random_font(string)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
        string = input("Input: ")
        print_specified_font(string, sys.argv[2])
    else:
        sys.exit("Invalid usage")


def print_random_font(string: str):
    font_list = figlet.getFonts()
    shuffle(font_list)
    figlet.setFont(font=font_list[0])
    print(figlet.renderText(string))


def print_specified_font(string: str, font: str):
    figlet.setFont(font=font)
    print(figlet.renderText(string))


if __name__ == "__main__":
    figlet = Figlet()
    main()
