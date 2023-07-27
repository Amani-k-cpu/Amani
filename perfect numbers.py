n = int(input("enter the number: "))

i = 0
for x in range (1, n):
    if n %  x == 0:
       i += x
if n == i:
    print("perfect number")
else:
    print("not perfect number")