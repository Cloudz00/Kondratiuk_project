import math
mu=0
sigma=1
x=1
f=(math.exp((-1*(x-mu)**2)/2*sigma**2))/(sigma*math.sqrt(2*math.pi))
print(f)

john=3
mary=5
adam=6
print(str(john)+","+str(mary)+","+str(adam))
totalApple=john+mary+adam
print(totalApple)
print("Загальна кі-сть яблук: "+str(totalApple))

kilometers = 12.25
miles = 7.38
miles_from_kilometers = kilometers/1.61
kilometers_from_miles = miles*1.61
print(miles, "miles is", round(kilometers_from_miles, 2), "kilometers")
print(kilometers, "kilometers is", round(miles_from_kilometers, 2), "miles")

#x = input("Уведіть х - ")
x = float(x)
y=3*x**3-2*x**2+3*x-1
print("y =", y)

#this program computes the number of seconds in a given number of hours
hours = 2
seconds = 3600 #seconds in 1 hour
print("Hours: ", hours)
print("Seconds in Hours: ", hours * seconds) # printing seconds in a given hours

"""x=float(input("введіть х - "))
y=float(input("введіть y - "))
addition=x+y; print(addition)
subtraction=x-y; print(subtraction)
multiplication=x*y; print(multiplication)
division=x/y; print(division)"""

""" = float(input("введіть х - "))
y=1/(x+(1/(x+(1/(x+(1/(x+(1/x))))))))
print("y- ",y)"""

"""hours=int(input("Введіть початок події. Години - "))
for i in range(1,100):
    if hours < 0 or hours > 24: hours=int(input("Неможливий час, спробуйте ще раз. Години - "))
    else:
        break
minutes=int(input("хвилини - "))
for i in range(1,100):
    if minutes < 0 or minutes>59: minutes=int(input("Неможливий час, спробуйте ще раз. Хвилини - "))
    else:
        break
end_hours=hours
end_minutes=minutes
time=int(input("Введіть скільки хвилин буде тривати подія - "))
for i in range(1,100):
    if time < 0: time=int(input("Неможливий час, спробуйте ще раз. Хвилини - "))
    else:
        break

if time+minutes >= 60:
    hours_in_time = time // 60
    end_hours=hours+hours_in_time
    for i in range(1,100):
        if end_hours>=24: end_hours-=24
        else:
            break
    minutes_in_time = time % 60
    end_minutes = minutes + minutes_in_time
else:end_minutes=end_minutes+time
if end_minutes >= 60:
    end_hours += 1
    end_minutes -= 60

if end_hours >= 24:
    end_hours -= 24
print("Подія кінчиться о ", str(end_hours)+":"+str(end_minutes))