
from physics.vector import Vector2

POSITION_SLOP = 0.01
POSITION_CORRECTION = 0.8


def apply_impulse(a, b, normal, restitution=0.8):
    inv_a = a.inverse_mass
    inv_b = b.inverse_mass
    inv_sum = inv_a + inv_b

    if inv_sum == 0:
        return

    relative_velocity = b.velocity - a.velocity
    velocity_normal = relative_velocity.dot(normal)

    if velocity_normal > 0:
        return

    effective_restitution = (
        restitution if abs(velocity_normal) > 1.0 else 0.0
    )

    impulse_size = -(1 + effective_restitution) * velocity_normal / inv_sum
    impulse = normal * impulse_size

    a.velocity -= impulse * inv_a
    b.velocity += impulse * inv_b


def correct_positions(a, b, normal, penetration):
    inv_a = a.inverse_mass
    inv_b = b.inverse_mass
    inv_sum = inv_a + inv_b

    if inv_sum == 0:
        return

    correction_amount = (
        max(penetration - POSITION_SLOP, 0)
        * POSITION_CORRECTION
        / inv_sum
    )

    correction = normal * correction_amount

    a.position -= correction * inv_a
    b.position += correction * inv_b


def resolve_circle_collision(a, b, restitution=0.8, friction=0.3):
    difference = b.position - a.position
    distance = difference.magnitude()
    minimum_distance = a.radius + b.radius

    if distance >= minimum_distance:
        return False

    normal = (
        Vector2(1, 0)
        if distance == 0
        else difference / distance
    )

    correct_positions(a, b, normal, minimum_distance - distance)
    apply_impulse(a, b, normal, restitution)

    return True


def resolve_rectangle_collision(a, b, restitution=0.8, friction=0.3):
    a_left, a_top, a_right, a_bottom = a.get_bounds()
    b_left, b_top, b_right, b_bottom = b.get_bounds()

    overlap_x = min(a_right, b_right) - max(a_left, b_left)
    overlap_y = min(a_bottom, b_bottom) - max(a_top, b_top)

    if overlap_x <= 0 or overlap_y <= 0:
        return False

    if overlap_x < overlap_y:
        normal = Vector2(
            1 if a.position.x < b.position.x else -1, 0
        )
        penetration = overlap_x
    else:
        normal = Vector2(
            0, 1 if a.position.y < b.position.y else -1
        )
        penetration = overlap_y

    correct_positions(a, b, normal, penetration)
    apply_impulse(a, b, normal, restitution)

    return True


def resolve_circle_rectangle(circle, rectangle, restitution=0.8):
    """Resolve circle-rectangle collision with stable contact handling."""

    left, top, right, bottom = rectangle.get_bounds()

    closest_x = max(left, min(circle.position.x, right))
    closest_y = max(top, min(circle.position.y, bottom))

    difference = Vector2(
        circle.position.x - closest_x,
        circle.position.y - closest_y
    )

    distance = difference.magnitude()

    if distance >= circle.radius:
        return False

    if distance > 0.000001:
        normal = difference / distance
        penetration = circle.radius - distance

    else:
        distances = [
            (abs(circle.position.x - left), Vector2(-1, 0)),
            (abs(right - circle.position.x), Vector2(1, 0)),
            (abs(circle.position.y - top), Vector2(0, -1)),
            (abs(bottom - circle.position.y), Vector2(0, 1)),
        ]

        edge_distance, normal = min(
            distances,
            key=lambda item: item[0]
        )

        penetration = circle.radius + edge_distance

    inverse_circle = circle.inverse_mass
    inverse_rectangle = rectangle.inverse_mass
    inverse_sum = inverse_circle + inverse_rectangle

    if inverse_sum == 0:
        return False

    # Correct the positions.
    correction_amount = (
        max(penetration - POSITION_SLOP, 0) / inverse_sum
    )

    circle.position += (
        normal * correction_amount * inverse_circle
    )

    rectangle.position -= (
        normal * correction_amount * inverse_rectangle
    )

    # Apply an impulse only when moving into the surface.
    relative_velocity = circle.velocity - rectangle.velocity
    velocity_normal = relative_velocity.dot(normal)

    if velocity_normal < -1.0:
        impulse_size = (
            -(1 + restitution) * velocity_normal / inverse_sum
        )

        impulse = normal * impulse_size

        circle.velocity += impulse * inverse_circle
        rectangle.velocity -= impulse * inverse_rectangle

    return True


def check_aabb_collision(a, b):
    """Check whether two axis-aligned rectangles overlap."""

    a_left, a_top, a_right, a_bottom = a.get_bounds()
    b_left, b_top, b_right, b_bottom = b.get_bounds()

    return (
        a_left < b_right
        and a_right > b_left
        and a_top < b_bottom
        and a_bottom > b_top
    )
