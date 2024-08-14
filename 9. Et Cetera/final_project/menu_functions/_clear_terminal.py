import subprocess
import platform


def clear_terminal():
    """
    Clear the terminal screen in a more secure manner.
    """
    if platform.system() == 'Windows':
        subprocess.run('cls', shell=True, check=True)
    else:
        subprocess.run('clear', shell=True, check=True)
