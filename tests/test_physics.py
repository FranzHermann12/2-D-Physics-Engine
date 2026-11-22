
import unittest

from physics.vector import Vector2
from physics.body import Body
from physics.rectangle import RectangleBody
from physics.collision import (
    resolve_circle_collision,
    resolve_circle_rectangle,
    check_aabb_collision,
)
from physics.world import World


class TestVector2(unittest.TestCase):

    def test_addition(self):
        result = Vector2(2, 3) + Vector2(4, 5)
        self.assertEqual(result.x, 6)
        self.assertEqual(result.y, 8)

    def test_magnitude(self):
        vector = Vector2(3, 4)
        self.assertAlmostEqual(vector.magnitude(), 5)


class TestBody(unittest.TestCase):

    def test_force_and_movement(self):
        body = Body(
            position=Vector2(0, 0),
            mass=2
        )

        body.apply_force(Vector2(10, 0))
        body.update(1)

        self.assertAlmostEqual(body.velocity.x, 5)
        self.assertAlmostEqual(body.position.x, 5)

    def test_static_body_does_not_move(self):
        body = Body(
            position=Vector2(10, 20),
            is_static=True
        )

        body.apply_force(Vector2(100, 100))
        body.update(1)

        self.assertEqual(body.position.x, 10)
        self.assertEqual(body.position.y, 20)


class TestCollisions(unittest.TestCase):

    def test_circle_collision(self):
        a = Body(
            position=Vector2(0, 0),
            radius=10,
            velocity=Vector2(10, 0)
        )

        b = Body(
            position=Vector2(15, 0),
            radius=10,
            velocity=Vector2(-10, 0)
        )

        result = resolve_circle_collision(
            a, b, restitution=1.0
        )

        self.assertTrue(result)
        self.assertAlmostEqual(a.velocity.x, -10)
        self.assertAlmostEqual(b.velocity.x, 10)

    def test_circle_rectangle_collision(self):
        circle = Body(
            position=Vector2(0, -8),
            radius=10,
            velocity=Vector2(0, 10)
        )

        rectangle = RectangleBody(
            position=Vector2(0, 0),
            width=50,
            height=10,
            is_static=True
        )

        result = resolve_circle_rectangle(
            circle, rectangle, restitution=0.8
        )

        self.assertTrue(result)
        self.assertLess(circle.velocity.y, 0)

    def test_aabb_collision(self):
        a = RectangleBody(
            position=Vector2(0, 0),
            width=20,
            height=20
        )

        b = RectangleBody(
            position=Vector2(15, 0),
            width=20,
            height=20
        )

        c = RectangleBody(
            position=Vector2(50, 0),
            width=20,
            height=20
        )

        self.assertTrue(check_aabb_collision(a, b))
        self.assertFalse(check_aabb_collision(a, c))


class TestWorld(unittest.TestCase):

    def test_gravity(self):
        world = World(
            gravity=Vector2(0, 100),
            width=800,
            height=600
        )

        body = Body(
            position=Vector2(100, 100)
        )

        world.add_body(body)
        world.step(1 / 60)

        self.assertGreater(body.velocity.y, 0)

    def test_add_and_remove_body(self):
        world = World()
        body = Body(position=Vector2(100, 100))

        world.add_body(body)
        self.assertIn(body, world.bodies)

        world.remove_body(body)
        self.assertNotIn(body, world.bodies)


if __name__ == "__main__":
    unittest.main()
