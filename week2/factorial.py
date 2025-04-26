def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

try:
    num = abs(int(float(input('input the start number: '))))
    print(factorial(num))
except:
    print('please iniput a valid number: ')
