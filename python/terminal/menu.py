#Relative package imports
from .util import clear_terminal, get_terminal_dimensions

#External package imports
import time
import math



def display_menu(
    options: list[str] = ["Option 1", "Option 2", "Option 3"]
    ) -> int:
    """
    Displays a menu in the terminal with the given options and prompts the user to select one. The user can also choose to exit the menu by selecting 0. The function will continue to prompt the user until a valid selection is made.
    Args:
        options (list[str]): A list of strings representing the menu options. Default is ["Option 1", "Option 2", "Option 3"].
    Returns:
        choice (int): The index of the user's selected option. Returns 0 if the user chooses to exit.
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
    ) -> int | None:
    """
    Displays a list of items in a column format based on the terminal dimensions. The user can navigate through the pages of the list using ',' and '.' keys, and can exit the display by pressing 'q'.
    Args:
        list_items (list[str]): A list of strings representing the items to be displayed.
        enumerate_items (bool): Whether to enumerate the items in the list. Default is False.
        spacing (int): The number of spaces between columns. Default is 20.
    Returns:
        None
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
        Renders a single page of the list items based on the current page number and terminal dimensions.
        Args:
            page_num (int): The current page number to be rendered.
        Returns:
            page_num (int): The current page number after rendering.
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