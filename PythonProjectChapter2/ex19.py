n=int(input("Nhập vào 1 số nguyên dương: "))
so_lon_nhat=0
for digit in n:
    if int(digit)>so_lon_nhat:
        so_lon_nhat=int(digit)
print(f"Chữ số lớn nhất trong {n} là: {so_lon_nhat}")