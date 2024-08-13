import argparse


def parse_arguments():
    """
    Parse the arguments passed to the script

    :return: the path to the PROJECTS file
    :rtype: str
    """

    parser = argparse.ArgumentParser(
        description="Script to view and pick a random project from your projects table")
    parser.add_argument("-f", "--file", help="Path to the PROJECTS file")
    return parser.parse_args().file
