import random
def func(a,b):
    a=random.randint(a,b)
    print(a)
    n=int(input())
    while not(a<=n<=b):
        if n>b:
            print("Перелёт")
        elif n<a:
            print("Недолёт")
        n=int(input())
    print("Число угадано")
a=int(input())
b=int(input())
func(a,b)
