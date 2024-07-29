from re import findall, IGNORECASE


def main():
    print(count(input("Text: ")))


def count(s):
    return len(findall(r"\bum\b", s, IGNORECASE))


if __name__ == "__main__":
    main()
