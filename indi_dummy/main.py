"""The package is demo package to do a PoC and learn various functionalities provided in Github.
"""

import random


def greet(name):
    """The method greets you with your name with random probability

    Examples:
        >>> greet("Indi")
        Hi, Indi

    Args:
        name: Your name

    Returns:
        Greeting message
    """
    chance = random.random()
    print(f"Hi, {name}" if chance < 0.5 else f"Hola, {name}" if (chance > 0.5) and (chance < 0.8) else f"Bojour, {name}")


def depart(name):
    """The method Deprats you with your name with random probability

    Examples:
        >>> depart("Indi")
        Bye, Indi

    Args:
        name: Your name

    Returns:
        Greeting message
    """
    val = random.random()
    print(f"Bye, {name}" if val < 0.5 else f"adiós, {name}" if (val > 0.5) and (val < 0.8) else f"au revoir, {name}")
