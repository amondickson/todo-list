import sqlite3
import sys
from datetime import datetime
from tabulate import tabulate
from colorama import Fore, Style
from pyfiglet import Figlet

# Database connection and cursor creation
conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create table (if it doesn't exist)
cursor.execute('''CREATE TABLE IF NOT EXISTS todo_items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  set_date DATE DEFAULT CURRENT_DATE,
  completion_date DATE,             
  completed BOOLEAN DEFAULT FALSE,
  notes TEXT
)''')

def print_header(message):
    """Prints the header with specified message."""
    f = Figlet(font='slant')
    header = f.renderText(message)
    print(Fore.BLUE + header + Style.RESET_ALL)

def add_task(title):
    """Adds a new task to the to-do list."""
    current_date = datetime.now().date()
    completion_date = input("Enter task completion date (YYYY-MM-DD): ")
    try:
        completion_date = datetime.strptime(completion_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    if completion_date < current_date:
        print(Fore.RED + "You cannot set a completion date in the past." + Style.RESET_ALL)
        return

    notes = input("Enter quick notes for the task: ")

    cursor.execute("SELECT COUNT(*) FROM todo_items")
    task_count = cursor.fetchone()[0]
    new_task_id = task_count + 1

    cursor.execute("INSERT INTO todo_items (id, title, completion_date, notes) VALUES (?, ?, ?, ?)",
                   (new_task_id, title, completion_date, notes))
    conn.commit()
    print(Fore.GREEN + f"Task '{title}' added successfully with ID {new_task_id}, completion date {completion_date}, and notes '{notes}'." + Style.RESET_ALL)

def get_tasks(completed=False):
    """Gets all tasks from the to-do list, optionally filtering by completion status."""
    if completed:
        cursor.execute("SELECT * FROM todo_items WHERE completed = ?", (True,))
    else:
        cursor.execute("SELECT * FROM todo_items")
    tasks = cursor.fetchall()
    return tasks

def print_tasks(tasks):
    """Prints a list of tasks using tabulate for a more organized format."""
    if not tasks:
        print(Fore.YELLOW + "No tasks found." + Style.RESET_ALL)
    else:
        headers = [Fore.CYAN + "TASK ID", "TASK NAME", "SET DATE", "COMPLETION DATE", "TASK STATUS", "NOTES" + Style.RESET_ALL]
        task_data = [(task[0], task[1], task[2], task[3], Fore.GREEN + 'Completed' + Style.RESET_ALL if task[4] else Fore.RED + 'Incomplete' + Style.RESET_ALL, task[5]) for task in tasks]
        print(tabulate(task_data, headers=headers, tablefmt="grid"))

def update_task(id, completed):
    """Marks a task as completed or incomplete."""
    cursor.execute("UPDATE todo_items SET completed = ? WHERE id = ?", (completed, id))
    conn.commit()
    print(Fore.GREEN + f"Task '{id}' marked as {'completed' if completed else 'incomplete'}" + Style.RESET_ALL)

def delete_task(id):
    """Deletes a task from the to-do list."""
    cursor.execute("DELETE FROM todo_items WHERE id = ?", (id,))
    conn.commit()
    print(Fore.GREEN + f"Task '{id}' deleted successfully!" + Style.RESET_ALL)

def view_all_tasks():
    """Prints all tasks, allowing the user to select one by ID."""
    tasks = get_tasks()
    print_tasks(tasks)

def main_menu():
    """Displays the main menu and handles user input."""
    print_header("TO-DO LIST")
    while True:
        print("\n1. Add a task")
        print("2. View all tasks")
        print("3. View completed tasks")
        print("4. Mark a task as completed")
        print("5. Delete a task")
        print("6. Exit")

        choice = input("Input option: ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            break  # Exit the inner loop if a valid choice is entered
        else:
            print(Fore.RED + "Invalid option. Please you can only select from the options 1-6." + Style.RESET_ALL)

    if choice == '1':
        title = input("Enter task title: ")
        add_task(title)
    elif choice == '2':
        tasks = get_tasks()
        print_tasks(tasks)
    elif choice == '3':
        tasks = get_tasks(completed=True)
        print_tasks(tasks)
    elif choice == '4':
        view_all_tasks()  # Let user view all tasks before selecting one to mark
        id = int(input("Enter task ID to mark as completed: "))
        update_task(id, True)
    elif choice == '5':
        view_all_tasks()  # Let user view all tasks before selecting one to delete
        id = int(input("Enter task ID to delete: "))
        delete_task(id)
    elif choice == '6':
        print(Fore.YELLOW + "Exiting to-do list..." + Style.RESET_ALL)
        close = input("Are you sure you want to close this application? yes/press any key to continue: ").lower()
        while close == "yes":
            print(Fore.YELLOW + "Closed!!!" + Style.RESET_ALL)
            sys.exit()    

# Call the main menu function to start the program
while True:
    main_menu()

# Close the database connection after exiting the loop
conn.close()
