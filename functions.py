FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Read a file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def update_todos(todos_in, filepath=FILEPATH):
    """ Write the to-do item list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_in)
