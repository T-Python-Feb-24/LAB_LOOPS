n= int(input("Enter positive numper:"))
sum_evens =0
for num in range(1,n+1):
     if num %2 == 0:
         sum_evens += num
         print("The sum of even number between 1 an","is:", sum_evens)