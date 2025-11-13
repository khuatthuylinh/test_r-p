n=int(input("Nhập vào 1 số nguyên dương n: "))
if n<0:
    print("Không có giai thừa")
elif n==0 or n==1:
    print(f"{n}!=1")
else:
    factorial=1
    for i in range(2,n+1):
        factorial*=i
    print(f"{n}!={factorial}")