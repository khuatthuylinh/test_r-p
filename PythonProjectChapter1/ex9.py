a=float(input("Nhập vào số thứ nhất: "))
b=float(input("Nhập vào số thứ 2: "))
c=float(input("Nhập vào số thứ 3: "))

if a>=b and a>=c:
    so_lon_nhat=a
elif b>=a and b>=c:
    so_lon_nhat=b
else:
    so_lon_nhat=c

print("Số lớn nhất là: ", so_lon_nhat)