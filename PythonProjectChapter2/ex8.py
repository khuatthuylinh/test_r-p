n=int(input("Nhập vào 1 số từ 1 đến 9: "))
if n<1 or n>9:
    print("Số không hợp lệ")
else:
    print(f"Bảng cửu chương của {n} là:")
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
