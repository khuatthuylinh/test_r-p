chuoi=input("Nhập vào 1 chuỗi: ")
ky_tu=input("Nhập vào ký tự cần đếm: ")
dem =0
for a in chuoi:
    if a==ky_tu:
        dem +=1
print(f"Ký tự '{ky_tu}' xuất hiện {dem} lần.")