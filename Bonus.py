'''
Sum of Even Numbers
Write a Python program that prompts the user for a positive integer n, 
and then calculates the sum of all even numbers between 1 and n, inclusive.

Your program should use a loop (either a for loop or a while loop) to iterate over the numbers between 1 and n, and only add the even numbers to the sum.
------------------------------
For example:

Enter a positive integer: 10
The sum of even numbers between 1 and 10 is 30.
------------------------------
In this example, the even numbers between 1 and 10 are 2, 4, 6, 8, and 10, and their sum is 30.
'''

number = int(input("Enter a positive interger: "))
count = 1
sum = 0

while count <= number:
    if count % 2 == 0:
        #print(count)
        sum = sum + count
    count += 1
print(f"The sum of even numbers between 1 and {number} is {sum}.")