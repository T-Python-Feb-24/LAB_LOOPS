while True:

    n = input("Enter a positive integer or 'end' to exit ->")
    if n == "end":
        print("exiting...")
        break

    n = int(n)

    sum = 0
    num = 1

    if n < 0:
        print("This is not an even number")

    while num <= n:
        if num % 2 == 0:
            sum += num
        num += 1
    print(f"The sum of even numbers between 1 and{n} is {sum}")
    print("-"*50)