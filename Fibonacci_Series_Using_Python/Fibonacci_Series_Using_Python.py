def fib(num):
    a = 0
    b = 1

    if num <= 0:
        print("The entered value should be greater than zero")
    else:
        print(a)
        print(b)

        for i in range(2, num): # or we can use range(3, num + 1) 
            c = a + b
            a = b
            b = c
            print(c)
    return

number = int(input("Enter the nth number of the Fibonacci Series to find: "))
fib(number)