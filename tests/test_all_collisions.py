
from physics.vector import Vector2
from physics.body import Body
from physics.rectangle import RectangleBody
from physics.world import World

world = World(gravity=Vector2(0, 0), restitution=0.8)

# Circle
circle = Body(
    position=Vector2(100, 100),
    mass=1,
    radius=20,
    velocity=Vector2(50, 0)
)

# Rectangle
rectangle = RectangleBody(
    position=Vector2(130, 100),
    width=60,
    height=60,
    mass=1
)

world.add_body(circle)
world.add_body(rectangle)

print("Before collision:")
print("Circle velocity:", circle.velocity)
print("Rectangle velocity:", rectangle.velocity)

world.step(0.01)

print("\nAfter collision:")
print("Circle velocity:", circle.velocity)
print("Rectangle velocity:", rectangle.velocity)

print("\nCircle-rectangle collision test completed!")
