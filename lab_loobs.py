#make a range from 45 to 210
numbers = range(45, 210)
#using a for loop iterate over the sequence and print the elements
for number in numbers:
    #Skip the number 100 and break the loop at 205
    if number == 100:
        continue
    elif number == 205:
        break
    print(number)


# Ask the user: "what is the product of 7 * 24 ?"
user_answer = int(input('What is the product of 7 * 24? '))

# Check if the answer is correct, then exit the loop
while user_answer != 168:
    # If the answer is wrong, print "Your Answer is wrong try again.." and ask the user again.
    print('Your Answer is wrong. Try again...')
    user_answer = int(input('What is the product of 7 * 24? '))
else:
    # If the answer is right, print "You answered this Question correctly."
    print('You answered this question correctly.')


