FILEPATH = "to-do.txt"

def read_todos(filepath= FILEPATH):
    """
    متن در فایل را می خواند 
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath= FILEPATH):
    """
    یک متن در درون فایل ایجاد می کند
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)