#Relative package imports
from .util import clear_terminal, get_terminal_dimensions

#External package imports
import time
import math

def display_menu(
    options: list[str] = ["Option 1", "Option 2", "Option 3"]
    ):
    """
    Displays a menu in the terminal with the given options. Returns the index of the selected option (int).
     - options: A list of strings representing the menu options.
     - Returns: The index of the selected option (int) with 0 representing the exit option.
     - Note: The menu will continue to display until a valid option is selected or the user chooses to exit by entering 0.
    """
    while True:
        clear_terminal()
        print("\n--- Main Menu ---")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        print("0. Exit")
        
        try:
            choice: int = int(input(f"\nEnter your choice (0-{len(options)}): "))
            if choice == 0:
                clear_terminal()
                return 0
            elif 1 <= choice <= len(options):
                clear_terminal()
                return choice
            else:
                clear_terminal()
                print(f"Invalid selection. Please choose any number from 0 to {len(options)}.")
                time.sleep(2)
                
        except ValueError:
            clear_terminal()
            print("Invalid input. Please enter a number.")
            time.sleep(2)

def display_column_list(
    list_items: list[str],
    enumerate_items: bool = False,
    spacing: int = 20
    ) -> int:
    """
    Takes in a list of items and a defined number of columns to print a list in the terminal in column-major order (in order from top to bottom, left to right). Returns the current page number (int).
     - list_items: A list of strings representing the items to be displayed.
     - enumerate_items: A boolean indicating whether to enumerate the items in the list (default is False). If True, each item will be prefixed with its index in the list (starting from 1) followed by a period and a space (e.g., "001. Item Name").
     - spacing: An integer representing the width of each column (default is 20).
    """
    
    if not list_items:
        return

    clear_terminal()
    terminal_width, terminal_height = get_terminal_dimensions()
    row_count = terminal_height - 3
    col_count = max(1, terminal_width // spacing)

    if row_count < 1:
        row_count = 1
            
    total_items = len(list_items)
    max_items_per_page = col_count * row_count
    if max_items_per_page > total_items:
        total_pages = 1
    else:
        total_pages = math.ceil(total_items / max_items_per_page)
    
    def render_page(page_num):
        """
        Renders the list based off of the terminal dimentions. Returns the current page number (int).
        """
        start_index = page_num * max_items_per_page
        end_index = min(start_index + max_items_per_page, total_items)
        page_items = list_items[start_index:end_index]
        
        grid = [['' for _ in range(col_count)] for _ in range(row_count)]
        
        index = 0
        for col in range(col_count):
            for row in range(row_count):
                if index < len(page_items):
                    if enumerate_items:
                        grid[row][col] = f"{start_index + index + 1:03d}" + ". " + page_items[index]
                    else:
                        grid[row][col] = page_items[index]
                    index += 1
        
        for row in grid:
            row_items = [item for item in row if item]
            if row_items:
                print("".join(f"{item:<{spacing}}" for item in row_items))
    
        return page_num 

    current_page = 0
    running = True
    
    while running:
        clear_terminal()
        current_page = render_page(current_page)
        if total_pages > 1:
            try:
                key = input(f"\nPage {current_page + 1}/{total_pages} | Keys: ',' — Left, '.' — Right, q to quit.\n")
                if key.lower() == 'q':
                    clear_terminal()
                    running = False
                elif key.lower() == ',':
                    current_page -= 1
                    if current_page < 0:
                        current_page = total_pages - 1
                elif key.lower() == '.':
                    current_page += 1
                    if current_page > total_pages - 1:
                        current_page = 0
                        
            except Exception as e:
                print("Error: display_column_list failure")
                time.sleep(2)