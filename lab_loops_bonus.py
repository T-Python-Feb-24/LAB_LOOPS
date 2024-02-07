# Bonus: Sum of even numbers

positive_int:str = int(input("Enter a positive integer: "))

sum_of_even_number = 0
for number in range(1, positive_int+ 1):
    if number % 2 == 0:
        sum_of_even_number += number
else:
    print(f"The sum of even numbers between 1 to {positive_int} is {sum_of_even_number} ")

