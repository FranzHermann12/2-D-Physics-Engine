
from physics.vector import Vector2
from physics.body import Body
from physics.rectangle import RectangleBody
from physics.world import World

world = World(gravity=Vector2(0, 9.81))

floor = RectangleBody(
    position=Vector2(200, 200),
    width=300,
    height=30,
    is_static=True
)

ball = Body(
    position=Vector2(200, 170),
    mass=1,
    radius=20,
    is_static=False
)

world.add_body(floor)
world.add_body(ball)

for _ in range(120):
    world.step(1 / 60)

print("Floor position:", floor.position)
print("Ball position:", ball.position)
print("Floor static:", floor.is_static)
print("Ball static:", ball.is_static)
