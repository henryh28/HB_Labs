"""CLI application for a prefix-notation calculator."""

from audioop import mul
from sys import breakpointhook
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

allowed = {"+": add, "-": subtract, "*": multiply, "/": divide, "square": square, "cube": cube, "pow": power, "mod": mod}

while True:
    equation = input(f"Enter you equation > ")
    # print ("equation: ", equation)

    if equation[0].lower() == 'q':
        print ("Exiting program")
        break

    tokens = equation.split(" ")
    function_to_call = allowed[tokens[0]]

    if tokens[0] in allowed:
        tokens = [int(x) for x in tokens if x.isdigit()]

        print (function_to_call(*tokens))
    else:
        print ("Invalid input, please try again")










