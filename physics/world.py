
from physics.vector import Vector2
from physics.rectangle import RectangleBody

from physics.collision import (
    resolve_circle_collision,
    resolve_rectangle_collision,
    resolve_circle_rectangle,
)


class World:
    """Main 2D physics simulation world."""

    def __init__(
        self,
        gravity=None,
        restitution=0.8,
        friction=0.3,
        width=800,
        height=600,
        solver_iterations=8,
        fixed_delta_time=1 / 120
    ):
        self.gravity = gravity if gravity is not None else Vector2(0, 9.81)
        self.restitution = restitution
        self.friction = friction
        self.width = width
        self.height = height
        self.solver_iterations = solver_iterations
        self.fixed_delta_time = fixed_delta_time
        self.accumulator = 0.0
        self.bodies = []

    def add_body(self, body):
        if body not in self.bodies:
            self.bodies.append(body)

    def remove_body(self, body):
        if body in self.bodies:
            self.bodies.remove(body)

    def _resolve_boundaries(self, body):
        if body.is_static:
            return

        if isinstance(body, RectangleBody):
            left, top, right, bottom = body.get_bounds()
        else:
            left = body.position.x - body.radius
            right = body.position.x + body.radius
            top = body.position.y - body.radius
            bottom = body.position.y + body.radius

        if left < 0:
            body.position.x += -left
            body.velocity.x = abs(body.velocity.x) * self.restitution

        if right > self.width:
            body.position.x -= right - self.width
            body.velocity.x = -abs(body.velocity.x) * self.restitution

        if top < 0:
            body.position.y += -top
            body.velocity.y = abs(body.velocity.y) * self.restitution

        if bottom > self.height:
            body.position.y -= bottom - self.height
            body.velocity.y = -abs(body.velocity.y) * self.restitution

    def _resolve_collisions(self):
        for _ in range(self.solver_iterations):
            for i in range(len(self.bodies)):
                for j in range(i + 1, len(self.bodies)):
                    a = self.bodies[i]
                    b = self.bodies[j]

                    if a.inverse_mass + b.inverse_mass == 0:
                        continue

                    a_rect = isinstance(a, RectangleBody)
                    b_rect = isinstance(b, RectangleBody)

                    if a_rect and b_rect:
                        resolve_rectangle_collision(
                            a, b, self.restitution, self.friction
                        )
                    elif a_rect:
                        resolve_circle_rectangle(b, a, self.restitution)
                    elif b_rect:
                        resolve_circle_rectangle(a, b, self.restitution)
                    else:
                        resolve_circle_collision(
                            a, b, self.restitution, self.friction
                        )

            for body in self.bodies:
                self._resolve_boundaries(body)

    def _step_once(self, delta_time):
        for body in self.bodies:
            if not body.is_static:
                body.apply_force(self.gravity * body.mass)

            body.update(delta_time)

        self._resolve_collisions()

    def step(self, delta_time):
        if delta_time < 0:
            raise ValueError("delta_time cannot be negative.")

        self.accumulator += min(delta_time, 0.1)

        while self.accumulator >= self.fixed_delta_time:
            self._step_once(self.fixed_delta_time)
            self.accumulator -= self.fixed_delta_time

    def clear(self):
        self.bodies.clear()
        self.accumulator = 0.0
