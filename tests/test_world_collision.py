
from physics.vector import Vector2
from physics.body import Body
from physics.world import World

# Create a world without gravity
world = World(
    gravity=Vector2(0, 0),
    restitution=1.0
)

# Create two approaching balls
ball_a = Body(
    Vector2(100, 100),
    mass=2,
    radius=20,
    velocity=Vector2(50, 0)
)

ball_b = Body(
    Vector2(130, 100),
    mass=2,
    radius=20,
    velocity=Vector2(-50, 0)
)

world.add_body(ball_a)
world.add_body(ball_b)

print("Before simulation:")
print("Ball A:", ball_a.velocity)
print("Ball B:", ball_b.velocity)

# Advance the physics world
world.step(0.01)

print("\nAfter simulation:")
print("Ball A:", ball_a.velocity)
print("Ball B:", ball_b.velocity)

print("\nCollision handled automatically!")
