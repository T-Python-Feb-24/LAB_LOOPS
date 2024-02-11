for number in range(45, 210):
        print(number)
        if number == 100:
            continue
        elif number == 205:
             break
        print(number)
        Question=int(input("what is the product og 7*24?"))
        while Question !="168":
            print("You answered this Question wrong, thr correct answer is 168")
        else:
            print("You answered this Question correctly")