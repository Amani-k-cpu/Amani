import math

print("square(1) circle(2) rectangle(3) cylender(4) trangle(5)")



def s_area(s_length):
    s_area = s_length **2
    return s_area


def c_area(c_half):
    c_area = (math.pi *((c_half)**2))
    return c_area


def r_area(r_length, r_weight):
    r_area = (r_length * r_weight)
    return r_area


def cy_area(cy_half, cy_hight):
    cy_area = (2*math.pi*cy_half*(cy_half+cy_hight))
    return cy_area


def t_area(t_hight, t_length):
    t_area =(t_hight *t_length)/2
    return t_area


x = 1

while x == 1:
    answer = input("choose number or quit: ")
    if not (answer == "quit"):
       answer = int(answer)
       if answer == 1:
          s_length = int(input("enter s_length: "))
          print("the area of square: ",s_area(s_length))
       elif answer == 2:
         c_half = int(input("enter c_half: "))
         print("the area of circle: ", c_area(c_half))
       elif answer == 3:
         r_length = int(input("enter r_length: "))
         r_weight = int(input("enter r_weight"))
         print("the area of rectangle: ",r_area(r_length, r_weight))
       elif answer == 4:
         cy_half = int(input("enter cy_half: "))
         cy_hight = int(input("enter cy_hight"))
         print("the area of cylender: ",cy_area(cy_half, cy_hight))
       else:
         t_hight = int(input("enter t_hight"))
         t_length = int(input("enter t_length: "))
         print("the area of traingle: ",t_area(t_hight, t_length))
    else:
        break
        print("-------")


        
        
    

