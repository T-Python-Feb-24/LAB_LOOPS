## 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205

## 2) Using a while loop and input , do the following :
'''
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.

'''
for num in range(45, 211):
    if num == 100:
        continue
    print(num)
    if num == 205:
        break
while True:
        answer = input("What is the product of 7 * 24? ")
        if answer == "168":
             
            print("You answered this question correctly.")
            
            break

        else:
             
             print("Your answer is wrong. Try again...")