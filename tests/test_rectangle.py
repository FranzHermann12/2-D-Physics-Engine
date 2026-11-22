from physics.vector import Vector2
from physics.rectangle import RectangleBody
from physics.collision import check_aabb_collision


rectangle_a = RectangleBody(
    position=Vector2(100, 100),
    width=80,
    height=60
)

rectangle_b = RectangleBody(
    position=Vector2(150, 100),
    width=80,
    height=60
)

rectangle_c = RectangleBody(
    position=Vector2(300, 100),
    width=80,
    height=60
)

print("A and B collide:", check_aabb_collision(rectangle_a, rectangle_b))
print("A and C collide:", check_aabb_collision(rectangle_a, rectangle_c))