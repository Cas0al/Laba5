def func(a,b):
    print("Введите число")
    n=int(input())
    while not(a<=n<=b):
        print("Введите число")
        n=int(input())
    print("Число корректное")
a=int(input())
b=int(input())
func(a,b)
