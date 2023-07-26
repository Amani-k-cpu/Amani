n = 0
w = 5
b = 5
width = 100

width = width - b

while width > 0:
    width = width-w-b
    n=n+1
    if width < 0:
        break
width = width+w+b
print("the gap =",width/2)
print("number of tails", n*2-1)
