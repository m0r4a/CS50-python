# Internal variable
from _clear_terminal import clear_terminal
from .styles import STYLES

from rich.text import Text
from rich.console import Console
from rich.panel import Panel


def print_project_info(project):
    """
    Print the project information in a panel

    :param project: Project object
    :type project
    """

    console = Console()

    info = Text()
    info.append("Name: ", style=STYLES["menu"])
    info.append(f"{project.name}\n")
    info.append("Description: ", style=STYLES["menu"])
    info.append(f"{project.description}\n")
    info.append("Difficulty: ", style=STYLES["menu"])
    info.append(f"{project.difficulty}\n")
    info.append("Status: ", style=STYLES["menu"])
    info.append(project.status)

    console.print(Panel(info, expand=False, border_style=STYLES["border"]))
    input("\nPress Enter to continue...")
    clear_terminal()
