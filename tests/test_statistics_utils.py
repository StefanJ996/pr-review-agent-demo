"""Tests for statistical helpers."""

import pytest

from statistics_utils import average, median


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([1.0, 2.0, 3.0], 2.0),
        ([-2.0, 2.0], 0.0),
        ([4.0], 4.0),
    ],
)
def test_average_returns_arithmetic_mean(values: list[float], expected: float) -> None:
    assert average(values) == expected


def test_average_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="values must not be empty"):
        average([])


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([3.0, 1.0, 2.0], 2.0),
        ([4.0, 1.0, 2.0, 3.0], 2.5),
        ([-5.0, 10.0, 0.0], 0.0),
    ],
)
def test_median_handles_unsorted_values(values: list[float], expected: float) -> None:
    assert median(values) == expected


def test_median_rejects_empty_input() -> None:
    with pytest.raises(ValueError, match="values must not be empty"):
        median([])
