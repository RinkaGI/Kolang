### KOLANG PROGRAMMING LANGUAGE: PYTHON WITH BASIC SYNTAX

# Import sys
from sys import *

# Open file function
def open_file(filename):
    data = open(filename, 'r').read()
    return data

# Parse function, this is for execute the code
def parse(filecontents):
    code = ""

    # Print function
    if "PRINT " in filecontents:
        code = filecontents.replace("PRINT ", "") # Change print to space
        code = code.replace("\n", "") # And space and more.
        code = code.replace("\"", "")

        # Semicolon code
        if ";" in code:
            code = code[:-1] # Quit the last character
            if "; " in code:
                code = code.replace("; ", "\n") # For you can do: PRINT "HELLO"; PRINT " WORLD";
            else:
                code = code.replace(";", "\n")

    # return code parsed
    if code is not None:
        return code
    else:
        return ""

def run():
    # Run code
    data = open_file(argv[1])
    print(parse(data))

run()
