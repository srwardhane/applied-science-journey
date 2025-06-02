from __future__ import annotations

import math

import pytest

from journey.linear import vector_dot


# ---------- fixtures ---------- #
@pytest.fixture(scope="module")
def unit_vectors() -> list[tuple[list[float], list[float], float]]:
    """Common tiny dataset so we don’t repeat lists everywhere."""
    return [
        ([1.0, 0.0, 0.0], [1.0, 0.0, 0.0], 1.0),
        ([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], 0.0),
        ([1.0, 2.0, 3.0], [4.0, 5.0, 6.0], 32.0),
    ]


# ---------- parametrised tests ---------- #
@pytest.mark.parametrize(
    "a,b,expected",
    [
        ([0.0, 0.0], [0.0, 0.0], 0.0),
        ([1.0], [2.0], 2.0),
        ([-1.0, -2.0], [-3.0, -4.0], 11.0),
    ],
)
def test_vector_dot_param(a: list[float], b: list[float], expected: float) -> None:
    assert math.isclose(vector_dot(a, b), expected)


def test_vector_dot_fixture(
    unit_vectors: list[tuple[list[float], list[float], float]]
) -> None:
    """Reuse the fixture data—shows how fixtures reduce duplication."""
    for a, b, expected in unit_vectors:
        assert math.isclose(vector_dot(a, b), expected)
