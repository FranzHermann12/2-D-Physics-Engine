
from physics.body import Body
from physics.vector import Vector2


class RectangleBody(Body):
    """A rectangular physical body."""

    def __init__(
        self,
        position,
        width,
        height,
        mass=1.0,
        velocity=None,
        is_static=False
    ):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")

        super().__init__(
            position=position,
            mass=mass,
            radius=1,
            velocity=velocity,
            is_static=is_static
        )

        self.width = float(width)
        self.height = float(height)

    def get_bounds(self):
        half_width = self.width / 2
        half_height = self.height / 2

        return (
            self.position.x - half_width,
            self.position.y - half_height,
            self.position.x + half_width,
            self.position.y + half_height
        )
