"""
:mod:`source.source2` -- get_quadrilateral_type source code
============================================

The following code determines if a set of 4 sides of a quadrilateral is square, rectangle, or other/invalid
"""

def get_quadrilateral_type(a=0, b=0, c=0, d=0, w=90, x=90, y=90, z=90):
    """
    Determine if the given quadrilateral is a rectangle, square, rhombus, disconnected, or other/invalid

    :param a: line a
    :type a: float

    :param b: line b
    :type b: float

    :param c: line c
    :type c: float

    :param d: line d
    :type d: float

    :param w: angle w
    :type w: float

    :param x: angle x
    :type x: float

    :param y: angle y
    :type y: float

    :param z: angle z
    :type z: float

    :return: "rectangle", "square", or "other_or_invalid"
    :rtype: str
    """
    if w == 90 and x == 90 and y == 90 and z == 90:
        if a == b and b == c and c == d:
            return "square"
        elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
            return "rectangle"
        else:
            return "invalid"
    elif w + x + y + z == 360:
        if w == y and x == z and ((w < 90 and x > 90) or (w > 90 and x < 90)) and a == b and b == c and c == d:
            return "rhombus"
        else:
            return "other"
    else:
        return "disconnected"
