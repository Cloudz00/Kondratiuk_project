"""def is_year_leap(year):
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return True
    else: return False

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result != test_results[i]: print("Failed")
    else: print("OK")"""

"""def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

def days_in_month(year, month):
    x = [4, 6, 9, 11]
    if month != 2:
        if month in x: days = 30
        else: days = 31
    else:
        if is_year_leap(year): days = 29
        else: days = 28
    return days

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")"""

"""def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

def days_in_month(year, month):
    x = [4, 6, 9, 11]
    if month != 2:
        if month in x: days = 30
        else: days = 31
    else:
        if is_year_leap(year): days = 29
        else: days = 28
    return days
def day_of_year(year, month, day):
    sum=day
    for i in range(1,month):
        sum+=days_in_month(year, i)
        print (sum)
    return sum

print(day_of_year(400, 12, 31))"""

"""def is_prime(num):
    if num != 0 and num != 1 and num != 2 and num != 3 and num != 5:
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            return False
        else:
            return True
    else:
        return True

for i in range(1, 20):
    if is_prime(i + 1): print(i + 1, end=" ")"""

"""def liters_100km_to_miles_gallon(liters):
    gallon=liters/3.785411784
    miles=0.62137*100
    return miles/gallon

def miles_gallon_to_liters_100km(gallon):
    liters = 3.785411784/gallon
    km = 0.62137*100
    return liters*km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))"""

def is_a_triangle(a, b, c):
    #Сума будь-яких двох сторін має бути більшою за третю
    if (a + b > c) and (b + c > a) and (a + c > b): return True
    else: return False

def is_a_right_triangle(a, b, c):
    if is_a_triangle(a, b, c):
        #Визначення гіпотенузи (найбільше число)
        sides = [a, b, c]
        sides.sort()
        a, b, c = sides

        #Теорема Піфагора
        if a**2 + b**2 == c**2:
            return True
        else:
            return False
    else:
        return False