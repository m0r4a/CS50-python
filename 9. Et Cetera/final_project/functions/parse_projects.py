# External function
from re import match as match_function


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
