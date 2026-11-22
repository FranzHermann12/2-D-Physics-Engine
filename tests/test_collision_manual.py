
from physics.vector import Vector2
from physics.body import Body
from physics.collision import resolve_circle_collision

# Create two balls moving towards each other
ball_a = Body(
    position=Vector2(100, 100),
    mass=2,
    radius=20,
    velocity=Vector2(50, 0)
)

ball_b = Body(
    position=Vector2(130, 100),
    mass=2,
    radius=20,
    velocity=Vector2(-50, 0)
)

print("Before collision:")
print("Ball A velocity:", ball_a.velocity)
print("Ball B velocity:", ball_b.velocity)

collided = resolve_circle_collision(
    ball_a,
    ball_b,
    restitution=1.0
)

print("\nCollision detected:", collided)

print("\nAfter collision:")
print("Ball A velocity:", ball_a.velocity)
print("Ball B velocity:", ball_b.velocity)
