def func(n):
    k=0
    mn=10**10
    for i in range(n):
        t=int(input())
        if t==mn:
            mn=t
            k+=1
        if t<mn:
            mn=t
            k=1
    print(k)            
n=int(input())
func(n)
