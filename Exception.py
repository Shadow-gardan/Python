# Exception handling in python 

#Exception handling in Python is a mechanism to respond to runtime errors and ensure that the program can continue or fail gracefully rather than crashing.

#   Exception           | Description                         |
# | ------------------- | ----------------------------------- |
# | `ZeroDivisionError` | Division by zero                    |
# | `TypeError`         | Wrong type of argument or operation |
# | `ValueError`        | Invalid value                       |
# | `IndexError`        | Index out of range                  |
# | `KeyError`          | Dictionary key not found            |
# | `FileNotFoundError` | File does not exist                 |
# | `AttributeError`    | Invalid object attribute access     |


class exception :

    def __init__(self,x,y):
        x = 10
        y = 0

    try:
        print("Error")
        
       
    except:
        print("not errar")  