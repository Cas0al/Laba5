def func(a,b):
    while a!=b:
        if a>b:a-=b
        else:b-=a
    print(a)
a=int(input())
b=int(input())
func(a,b)
