
"""
An extremely buggy Python math library . . .
"""

# Should this function even be here?

def addition(x: int, y: int) -> int:
    """
    Adds two numbers.

    Note: `+` is the addition operator in Python.

    Args:
        x (int): The first parameter.
        y (int): The second parameter.

    Returns:
        int: The sum of `x` and `y`.
    """
    return x + y

def multiplication(x: int, y: int) -> int:
    """
    Multiplies two numbers.

    Note: `*` is the multiplication operator in Python.

    Args:
        x (int): The first parameter.
        y (int): The second parameter.

    Returns:
        int: The multiple of `x` and `y`.
    """
    return x * y

def division(x: int, y: int) -> int:
    """
    Multiplies two numbers.

    Note: `//` is the *integer* division operator in Python.

    Args:
        x (int): The first parameter.
        y (int): The second parameter.

    Returns:
        int: `x` divided by `y`.
    """
    if y == 0:
        raise ValueError("You can not divide by 0"
    return x // y
