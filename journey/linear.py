"""
journey.linear
~~~~~~~~~~~~~~

A grab-bag of linear–algebra helpers we’ll reuse in later lessons.
For now it holds just one pure function: `vector_dot`.
"""

from __future__ import annotations

from itertools import starmap
from operator import mul


def vector_dot(a: list[float], b: list[float]) -> float:
    """Return the dot-product of two equal-length vectors.

    Parameters
    ----------
    a, b
        Vectors of the *same* length.  Elements can be `int` or `float`
        but will be treated as floats.

    Returns
    -------
    float
        Σᵢ aᵢ × bᵢ

    Raises
    ------
    ValueError
        If the input vectors have different lengths.
    """
    if len(a) != len(b):
        raise ValueError("Vectors must be the same length")

    # Σᵢ aᵢ × bᵢ — `starmap` avoids a one-off temporary list
    return float(sum(starmap(mul, zip(a, b))))
