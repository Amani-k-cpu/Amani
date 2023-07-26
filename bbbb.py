hour1= int(input("hour1: "))
min1= int(input("min1: "))
hour2= int(input("hour2: "))
min2= int(input("min2: "))

if (hour1<hour2):
    print("hour1 come first")
elif (hour1 == hour2):
    if min1<=min2:
        print("hour1 come first")
    else:
        print("hour2 come first")
        
else:
    print("hour2 come first")


