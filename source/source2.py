"""
:mod:`source.source2` -- get_quadrilateral_type source code
============================================

The following code determines if a set of 4 sides of a quadrilateral is square, rectangle, or other/invalid
"""

def get_quadrilateral_type(a=0, b=0, c=0, d=0):
    """
    Determine if the given quadrilateral is a rectangle or square

    :param a: line a
    :type a: float

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :return: "rectangle", "square", or "other_or_invalid"
    :rtype: str
    """
    if a == b and b == c and c == d:
        return "square"
    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        return "rectangle"
    else:
        return "other_or_invalid"