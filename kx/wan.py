import sys

def trace(frame, event, arg_unused):

    if event == 'line':
        print(frame.f_lineno, event, arg_unused)
    output = sys.stdout
    outputfile = open("D:gzy.txt", "a")
    sys.stdout = outputfile
    print()
    return trace
sys.settrace(trace)

with open('rng.py', "rb") as f:
    source = f.read()
code = compile(source, 'rng.py', 'exec')
exec(code)
