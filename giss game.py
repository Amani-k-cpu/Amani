import random

num = 1

r = random.randint(1,10)
while num == 1:
    userInput = int(input("the answer is:"))
 
    if userInput == (r):
         print("correct")
    elif userInput < (r):
         print("go lower")
    else:
         print("go upper")


    break
   

       
    
    
    