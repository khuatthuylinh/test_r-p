try:
    s = input("Nhập vào một chuỗi: ")

    if s == "":
        raise ValueError("Chuỗi không được để trống!")
    else:
        do_dai_chuoi=len(s)
        print(f"Độ dài của chuỗi là: {do_dai_chuoi}")

except:
    print("Không hợp lệ")