
from physics.vector import Vector2
from physics.body import Body
from physics.world import World

world = World(
    gravity=Vector2(0, 0),
    width=800,
    height=600,
    restitution=0.8
)

ball = Body(
    position=Vector2(790, 300),
    mass=1,
    radius=20,
    velocity=Vector2(100, 0)
)

world.add_body(ball)

for _ in range(10):
    world.step(0.1)

print("Ball position:", ball.position)
print("Ball velocity:", ball.velocity)

assert ball.position.x <= 780
print("Boundary test passed!")
