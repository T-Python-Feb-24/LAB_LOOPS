loop = range(45, 210)


for number in loop:
    if number == 100:
        continue
    print(number)
    if number == 250:
        break
print(number)

question = "What is the product of 7 * 24?"
while int(input(question)) != 168:
    print("Answer is wrong, try again")
else:
    print("You answered this question correctly")