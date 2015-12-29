from command_functions.assign_variable import assign_variable
from command_functions.print_data import print_data
from command_functions.call_func_method import call_func_method

# commands that can be called by the user; the first word in the voice command
commands = {"assign": assign_variable,
            "print": print_data,
            "call": call_func_method}