import sys
from io import StringIO
import os


def run_code(code, modules):

    code_file = 'code_to_run.py'
    with open(code_file, "w") as file:
        file.write(code)
    # sys.stdout = open('file', 'w')
    
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    with open(code_file) as f:
        try:
            os.system('cd main_interpreter\n virtualenv venv')
            # os.system('virtualenv venv')
            os.system('source main_interpreter/venv/bin/activate')

            # loop through modules and install them
            for mod in modules:
                os.system('pip install ' + mod)

            code = compile(f.read(), code_file, 'exec')
            exec(code)
            os.system('deactivate') # this command isn't working for some reason
            os.system('rm -r main_interpreter/venv')
        except Exception as e:
            # scrub file name
            error = str(e)
            error = error.replace(code_file + ', ', '')
            print(error)

        finally:
            sys.stdout = old_stdout
            # sys.stdout = sys.__stdout__
            print('this should print in console')
    # with open("file", 'r') as f:
    #     return f.read()

    return mystdout.getvalue()