def main():
    string = input("Please, input your message: ")
    print(convert(string))


def convert(string):
    firstReplace = string.replace(":)", "🙂")
    secondReplace = firstReplace.replace(":(", "🙁")

    return secondReplace


main()
