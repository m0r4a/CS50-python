# Internal function
from .styles import STYLES

# External modules
from os import path
import sys
from rich.console import Console


def open_readme(file_name):
    """
    Open the README file and return its content as a list of strings.

    :param file_name: The name of the file to open.
    :type file_name: str
    :raises FileNotFoundError: If the file does not exist.
    :raises Exception: If there is an error reading the file.
    :return: The content of the file as a list of strings.
    :rtype: list
    """

    console = Console()

    script_dir = path.dirname(path.abspath(sys.argv[0]))

    readme_path = path.join(script_dir, file_name or 'PROJECTS.md')

    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        console.print(f"[{STYLES['error']}]Error: File '{
                      readme_path}' not found.[/{STYLES['error']}]")
        raise FileNotFoundError
    except Exception as e:
        console.print(f"[{STYLES['error']}]Error reading file: {
                      str(e)}[/{STYLES['error']}]")
        raise e
