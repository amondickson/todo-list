**To-Do List Application**

This is a simple command-line To-Do List application written in Python. It allows users to manage their tasks effectively by adding, viewing, marking as completed, and deleting tasks.

**Features**
Add Task: Users can add new tasks to the to-do list, specifying the task title, completion date, and optional notes.
View Tasks: Users can view all tasks in the to-do list, as well as filter tasks by completion status (completed or incomplete).
Mark as Completed: Users can mark a task as completed, updating its status accordingly.
Delete Task: Users can delete a task from the to-do list.
Simple Interface: The application provides a simple and intuitive command-line interface for easy interaction.

**Installation**
Clone the repository to your local machine:
git clone https://github.com/amondickson/todo-list.git
Navigate to the project directory:
cd todo-list

**Usage**
Make sure to activate your virtual environment.
Run the todo.py script to start the application:
python todo.py
Follow the on-screen instructions to navigate through the application menu.

**Terminal Compatibility**
This To-Do List application relies on color support in the terminal for an enhanced user experience. It utilizes ANSI escape codes for color rendering.

**Recommended Terminal Emulators**
Windows Termina
iTerm2
GNOME Terminal

**Checking Terminal Compatibility**
To ensure your terminal emulator supports ANSI escape codes and color rendering, you can run the following command:

echo -e "\033[38;5;1mTest\033[0m"

If "Test" is displayed in red, your terminal emulator supports color rendering.

**Dependencies**
sqlite3: For interacting with SQLite database.
colorama: For colored text output in the terminal.
tabulate: For formatting data into tables.
pyfiglet: For generating ASCII art text.
datetime: For working with dates and times.

**Contributing**
Contributions are welcome! If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Please ensure that your code follows the project's coding style and conventions.

**License**
This project is licensed under the [toDO_List](LICENSE).

**Credits**
This To-Do List application was created by Amon Dickson.

