"""Statistical helpers for reporting examples."""

from collections.abc import Sequence


def average(values: Sequence[float]) -> float:
    """Return the arithmetic mean for a non-empty sequence of values.

    Args:
        values: Numeric values to average.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median for a non-empty sequence of values.

    Args:
        values: Numeric values to inspect.

    Raises:
        ValueError: If values is empty.
    """
    if not values:
        raise ValueError("values must not be empty")

    sorted_values = sorted(values)
    midpoint = len(sorted_values) // 2
    if len(sorted_values) % 2 == 1:
        return float(sorted_values[midpoint])

    lower = sorted_values[midpoint - 1]
    upper = sorted_values[midpoint]
    return (lower + upper) / 2
