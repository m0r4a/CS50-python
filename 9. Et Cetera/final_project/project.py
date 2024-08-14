# Python libraries
from os import path
import sys
import argparse
from re import match as match_function

# Rich library
from rich.console import Console
from rich.style import Style
from rich.panel import Panel
from rich.prompt import Prompt


# Menu functions
from menu_functions._clear_terminal import clear_terminal
from menu_functions._show_all_projects import show_all_projects
from menu_functions._show_random_project import show_random_project


class Project:
    """
    Class to represent a project

    Attributes:
    - name: str
    - description: str
    - difficulty: str
    - status: str
    """

    def __init__(self, name, description, difficulty, status):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, Project):
            return False
        return (self.name == other.name and
                self.description == other.description and
                self.difficulty == other.difficulty and
                self.status == other.status)

    def __repr__(self):
        return (f"Project(name={self.name!r}, description={self.description!r}, "
                f"difficulty={self.difficulty!r}, status={self.status!r})")


STYLES = {
    "header": Style(color="royal_blue1", bold=True),
    "table_header": Style(color="royal_blue1"),
    "table": Style(color="light_steel_blue"),
    "menu": Style(color="light_steel_blue"),
    "border": Style(color="sky_blue2"),
    "error": Style(color="red", bold=True),
    "success": Style(color="green", bold=True),
}


def main(file_name=None):
    projects = open_readme(file_name)
    projects_dict = parse_projects(projects)
    display_menu(projects_dict, STYLES)


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


def parse_projects(projects):
    """
    Parse a list of projects from a list of strings

    :param projects: list
    :type projects: list
    :return: A dictionary of projects
    :rtype: dict
    """
    projects_dict = {}
    for project_info in projects:
        project = parse_project(project_info)
        if project:
            projects_dict[project.name] = project
    return projects_dict


def parse_project(project_info):
    """
    Parse a project from a string

    :param project_info: str
    :type project_info: str
    :return: A project object or None
    :rtype: Project or None
    """

    pattern = r"\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|"
    match = match_function(pattern, project_info)

    if match:
        name = match.group(1)
        description = match.group(3)
        difficulty = match.group(4)
        status = match.group(5)
        return Project(name, description, difficulty, status)
    return None


def display_menu(projects_dict, STYLES):
    """
    Display the main menu of the program

    :param projects_dict: A dictionary containing all the projects
    :type projects_dict: dict
    :param STYLES: A dictionary containing all the styles
    :type STYLES: dict
    """

    console = Console()

    while True:
        try:
            console.print(Panel.fit("Project Manager", style=STYLES["header"]))
            options = [
                ("1", "Show all projects"),
                ("2", "Show a random project"),
                ("3", "Exit")
            ]
            for opt, desc in options:
                console.print(f"[{STYLES['menu']}]{opt}. {
                    desc}[/{STYLES['menu']}]")

            choice = Prompt.ask("Choose an option", choices=[
                                "1", "2", "3", "all", "random", "exit", ""])

            if choice.lower() in ("1", "all"):
                clear_terminal()
                show_all_projects(projects_dict, STYLES)
            elif choice.lower() in ("2", "random"):
                clear_terminal()
                show_random_project(projects_dict, STYLES)
            else:
                console.print(
                    "[green]Thank you for using Project Manager. Goodbye![/green]")
                break
        except KeyboardInterrupt:
            console.print(
                "\n[red]KeyboardInterrupt: Exiting the program...[/red]")
            break


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


if __name__ == "__main__":
    file_name_argument = parse_arguments()
    main(file_name_argument)
