
def  somme(x,y):
    z = x +y
    print(z)

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()