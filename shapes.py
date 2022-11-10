import math
"""
    The shapes module makes it easy to calculate the area and volume of various shapes.
    METHODS:
    perimeter
    circumference
    area
    volume
"""
decimal_places = 3


def perimeter(*args):
    """
        PARAMETER(S):
        length of any number of sides separated by commas
    """
    x = [*args]

    for val in x:
        if val <= 0:
            return "Values must be positive numbers"
        if not isinstance(val, (int, float)):
            return "Values must be of type int or float"

    return round(sum(x), decimal_places)


def circumference(r):
    """
        PARAMETERS:
        radius
    """
    if r <= 0:
        return "Radius must be a positive number"
    if not isinstance(r, (int, float)):
        return "Radius must be of type int or float"

    return round(math.pi * (r ** 2), decimal_places)


def area(s, x='1', y='1'):
    """
        PARAMETERS:
        shape (as a string) -- The valid shapes are 'circle', 'rectangle', 'triangle', 'ellipse'/'oval'
        length (or radius if circle, base if triangle, major axis if oval)
        width (or height if triangle, minor axis if oval)
    """

    shapes = {
        'circle': True,
        'triangle': True,
        'square': True,
        'rectangle': True,
        'ellipse': True,
        'oval': True,
    }
    s = s.lower()

    if s not in shapes.keys():
        return f"Function area does not support the shape {s}"

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "Values must be of type int or float"

    if x <= 0 or y <= 0:
        return "Values must be positive numbers"

    if s == 'circle':
        return round(((math.pi * x) ** 2), decimal_places)

    if s == 'triangle':
        return round((.5 * x * y), decimal_places)

    if s == 'square':
        return round((x ** 2), 3)

    if s == 'rectangle':
        return round((x * y), decimal_places)

    if s == 'ellipse' or s == 'oval':
        return round((math.pi * x * y), decimal_places)


def volume(s, x=1, y=1, z=1):
    """
        PARAMETERS:
        shape (as a string) -- The valid shapes are: 'sphere', 'cylinder', 'cube', 'cuboid'
        length (or radius if sphere)
        width (or height if cylinder)
        height
    """
    shapes = {
        'sphere': True,
        'cylinder': True,
        'cube': True,
        'cuboid': True
    }
    s = s.lower()

    if s not in shapes.keys():
        return f"Function volume does not support the shape {s}"

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)) or not isinstance(z, (int, float)):
        return "Values must be of type int or float"

    if x <= 0 or y <= 0 or z <= 0:
        return "Values must be positive numbers"

    if s == 'sphere':
        return round(((4/3) * math.pi) * (x ** 3), decimal_places)

    if s == 'cylinder':
        return round((math.pi * (x ** 2) * y), decimal_places)

    if s == 'cube':
        return round((x ** 3), decimal_places)

    if s == 'cuboid':
        return round((x * y * z), decimal_places)
