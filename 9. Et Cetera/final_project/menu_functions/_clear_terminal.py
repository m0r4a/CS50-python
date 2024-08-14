from os import system, name


def clear_terminal():
    """
    Clear the terminal screen
    """

    if name == 'nt':
        system('cls')
    else:
        system('clear')
