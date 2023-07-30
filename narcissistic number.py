n = str(input(""))
x = len(n)

answer = 0
for i in n:
    
    answer+=int(i)**x
    
if answer==int(n):
    print('Yes')
else:
    print('No')