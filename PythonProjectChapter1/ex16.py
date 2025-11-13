try:
    a=int(input("Nhập số nguyên thứ nhất: "))
    b=int(input("Nhập số nguyên thứ hai: "))
    ket_qua=a/b
    print("Kết quả của phép chia:", ket_qua)
except ZeroDivisionError:
    print("Không thể chia cho 0")
except:
    print("Số không hợp lệ")
