number:int = int(input("Enter positive integer number: "))
numbers:int = range(0,number+1)
sum = 0
for num in numbers:
    if num % 2 == 0:
        print(num)
        sum += num
print("the sum of the even numbers in your range is: ", sum)