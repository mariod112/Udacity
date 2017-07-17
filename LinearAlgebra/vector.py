import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, other):
        return self.coordinates == other.coordinates

    def __add__(self, other):
        iterator = zip(self.coordinates, other.coordinates)
        return Vector([x + y for x, y in iterator])

    def __sub__(self, other):
        iterator = zip(self.coordinates, other.coordinates)
        return Vector([x - y for x, y in iterator])

    def scalar_multiply(self, multiplier):
        return Vector([x * Decimal(multiplier) for x in self.coordinates])

    def magnitude(self):
        squares = [x **2 for x in self.coordinates]
        return Decimal(sum(squares)).sqrt()

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.scalar_multiply(Decimal('1.0')/ magnitude)

        except ZeroDivisionError:
            raise Exception('Invalid input: zero vector')

    def dot_product(self, other):
        return sum([x * y for x, y in zip(self.coordinates, other.coordinates)])

    def angle(self, other):
        dot_product = self.normalize().dot_product(other.normalize())
        return math.acos(dot_product)

    def angle_degrees(self, other):
        return math.degrees(self.angle(other))

    def parallel(self, other):
        return (self.is_zero() or
                other.is_zero() or
                self.angle(other) == 0 or
                self.angle(other) == math.pi)

    def orthogonal(self, other):
        return abs(self.dot_product(other)) < 1e-10

    def is_zero(self):
        return self.magnitude() < 1e-10