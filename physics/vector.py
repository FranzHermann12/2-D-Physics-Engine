import math


class Vector2:
    """A two-dimensional mathematical vector."""

    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector2(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, scalar):
        return Vector2(
            self.x * scalar,
            self.y * scalar
        )

    def __rmul__(self, scalar):
        return self * scalar

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide a vector by zero.")

        return Vector2(
            self.x / scalar,
            self.y / scalar
        )

    def magnitude(self):
        return math.hypot(self.x, self.y)

    def normalized(self):
        length = self.magnitude()

        if length == 0:
            return Vector2()

        return self / length

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __repr__(self):
        return f"Vector2(x={self.x}, y={self.y})"
