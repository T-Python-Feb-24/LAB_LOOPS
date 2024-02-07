num= int(input("Enter a positive integer: "))
sum=0
for n in range(1,num+1):
    if n%2 ==0:
     sum+=n
else:
    print(f"The sum of even numbers between 1 and,{num} is ,{sum}")
   