for i in range(45, 210):
    match i:
        case 100:
            continue
        case 205:
            break
        case _:
            print(i)
question = 0
answer = 7*24
while question != answer:
    question = int(input("What is the product of 7 * 24?\n"))
    if question == answer:
        print("You answered this Question correctly")
        break
    else:
        print("Your Answer is wrong try again..")
