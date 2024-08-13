import os
import argparse
import re
import random
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.style import Style
from rich.prompt import Prompt
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import FuzzyWordCompleter
from prompt_toolkit.formatted_text import HTML

console = Console()

# Define custom styles
STYLES = {
    "header": Style(color="royal_blue1", bold=True),
    "table_header": Style(color="royal_blue1"),
    "table": Style(color="light_steel_blue"),
    "menu": Style(color="light_steel_blue"),
    "border": Style(color="sky_blue2"),
    "error": Style(color="red", bold=True),
    "success": Style(color="green", bold=True),
}


class Project:
    def __init__(self, name, description, difficulty, status):
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.status = status


def main(file_name=None):
    projects = open_readme(file_name)
    projects_dict = parse_projects(projects)
    display_menu(projects_dict)


def parse_projects(projects):
    projects_dict = {}
    for project_info in projects:
        project = parse_project(project_info)
        if project:
            projects_dict[project.name] = project
    return projects_dict


def display_menu(projects_dict):
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


def show_all_projects(projects_dict):
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
                print_project_info(projects_dict[selected_project])
                console.print(Panel("Projects List", style=STYLES["header"]))
                console.print(table)

            else:
                console.print(
                    "[red]Project not found. Please try again.[/red]")
        except KeyboardInterrupt:
            clear_terminal()
            return


def show_random_project(projects_dict):
    clear_terminal()
    if not projects_dict:
        console.print("[red]No projects available.[/red]")
        return

    random_project = random.choice(list(projects_dict.values()))
    console.print(Panel("Random Project", style=STYLES["header"]))
    print_project_info(random_project)


def print_project_info(project):
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


def parse_project(project_info):
    pattern = r"\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|"
    match = re.match(pattern, project_info)

    if match:
        name = match.group(1)
        description = match.group(3)
        difficulty = match.group(4)
        status = match.group(5)
        return Project(name, description, difficulty, status)
    return None


def open_readme(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    readme_path = os.path.join(script_dir, file_name or 'PROJECTS.md')

    try:
        with open(readme_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        console.print(f"[{STYLES['error']}]Error: File '{
                      readme_path}' not found.[/{STYLES['error']}]")
        exit(1)
    except Exception as e:
        console.print(f"[{STYLES['error']}]Error reading file: {
                      str(e)}[/{STYLES['error']}]")
        exit(1)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def process_arguments():
    parser = argparse.ArgumentParser(
        description="Script to view and pick a random project from your projects table")
    parser.add_argument("-f", "--file", help="Path to the PROJECTS file")
    return parser.parse_args().file


if __name__ == "__main__":
    file_name = process_arguments()
    main(file_name)
