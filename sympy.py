import sympy
def isprime(n):
    if (n<2):
        return False
    for i in range(2,n // 2+1):
        if (n%i==0):
         return False
    return True

#def main():
number= int(input('Please provide an integer:'))
if isprime (number):
    print('The integer',number, 'is  prime')
#else:
  #  print('The integer',number, 'is not prime')

'''
numbers = int(input('Please provide an integer:'))
if isPrime(number):
    print('The integer',numbers, 'is not prime')
else:
    print('The integer',numbers, 'is not prime')

Number= int(input('Please provide an integer:'))
if isPrime(Number):
    print('The integer',Number, 'is Negtive')
else:
    print('The integer',Number, 'is not Negtive')

'''