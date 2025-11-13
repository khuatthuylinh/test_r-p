import math
try:
    a=float(input("Nhập vào 1 số: "))
    if a<0:
        print("Không thể tính căn bậc 2 của số âm")
    else:
        can_bac_hai=math.sqrt(a)
        print("Căn bậc hai của",a,"là: ",can_bac_hai)
except:
    print("Số không hợp lệ")