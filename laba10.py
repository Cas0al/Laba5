def func(n):
    while n>0:
        if n//64>0:
            print(f"64 - {n//64}")
        n%=64
        if n//32>0:
            print(f"32 - {n//32}")
        n%=32
        if n//16>0:
            print(f"16 - {n//16}")
        n%=16
        if n//8>0:
            print(f"8 - {n//8}")
        n%=8
        if n//4>0:
            print(f"4 - {n//4}")
        n%=4
        if n//2>0:
            print(f"2 - {n//2}")
        n%=2
        if n>0:
            print(f"1 - {n}")
        break
n=int(input())
func(n)
