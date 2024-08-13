from .styles import STYLES
from ._show_all_projects import show_all_projects
from ._show_random_project import show_random_project
from ._clear_terminal import clear_terminal


from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt


def display_menu(projects_dict):
    """
    Display the main menu of the program
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
                show_all_projects(projects_dict)
            elif choice.lower() in ("2", "random"):
                clear_terminal()
                show_random_project(projects_dict)
            else:
                console.print(
                    "[green]Thank you for using Project Manager. Goodbye![/green]")
                break
        except KeyboardInterrupt:
            console.print(
                "\n[red]KeyboardInterrupt: Exiting the program...[/red]")
            break
