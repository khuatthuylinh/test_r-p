def greet(name= "Student" ):
    print("Hello " + name+"!")
ten=input("Nhập vào tên của bạn: ")

if ten=="":
        greet()
else:
        greet(ten)
