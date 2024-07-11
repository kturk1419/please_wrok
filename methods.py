FILEPATH = "todos.txt"

""""this method is to read the file todos.txt"""
def getTodos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

"""this method is to write at file todos.txt"""
def writeTodos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)
