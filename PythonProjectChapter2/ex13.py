n=int(input("Nhập vào 1 số nguyên: "))
tong =0
for digit in str(n):
    tong += int(digit)
print("Tổng các chữ số là:", tong)
