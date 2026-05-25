#65
# Write a Python program to calculate surface volume and area of a cylinder
import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

volume = math.pi * r * r * h

surface_area = 2 * math.pi * r * (r + h)

print("Volume of cylinder =", volume)
print("Surface area of cylinder =", surface_area)