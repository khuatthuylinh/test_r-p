try:
    print('Please enter 2 số để chia.')
    dividend = int(input("Nhập vào số bị chia: "))
    divisor = int(input("Nhập vào số chia: "))
    print(dividend, '/', divisor, '=', dividend / divisor)
except:
    print('Big problem')