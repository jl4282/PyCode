import sys
from io import StringIO
def run_code(code):
    with open("test2.py", "w") as file:
        file.write(code)
    # sys.stdout = open('file', 'w')
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    with open("test2.py") as f:
        try:
            code = compile(f.read(), "test2.py", 'exec')
            exec(code)
        except Exception as e:
            # scrub file name
            error = str(e)
            error = error.replace('test2.py, ', '')
            print(error)
    # sys.stdout = sys.__stdout__
        finally:
            sys.stdout = old_stdout
            print('this should print in console')
    return mystdout.getvalue()