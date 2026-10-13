def func(a,b):
    print("Enter new number in range from a to b")
    n=int(input())
    while not(a<=n<=b):
        print("Enter new number in range from a to b")
        n=int(input())
    print("Well, yes, you're right")
a=int(input())
b=int(input())
func(a,b)
