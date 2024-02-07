# Sum of Even Numbers

# # Write a Python program that prompts the user for 
# a positive integer `n`, and then calculates the sum of all even numbers
# between 1 and `n`, inclusive.

even_num = int (input ("Enter a positive integer: "))
total = range(1,even_num+1)
for i in total:
    if (even_num %2 == 0) : 
        print(f"The sum of even numbers between 1 and {even_num} is {total}.")
    