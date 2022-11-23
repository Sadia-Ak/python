# Author:  Sadia Akther
# Email:  sakther1@student.gsu.edu
# Section: DSCI-006
# purpose: to determines if it Prime for tthe lab and extra assignment 1 and to find the fibonacci numbers foe assignment 2. 
# Pre-conditions: to provide the given integer.
# Post-conditiions: the outcome/result the of the input. 

import random  

#Lab 
def prime(num):
    n =[]
    for i in num:
        num1=0
        for t in range(2,i//2+1):
            if i%t==0:
                num1=1 
                break
        if num1==0:
            n.append(i)
    return n

n = int(input("How many numbers are needed to write to the file: "))
random.seed(1)

f = open("test.txt",'w')
for i in range(n):
    k = random.randint(1,100) 
    f.write(str(k)+" ")
f.close() 

f = open("test.txt",'r')
data=f.read()
num=list(map(int,data.split()))

primes = prime(num)

print('\n\n')
for i in range(n):
    print(num[i],end=' ')
print('\n\n*****************************\n')
for i in range(len(primes)):
    print(primes[i],end=' ')
print('\n')
print(len(primes),'prime numbers found in this file')
print('===========\n')

prime(num)


#Extra Assignment 1
def prime(num):
    n =[]
    for i in num:
        num1=0
        for t in range(2,i//2+1):
            if i%t==0:
                num1=1 
                break
        if num1==0:
            n.append(i)
    return n
def sumofd(data):
    r = [-1]
    for i in data: 
        k = list(map(int,str(i)))
        r.append(sum(k))
    return data[r.index(max(r))]

n = int(input("How many numbers are needed to write to the file: "))
random.seed(2)

f = open("test.txt",'w')
for i in range(n):
    k = random.randint(1,100) 
    f.write(str(k)+" ")
f.close() 

f = open("test.txt",'r')
data=f.read()
num=list(map(int,data.split()))
 
primes = prime(num)

print('\n\n')
for i in range(n):
    print(num[i],end=' ')
print('\n\n*****************************\n')
for i in range(len(primes)):
    print(primes[i],end=' ')
print('\n')
print(len(primes),'prime numbers found in this file')
print('\n\n******************************\n')
print(len(data),'has a maximum sum of digits = ',len(num))
print('===========\n')


#Extra Assignment 2

def fibonacci(n):
    n = int(input('How many Fibonacci numbers would you like to get:'))
    print('\n\n---------------\n')
    print('\n #Fibonacci')
    print('\n\n---------------\n')
    f = open("fibonacci.txt", "w")
    a = 0
    b = 1
    if n == 1:

        print("0", b)
        f.write("0 " + str(b) + "\n")
    else:
        print("0", b)
        f.write("0 " + str(b) + "\n")
        for _ in range(1, n):
            c = a + b
            print(_, c)
            f.write(str(_) + " " + str(c) + "\n")
            a = b
            b = c
    f.close()


fibonacci(n)