import random

x = 1
y = 0

while x == 1:
    q1 = random.randint(1,20)
    q2 = random.randint(1,20)
    print (q1, " +" , q2 ," =?")

    userInput = input( "the answer is:")
    
    if not (userInput == "done"):

       if userInput == str(q1 + q2):
         print("correct")
       else:
         print("wrong")
    else:
      break
        
        


