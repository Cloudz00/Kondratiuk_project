"""n=int(input("n= "))
print(n>=100)"""

"""x=int(input("x= "))
y=int(input("y= "))
top=x
if x<y:top=y
print(top)"""

"""str=input("Спробуйте написати Spathiphyllum - ")
if str=="Spathiphyllum": print("Yes - Spathiphyllum is the best plant ever!")
elif str=="spathiphyllum": print("No, I want a big Spathiphyllum!")
else: print("Spathiphyllum! Not",str)"""

"""income=float(input("Введіть дохід- "))
tax=0
if income<85528 and income!=85528: tax=income*0.18-556.2
else:tax=14839.2+0.32*(income-85528)
if tax<=0:tax=0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")"""

"""year=int(input("Enter year - "))
str1="Leap year"
str2="Common Year"
gr_cal="Not within the Gregorian calendar period."
if year<=1582: print(gr_cal)
elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(str1)
else:
    print(str2)"""


"""counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)"""


"""import random
secret_number = random.randint(1, 15)
print(
"""
#+================================+
#| Welcome to my game, muggle!    |
#| Enter an integer number        |
#| and guess what number I've     |
#| picked for you.                |
#| So, what is the secret number? |
#+================================+
""")
print(secret_number)#для перевірки коду
guess=int(input(""))
while guess!=secret_number:
    print ("Невірно, ха-ха! Ви застрягли у моїй петлі!")
    guess=int(input(""))
print("Молодець, магле! Тепер ти вільний")"""

"""import time
for i in range (1,6):
    print(i, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")"""

"""flag=True
while flag:
    output = input("Введіть слово: ")
    if output=="chupacabra":
        print("You've successfully left the loop.")
        break"""

"""user_word=input("Введіть слово для пожирання голосоних ")
user_word = user_word.upper()
result=""
for letter in user_word:
    if letter == "A": continue
    elif letter == "O": continue
    elif letter == "I": continue
    elif letter == "E": continue
    elif letter == "U": continue
    else:
        result=letter
        print(result)"""

"""user_word=input("Введіть слово для пожирання голосоних ")
user_word = user_word.upper()
word_without_vowels=""
for letter in user_word:
    if letter == "A" or letter == "O" or letter == "I" or letter == "E" or letter == "U": continue
    else: word_without_vowels+=letter
print(word_without_vowels)"""

"""blocks=int(input("введіть кількість блоків для піраміди- "))
height = 0
blocks_need = 1
while blocks >= blocks_need:
    height += 1
    blocks -= blocks_need
    blocks_need+= 1
print("Висота: ",height)"""


count=0
c0=int(input("число>0 & !=0: "))
while(c0!=1):
    if((c0%2)==0): c0/=2; print (c0); count+=1
    else: c0=c0*3+1; print (c0);  count+=1
print("steps: ",count)