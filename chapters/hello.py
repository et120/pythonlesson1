greeting = 'Hello World!'
print(greeting)


# Notes (single hash = single-line comment)

'''
Multiline Comments - Python does not really have a syntax for multiline comments. To add a multiline comment you could insert a # for each line. Or, not quite as intended, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it.


In computer programming, you’ll find two kinds of programming languages: 

1. Compiled languages 
    - Compiled programming languages like C and C++ will have a compiler program, which takes care of translating the language’s code into machine code

2. Interpreted languages
    - This machine code is typically saved into an executable file. Once you have an executable file, you can run your program on any compatible computer system without needing the compiler or the source code.
    - Interpreted languages like Python need an interpreter program (need to have a Python interpreter installed to run Python code on your computer) 
    
Some may consider this characteristic a drawback because it can make your code distribution process much more difficult.
However, in Python, having an interpreter offers one significant advantage that comes in handy during your development and testing process. 

The Python interpreter allows for what’s known as an interactive REPL (Read-Eval-Print Loop), or shell, which reads a piece of code, evaluates it, and then prints the result to the console in a loop.

Python’s REPL is an interactive way to talk to your computer using the Python language.

REPL:

- Reading your input, which consists of Python code as expressions and statements
- Evaluating your Python code, which generates a result or causes side effects
- Printing any output so that you can check your code’s results and get immediate feedback
- Looping back to step one to continue the interaction

Terminal:
py => starts REPL
quit() => quits REPL
'''