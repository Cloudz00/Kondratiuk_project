"""print("Programming"+3*"*"+"Essential"+3*"*"+"in"+3*"."+"Python")

print(4*" "+"*")
print(3*" "+"*"+" "+"*")
print(2*" "+"*"+3*" "+"*")
print(" "+"*"+5*" "+"*")
print(3*"*"+3*" "+3*"*")
print((2*" "+"*"+3*" "+"*\n")*2, end="")
print(2*" "+5*"*")

print("I'm student")

print("\"I'm\"\n"+2*"\""+"learning"+"\""*2+"\n"+3*"\""+"Python"+3*"\"")

print(500**8)

print(777**16)

print(3**3**4) """
#Об'єкт рандомайзера
import math
import random

#Змінні, що рахують скільки раз випаде значення х
a1=0; a2=0; a3=0; a4=0; a5=0

#Значення з таблиці
x1=0.11
x2=round(0.25+x1, 2)
x3=round(0.26+x2, 2)
x4=round(0.3+x3, 2)
x5=round(0.08+x4, 2)

#Створюємо випадкове число та округлюємо, і додаємо лічильник
for i in range(100000):
    number=random.random()
    number=round(number,2)
    if(number==x1): a1+=1
    elif(number==x2): a2+=1
    elif (number==x3): a3+=1
    elif (number==x4): a4+=1
    elif (number==x5): a5+=1
print("a1:",a1,", a2:",a2,", a3:",a3,", a4=:",a4,", a5=",a5)

lambda_val = 1
result = []

for i in range(10):
    y = random.random()
    xx = (-1 * (math.log(1 - y))) / lambda_val
    result.append(xx)

for el in result:
    print(el)

sum_val = 0
x_sum = []
for el in result:
    sum_val += el
    x_sum.append(sum_val)

a = 0
for el in x_sum:
    a += 1
    print(f'x{a}: {el}')