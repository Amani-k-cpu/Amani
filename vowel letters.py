counter = 0
s = input("enter a text: ")
s = s.lower()
print(s)
for i in s:
    if(i in "eaiuo"):
        counter +=1
print(counter)


