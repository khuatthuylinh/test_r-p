def de_quy(n):
    if n==1:
        return 1
    else:
        return n+de_quy(n-1)
n=int(input("Nhập số nguyên n: "))
print(de_quy(n))