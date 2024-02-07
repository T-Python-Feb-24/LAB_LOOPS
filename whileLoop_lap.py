ans = (" What is the product of 7 * 24 ? ")
tries = 3

while input(ans)  != "168":
    tries -= 1
    print(f"Your answer is wrong. Try again. {tries} remaining tries.")
    if tries == 0:
        print("You Lost ")
        break
    
else:
    print("You answered this Question correctly")