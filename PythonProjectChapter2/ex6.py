num = int(input("Nhập vào 1 số nguyên dương: "))
if num <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
else:
    count = 0
    temp = num
    while temp > 0:
        temp //= 10
        count += 1
    print(f"Số {num} có {count} chữ số.")
