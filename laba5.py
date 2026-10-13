import random
def func(a,b):
    a=random.randint(a,b)
    print(a)
    n=int(input())
    while not(a<=n<=b):
        if n>b:
            print("Too much")
        elif n<a:
            print("Too low")
        n=int(input())
    print("Hell yeah")
a=int(input())
b=int(input())
func(a,b)
