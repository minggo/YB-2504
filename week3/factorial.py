# def factorial(num):
#     if num == 0:
#         return 1
#     return num * factorial(num - 1)

# try:
#     num = abs(int(float(input('input the start number: '))))
#     print(factorial(num))
# except:
#     print('please iniput a valid number: ')


class Factorial:
    def __init__(self, num):
        self.num = num

    def isPrime(self):
        if (self.num <= 0):
            return False
        elif (self.num == 2):
            return True
        else:
            for i in range(2, self.num -1):
                if (self.num / i == 0):
                    return True
            return False


    def doRun(self, num):
        if (num < 0):
            print("it is an invalid number")
        else:
            if (num == 0):
                return 1
            else:
                return num * self.doRun(num - 1)
            
    def run(self):
        return self.doRun(self.num)   

num = int(float(input('input a number ')))
fac = Factorial(num)
# result = fac.run()
# print(f'the result is {result}')
if (fac.isPrime()):
    print('it is a prime')
else:
    print('it is not a prime')
                
