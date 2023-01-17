n = int(input("Digite o n valor de fibonacci: "))

def Fibonacci (n):
    if n <= 1:
        return n
    
    return Fibonacci(n-2) + Fibonacci (n-1)

for i in range (1,n+1):
    print(i,Fibonacci(i),end=" ",sep="-")