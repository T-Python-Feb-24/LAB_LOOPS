nnum = int(input(" Please Enter a positive integer:"))
sum1 = 0

for number in range(1, nnum+1):
    if number % 2 == 0:
        sum1 = sum1 + number

print(f"you enter the number {nnum}")

print(f"The sum of even numbers from 1 to {nnum} = {sum1}")