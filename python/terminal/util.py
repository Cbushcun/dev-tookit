import os
import subprocess
import shutil

def clear_terminal():
    if os.name == 'posix':
        subprocess.run('clear')
    else:
        subprocess.system('cls')

def get_terminal_dimensions():
    """
    Gets the dimentions of the terminal and returns an array of two integers represening the length and width of the terminal in columns and lines.
    """
    try:
        dimentions = shutil.get_terminal_size((80, 24))
        return [dimentions.columns, dimentions.lines]
        
    except Exception as e:
        print("Error: get_terminal_dimensions failure")
        