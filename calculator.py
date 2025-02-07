"""
An extremely buggy Python math library . . .
"""

def addition(x: int, y: int) -> int:
    """
    Adds two numbers.

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

    Args:
        x (int): The first parameter.
        y (int): The second parameter.

    Returns:
        int: The product of `x` and `y`.
    """
    return x * y

def division(x: int, y: int) -> int:
    """
    Divides two numbers using integer division.

    Args:
        x (int): The first parameter.
        y (int): The second parameter.

    Returns:
        int: `x` divided by `y` (integer division).

    Raises:
        ValueError: If `y` is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x // y
