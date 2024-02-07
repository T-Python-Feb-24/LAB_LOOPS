# 1) Using range(),  make a range from 45 to 210, using a for loop iterate over the sequence and print the elements. Skip the number 100 and break the loop at 205
numbers = range(45, 210)

for number in numbers:
    if number == 100:
        continue
    if number == 205:
        break
    print(number)
else:
    print("executed when the loop finishes correctly")

    # 2) Using a while loop and input , do the following :
    '''
- Ask the the user : "what is the product of 7 * 24 ?"
- check if the answer is right then exit the loop and print "You answered this Question correctly"
- if the answer is wrong, then print "Your Answer is wrong try again.." and show the user the question again.
'''
Question = " what is the product of 7 * 24? "

while input((Question)) != "168":
     print("Your Answer is wrong try again..")
else:
     print("You answered this Question correctly")
    