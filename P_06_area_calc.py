# ask user for width and height
# (assume they put valid data)
width = float(input("Width: "))
height = float(input("Height: "))

# calc the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# output the area / perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")