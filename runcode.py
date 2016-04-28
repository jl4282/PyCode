import sys
from io import StringIO
import os


def change_stdout(old_f):
    def new_f(*args, **kwargs):
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        old_f(*args, **kwargs)
        sys.stdout = old_stdout
        return mystdout.getvalue()
    return new_f

@change_stdout
def run_code(code, modules):

    code_file = 'code_to_run.py'
    with open(code_file, "w") as file:
        file.write(code)
    # sys.stdout = open('file', 'w')

    with open(code_file) as f:
        try:
            # requires virtualenv to already be installed
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
    # with open("file", 'r') as f:
    #     return f.read()
