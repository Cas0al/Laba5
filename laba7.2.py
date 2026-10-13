def func(a,b):
    if a==b:
        print(a)
    elif a>b:func(a-b,b)
    else:func(a,b-a)
a=int(input())
b=int(input())
func(a,b)
