import math

#Ask user to enter lengths of three sides of a triangle
a = float(input("Enter length of the 1st side of a triangle: "))
b = float(input("Enter length of the 2nd side of a triangle: "))
c = float(input("Enter length of the 3rd side of a triangle: "))

#check if entered values can form a triangle:
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print ("Entered values do not form a triangle!")
# if lengths form a triangle, proceed with calculations:
else:
#calculate area of the triangle:
    s = (a + b + c) / 2
    area = math.sqrt((s * (s - a)) * (s - b) * (s - c))
    print(f"Area of the triangle is {area} square units")