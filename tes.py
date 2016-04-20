import sys
with open("test2.py", "w") as file:
    file.write('print("hi")')


sys.stdout = open('file', 'w')
with open("test2.py") as f:
    code = compile(f.read(), "test2.py", 'exec')
    exec(code)
sys.stdout = sys.__stdout__
print('this should print in console')