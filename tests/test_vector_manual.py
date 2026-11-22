from physics.vector import Vector2

a = Vector2(3, 4)
b = Vector2(2, 1)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Magnitude:", a.magnitude())
print("Normalized:", a.normalized())
print("Dot product:", a.dot(b))