from graphics.rectangle import area as ra, perimeter as rp
from graphics.circle import area as ca, perimeter as cp
from graphics.three.cuboid import area as cua, perimeter as cup
from graphics.three.sphere import area as sa, perimeter as sp

print("Rectangle area:", ra(10, 5))
print("Rectangle perimeter:", rp(10, 5))

print("\nCircle area:", ca(7))
print("Circle perimeter:", cp(7))

print("\nCuboid area:", cua(2, 3, 4))
print("Cuboid perimeter:", cup(2, 3, 4))

print("\nSphere area:", sa(5))
print("Sphere perimeter:", sp(5))
