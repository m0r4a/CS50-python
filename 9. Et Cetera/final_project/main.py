# Internal functions
from functions.parse_projects import parse_projects
from functions.parse_arguments import parse_arguments
from functions.open_readme import open_readme
from functions.display_menu import display_menu


def main(file_name=None):
    projects = open_readme(file_name)
    projects_dict = parse_projects(projects)
    display_menu(projects_dict)


if __name__ == "__main__":
    file_name_argument = parse_arguments()
    main(file_name_argument)
