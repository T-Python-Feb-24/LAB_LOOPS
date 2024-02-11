number= int(input('Enter a number: '))
sum_even = 0
x = 0
while x <= number:
    if x % 2 == 0:
        print(x)
        sum+=x
    x+=1
print(f"Sum of all the even numbers is {sum_even}")