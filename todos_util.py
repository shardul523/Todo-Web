TODOS_FILE = "todos.txt"


def get_todos():
    try:
        with open(TODOS_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def set_todos(todos):
    with open(TODOS_FILE, "w") as file:
        file.writelines(todos)
