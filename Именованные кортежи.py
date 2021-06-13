from collections import namedtuple
Point = namedtuple("Point", "x y z")
A = Point(1, 0, 3)
print(A.x)