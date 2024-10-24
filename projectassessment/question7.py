# Triangle Type Checker

# Get the lengths of the triangle sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Determine the type of triangle
if side1 == side2 == side3:
    print("The triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles.")
else:
    print("The triangle is Scalene.")
