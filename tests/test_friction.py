
from physics.vector import Vector2
from physics.body import Body
from physics.world import World

world = World(
    gravity=Vector2(0, 0),
    restitution=1.0,
    friction=0.5
)

ball_a = Body(
    Vector2(100, 100),
    mass=2,
    radius=20,
    velocity=Vector2(50, 10)
)

ball_b = Body(
    Vector2(130, 100),
    mass=2,
    radius=20,
    velocity=Vector2(-50, 0)
)

world.add_body(ball_a)
world.add_body(ball_b)

world.step(0.01)

print("Ball A velocity:", ball_a.velocity)
print("Ball B velocity:", ball_b.velocity)

print("Friction test completed!")
