
# This is a global variable, This is a bad practice because it can lead to confusion and bugs in larger programs.
greeting = "Hello, World! global"

def greet():
    # if we want to refer a global variable inside a function, we can use the global keyword
    global greeting
    greeting = "Hello, World!"


def greetSpanish():
    greeting = "¡Hola, Mundo!"
    print(greeting)


greet()
print(greeting)  # This will print the global variable