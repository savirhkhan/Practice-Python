# fibonacci sequence generator

num = int(input("How many fibonacci Number , you would like to generate: "))
def fib_generator():
    fib1, fib2 = 0,1
    for i in range (num):
        print(fib2)
        fib1,fib2 = fib2, fib1+fib2

fib_generator()
