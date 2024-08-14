from project import open_readme, parse_project, parse_arguments, Project
from unittest.mock import mock_open, patch
import pytest
import sys


def test_open_readme():
    mock_content = "Line 1\nLine 2\nLine 3\n"

    # Success case
    with patch("builtins.open", mock_open(read_data=mock_content)):
        result = open_readme('README.md')
        assert result == mock_content.splitlines(True)

    # Not existing file
    with patch("builtins.open", side_effect=FileNotFoundError), pytest.raises(FileNotFoundError):
        open_readme('README.md')

    # Read error
    with patch("builtins.open", side_effect=IOError("Simulated read error")), pytest.raises(IOError, match="Simulated read error"):
        open_readme('README.md')


def test_parse_project():
    # Success case
    project_info = "| [Project Name](project-url) | Description of the project | Hard | In Progress |"
    expected_project = Project(
        "Project Name", "Description of the project", "Hard", "In Progress")

    result = parse_project(project_info)
    assert result == expected_project

    # Non matching pattern case
    project_info = "Invalid project info format"
    result = parse_project(project_info)
    assert result is None

    # Empty string
    project_info = ""
    result = parse_project(project_info)
    assert result is None


def test_parse_arguments():
    # Valid argument case
    test_args = ["script_name.py", "-f", "/path/to/projects/file"]

    with patch.object(sys, 'argv', test_args):
        result = parse_arguments()
        assert result == "/path/to/projects/file"

    # No argument case
    test_args = ["script_name.py"]

    with patch.object(sys, 'argv', test_args):
        result = parse_arguments()
        assert result is None

    # Valid argument using a flag with long name
    test_args = ["script_name.py", "--file", "/another/path/to/file"]

    with patch.object(sys, 'argv', test_args):
        result = parse_arguments()
        assert result == "/another/path/to/file"
