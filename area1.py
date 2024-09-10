# Calculate the area of a square

def square_area():
    Size = int(input("Enter the size of your triangle : "))
    area_of_square = Size * Size 
    print(f"The are of the square is {area_of_square} square units.")
    
square_area()











# Calculate the area of a triangle

def triangle_area():
    base = int(input("Enter the base of your triangle : "))
    height = int(input("Enter the height of your triangle : "))
    area_of_triangle = (base * height) / 2
    print(f"The are of the triangle is {area_of_triangle} square units.")
    
triangle_area()