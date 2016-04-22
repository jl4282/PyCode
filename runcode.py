import sys
from io import StringIO
import os


def run_code(code):

    code_file = 'code_to_run.py'
    with open(code_file, "w") as file:
        file.write(code)
    # sys.stdout = open('file', 'w')
    
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    with open(code_file) as f:
        try:
            os.system('virtualenv venv')
            os.system('source venv/bin/activate')
            code = compile(f.read(), code_file, 'exec')
            exec(code)
            os.system('deactivate')
            os.system('rm -r venv')
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