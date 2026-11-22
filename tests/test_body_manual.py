from physics.vector import Vector2
from physics.body import Body

# Create a body at position (0, 0)
ball = Body(
    position=Vector2(0, 0),
    mass=2.0,
    radius=10.0
)

# Apply a force of 10 units horizontally
ball.apply_force(Vector2(10, 0))

# Simulate 1 second
ball.update(1.0)

print("Position:", ball.position)
print("Velocity:", ball.velocity)
print("Acceleration:", ball.acceleration)
