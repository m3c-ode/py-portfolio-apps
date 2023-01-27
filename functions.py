FILEPATH = "./data/todos.txt"
from typing import List


def showTodos(filepath=FILEPATH):
    """DocString: opens the file containing the lines of todos and returns as a list"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    # for index, todo in enumerate(todos_local):
    #     todo = todo.strip("\n")
    #     # print(index + 1, " - ", todo)
    #     print(f"{index +1} - {todo}")
    return todos_local


def addTodoToFile(todos_arg: List[str], filepath=FILEPATH) -> None:
    """Overwites the file containing todos with the list passed as argument."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# this conditional block act as a guard depending what file is being compiled. Will act as if THIS file is ran. Used for testing
if __name__ == "__main__":
    print("Hello")
