n = int(input("Enter a positive integer: "))
sum_of_evens = 0
for num in range(1, n +1):
    if num % 2 == 0:
        sum_of_evens += num
    
print("The sum of even numbers between 1 and", n, "is", sum_of_evens)
