# Internal functions
from ._clear_terminal import clear_terminal
from ._print_project_info import print_project_info

# External functions
from rich.panel import Panel
from rich.console import Console
from random import choice


def show_random_project(projects_dict, STYLES):
    """
    Show a random project from the projects dictionary.

    :param projects_dict: Dictionary with the projects.
    :type projects_dict: dict
    :param STYLES: Dictionary with the styles
    :type STYLES: dict
    """

    console = Console()

    clear_terminal()
    if not projects_dict:
        console.print("[red]No projects available.[/red]")
        return

    random_project = choice(list(projects_dict.values()))
    console.print(Panel("Random Project", style=STYLES["header"]))
    print_project_info(random_project, STYLES)
