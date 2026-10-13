def func(z):
    s=0
    for i in range(z-1):
        s+=int(input())
    print(int((1+z)*z/2-s))
z=int(input())
func(z)
