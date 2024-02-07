# Write a Python program that prompts the user for a positive integer `n`, and then calculates the sum of all even numbers between 1 and `n`, inclusive.
# Your program should use a loop (either a `for` loop or a `while` loop) to iterate over the numbers between 1 and `n`, and only add the even numbers to the sum.

rangeNumber =int(input("Enter a positive integer"))
sum = 0
for number in range(1,(rangeNumber +1)):
    if number % 2 == 0 :
        sum += number
        
print(f"The sum of even numbers between 1 and {rangeNumber} is {sum}.")