Numbers= range(45 , 211)

for num1 in Numbers:
    if num1 ==100:
        continue
    elif num1 ==206:
        break
    print(num1)

   
        

Question :str = "what is the product of 7 * 24 ?"
Ttails : int = 5

while input (Question) != "168":
    Ttails -= 1
    print(f"Your answer is wrong , try again {Question} \n , you have {Ttails} tries")
    if Ttails == 0:
     print("You don't have any more tries :( )")
     break
    
else:
    print("Yay ,you answered this Question correctly :) ")
