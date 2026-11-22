from physics.vector import Vector2
from physics.body import Body
from physics.world import World

world = World(gravity=Vector2(0, 9.81))

ball = Body(
    position=Vector2(100, 0),
    mass=2.0,
    radius=15
)

world.add_body(ball)

for frame in range(60):
    world.step(1 / 60)

print("Final position:", ball.position)
print("Final velocity:", ball.velocity)
