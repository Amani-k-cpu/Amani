from math import tan, pi


n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))

def area(n, sides):
    p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
    
    return p_area


print("The area of the polygon is: ",area(n_sides, s_length))
