import subprocess


def clear_terminal():
    """
    Clear the terminal screen.
    """
    subprocess.run('/usr/bin/clear', shell=True, check=True)
