# help() and docstrings are two related but distinct concepts:

# Help()
# The help() function is a built-in Python function that provides interactive help for modules, functions, classes, and methods. When you call help() on an object, Python displays the object's docstring, if available, along with other information such as the object's type, module, and attributes.

def greet(name: str) -> None:
    """
    Prints a personalized greeting message.

    Args:
        name (str): The person's name.

    Returns:
        None
    """
    print(f"Hello, {name}!")

help(greet)


# Docstring
# A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Docstrings are used to document the code and provide a description of what the code does.

def greet(name: str) -> None:
    """
    Prints a personalized greeting message.

    Args:
        name (str): The person's name.

    Returns:
        None
    """
print(greet.__doc__)