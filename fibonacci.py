n = int(input("Digite o n valor de fibonacci: "))

def Fibonacci (n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    return Fibonacci(n-2) + Fibonacci (n-1)

print(Fibonacci(n))
