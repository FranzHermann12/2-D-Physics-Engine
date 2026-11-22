
from physics.vector import Vector2
from physics.rectangle import RectangleBody
from physics.world import World

world = World(gravity=Vector2(0, 0), restitution=0.8)

rectangle_a = RectangleBody(
    position=Vector2(100, 100),
    width=80,
    height=60,
    mass=1,
    velocity=Vector2(50, 0)
)

rectangle_b = RectangleBody(
    position=Vector2(170, 100),
    width=80,
    height=60,
    mass=1,
    velocity=Vector2(0, 0)
)

world.add_body(rectangle_a)
world.add_body(rectangle_b)

print("Before collision:")
print("A velocity:", rectangle_a.velocity)
print("B velocity:", rectangle_b.velocity)

world.step(0.01)

print("\nAfter collision:")
print("A velocity:", rectangle_a.velocity)
print("B velocity:", rectangle_b.velocity)

print("\nRectangle collision test completed.")
