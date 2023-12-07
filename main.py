from Graphics import rectangle
from Graphics import circle
from Graphics.Graphics3d import cuboid, sphere


print("\n")
a1=rectangle.rectanglearea(4,5)
print("Area of rectangle : ",a1)
a2=rectangle.rectperimeter(4,5)
print("Perimeter of rectangle : ",a2)
print("\n")

b1=circle.circlearea(4)
print("Area of the circle : ",b1)
b2=circle.circleperimeter(4)
print("Perimeter of the circle : ",b2)
print("\n")

print("\n")
c1=cuboid.cuboidarea(4,5,6)
print("Area of cuboid : ",c1)
c2=cuboid.cuboidperimeter(4,5,6)
print("Perimeter of cuboid : ",c2)
print("\n")

print("\n")
d1=sphere.spherearea(7)
print("Area of sphere : ",d1)
d2=sphere.spherperimeter(7)
print("Perimeter of sphere : ",d2)
print("\n")