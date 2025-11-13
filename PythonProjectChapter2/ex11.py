n=int(input("Nhập vào 1 số nguyên dương: "))
if n<=1:
    print(f"{n} không là số nguyên tố.")
else:
    nguyen_to=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            nguyen_to=False
            break
    if nguyen_to is False:
        print(f"{n} không là số nguyên tố.")
    else:
        print(f"{n} là số nguyên tố.")
