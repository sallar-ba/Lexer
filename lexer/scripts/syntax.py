import os

def check_cpp_syntax(code):
    try:
        # Save the code to a file
        with open('temp.cpp', 'w') as file:
            file.write(code)

        # Execute gcc command to check syntax
        result = os.system('gcc -fsyntax-only temp.cpp')

        # Check the return code to determine if the syntax is correct or not
        if result == 0:
            return True
            #print("Syntax check passed. Code is correct.")
        else:
            return False
            #print("Syntax check failed. Code contains errors.")

    finally:
        # Remove the temporary file
        os.remove('temp.cpp')