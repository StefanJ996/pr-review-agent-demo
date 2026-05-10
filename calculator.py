"""Saberi dva broja sa novim funkcijama."""


def add(a: int, b: int) -> int:
    """Saberi dva broja."""
    return a + b


def multiply(a: int, b: int) -> int:
    """Pomnozi dva broja."""
    return a * b


def divide(a, b):
    """Podeli dva broja. Bez type hints, bez null check-a."""
    return a / b


def Calculate_Stuff(X, Y):
    """Lose imenovana funkcija sa lose imenovanim parametrima."""
    result = X + Y
    return result
