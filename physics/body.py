
from physics.vector import Vector2


class Body:
    """A physical circular body."""

    def __init__(
        self,
        position,
        mass=1.0,
        radius=10,
        velocity=None,
        is_static=False
    ):
        if mass <= 0:
            raise ValueError("Mass must be positive.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        self.position = position
        self.mass = float(mass)
        self.radius = float(radius)
        self.velocity = velocity if velocity is not None else Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        self.force = Vector2(0, 0)
        self.is_static = is_static

    @property
    def inverse_mass(self):
        return 0.0 if self.is_static else 1.0 / self.mass

    def apply_force(self, force):
        if not self.is_static:
            self.force += force

    def update(self, delta_time):
        if self.is_static:
            self.force = Vector2(0, 0)
            self.acceleration = Vector2(0, 0)
            self.velocity = Vector2(0, 0)
            return

        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration * delta_time
        self.position += self.velocity * delta_time
        self.force = Vector2(0, 0)
