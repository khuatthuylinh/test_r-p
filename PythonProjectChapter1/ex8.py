def is_even(n):
    return n%2==0
n=int(input("Nhập vào 1 số n: "))
if is_even(n):
    print(n, "là số chẵn ")
else:
    print(n, "là số lẻ")

