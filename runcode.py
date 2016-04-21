import sys
from io import StringIO
def run_code(code):
    code_file = 'code_to_run.py'
    with open(code_file, "w") as file:
        file.write(code)
    # sys.stdout = open('file', 'w')
    
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    '''
    TODO: figure out why line breaks aren't working in printing
    TODO: decide whether it's better to write to a line, or keep as string buffer
    '''
    with open(code_file) as f:
        try:
            code = compile(f.read(), "test2.py", 'exec')
            exec(code)
        except Exception as e:
            # scrub file name
            error = str(e)
            error = error.replace('test2.py, ', '')
            print(error)

        finally:
            sys.stdout = old_stdout
            # sys.stdout = sys.__stdout__
            print('this should print in console')
    # with open("file", 'r') as f:
    #     return f.read()


    return mystdout.getvalue()