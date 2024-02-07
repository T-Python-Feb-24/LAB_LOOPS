# 1. Using range()
for number in range(45, 210):
    if number == 100:
        continue
    if number == 205:
        break
    print(number)

# 2. Using a while loop

user_result = "What is the product of 24 * 7 ?"
production_result = 24 * 7

while int(input(user_result)) != production_result:
    print("Your Answer is wrong try again..")
else:
    print("You answered this Question correctly")
    
