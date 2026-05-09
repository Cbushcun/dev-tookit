import os
import subprocess
import shutil

def clear_terminal() -> None:
    if os.name == 'posix':
        subprocess.run('clear')
    else:
        subprocess.system('cls')

def get_terminal_dimensions() -> list[int]:
    """
    Retrieves the current terminal dimensions (width and height) using shutil.get_terminal_size.
    Returns:
        list[int]: A list containing the terminal width and height as integers.
    """
    dimentions = shutil.get_terminal_size((80, 24))
    return [dimentions.columns, dimentions.lines]