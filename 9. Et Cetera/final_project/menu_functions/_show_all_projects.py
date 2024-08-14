# Internal function
from ._print_project_info import print_project_info
from ._clear_terminal import clear_terminal

# Rich
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

# Prompt Toolkit
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.formatted_text import HTML


console = Console()


def show_all_projects(projects_dict, STYLES):
    """
    Display all projects in a table format.

    :pram projects_dict: A dictionary containing all projects.
    :type projects_dict: dict
    :param STYLES: Dictionary with the styles
    :type STYLES: dict
    """

    clear_terminal()
    console.print(Panel("Projects List", style=STYLES["header"]))
    table = Table(show_header=True, header_style=STYLES["table_header"])
    table.add_column("#", style="dim", width=3, justify="center")
    table.add_column("Name", min_width=20, style=STYLES["table"])

    project_names = list(projects_dict.keys())
    for index, project_name in enumerate(project_names, 1):
        table.add_row(str(index), project_name)

    console.print(table)

    session = PromptSession()
    completer = FuzzyWordCompleter(project_names)

    while True:
        try:
            selected_project = session.prompt(
                HTML(
                    "<ansiblue>Search for a project (or 'back' to return to menu): </ansiblue>"),
                completer=completer
            )

            if selected_project.lower() in ('back', '', 'exit'):
                clear_terminal()
                return

            if selected_project in projects_dict:
                clear_terminal()
                print_project_info(projects_dict[selected_project], STYLES)
                console.print(Panel("Projects List", style=STYLES["header"]))
                console.print(table)

            else:
                console.print(
                    "[red]Project not found. Please try again.[/red]")
        except KeyboardInterrupt:
            clear_terminal()
            return
