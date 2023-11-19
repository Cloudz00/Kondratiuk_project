"""line=[1,2,3,4,5]
print(line)
change_num=int(input("Введіть число яке ви хочете вставити- "))
change_place=int(input("на яке місце по порядку- "))
line[change_place-1]=change_num
print(line)
del line[4]
print(line)
print (len(line))"""

"""n = int(input("Введіть кількість елементів у списку: "))
my_list = []

for i in range(n):
    element = int(input(f"Введіть елемент {i + 1}: "))
    my_list.append(element)

    n = len(my_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
print(my_list)"""

"""n = int(input("Введіть кількість елементів у списку: "))
list = []

for i in range(n):
    element = int(input(f"Введіть елемент {i + 1}: "))
    list.append(element)

changed_list = []
for element in list:
    if element not in changed_list:
        changed_list.append(element)
print(changed_list)"""

"""desk = [['_']*8 for _ in range(8)]
desk[0][0]="♟"
desk[7][0]="♟"
desk[0][7]="♟"
desk[7][7]="♟"
for row in desk:
    print(row)"""

list1=["A", "B", "C"]
list2=list1[:]
list3=list2[:]
del list1[0]
del list2[0]
print(list3)