a=int(input("Nhập số nguyên dương thứ nhất: "))
b=int(input("Nhập số nguyên dương thứ 2: "))
ucln =1
for i in range (1, min(a,b)+1):
    if a%i==0 and b%i==0:
        ucln=i
print(f"UCLN của {a} và {b} là: {ucln}")
