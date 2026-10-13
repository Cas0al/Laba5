def y(x,eps):
    y=1
    while True:
        if abs(y-0.5*(y+x/y))<eps:
            return 0.5*(y+x/y)
        y=0.5*(y+x/y)

x=int(input())
eps=float(input())
print(y(x,eps))
