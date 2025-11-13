import math
try:
    a=int(input("Nhập vào 1 số nguyên: "))
    if a<0:
        print("Không thể tính giai thừa của số âm")
    else:
        giai_thua=math.factorial(a)
        print(f"Giai thừa của {a} là: {giai_thua}")
except:
    print("Số không hợp lệ.")