def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Nhập vào 1 số : "))
result=factorial(n)
print(f"Giai thừa của {n} là: {result}")
