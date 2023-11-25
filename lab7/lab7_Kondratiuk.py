"""import random
generator= [random.randint(1, 100) for _ in range(20)]
print(generator)
n=int(input("Введіть число n - "))
result=()
for element in generator:
    if element<n:
        result+=(element,)
print(result)"""

"""w1=input("Перше слово - ")
w2=input("Друге - ")
w3=input("Третє - ")
line=(w1,w2,w3)
result=", ".join(line)
print(result)"""

"""library = {
    'Пригоди Героїв': {'Автор': 'Іван Письменник', 'Рік видання': 2015, 'Кількість сторінок': 240},
    'Таємниці Літа': {'Автор': 'Марія Романова', 'Рік видання': 2019, 'Кількість сторінок': 320},
    'Подорож до Зірок': {'Автор': 'Олександр Астроном', 'Рік видання': 2022, 'Кількість сторінок': 400},
    'Легенди Відьмака': {'Автор': 'Юрій Фентезіст', 'Рік видання': 2017, 'Кількість сторінок': 280},
    'Історії Загадок': {'Автор': 'Наталія Детективова', 'Рік видання': 2020, 'Кількість сторінок': 200},
}

search = input("Введіть назву книги: ")
if search in library:
    book_info = library[search]
    print(f"Інформація про книгу '{search}':")
    print(f"Автор: {book_info['Автор']}")
    print(f"Рік видання: {book_info['Рік видання']}")
    print(f"Кількість сторінок: {book_info['Кількість сторінок']}")
else:
    print(f"Книга з назвою '{search}' не знайдена в бібліотеці.")"""

"""students = {
    'Іванов': ('Іван', 'Іванович', 'Група A'),
    'Петров': ('Петро', 'Петрович', 'Група B'),
    'Сидоров': ('Сидір', 'Сидорович', 'Група C'),
}
search = input("Введіть прізвище студента: ")
if search in students:
    student_info = students[search]
    print(f"Інформація про студента '{search}':")
    print(f"Ім'я: {student_info[0]}")
    print(f"По батькові: {student_info[1]}")
    print(f"Група: {student_info[2]}")
else:
    print(f"Студента з прізвищем '{search}' не знайдено в списку.")"""


phones = {
    'Іванов': ['123-45-67', '987-65-43', '111-11-11'],
    'Петров': ['111-22-33', '222-33-44', '333-44-55'],
    'Сидоров': ['555-44-33', '999-88-77', '777-66-55'],
}
def add_number(contact, new_number):
    if contact in phones:
        phones[contact].append(new_number)
        print(f"Новий номер {new_number} додано для контакту {contact}.")
    else:
        print(f"Контакт {contact} не знайдено в телефонній книзі.")

add_number('Іванов', '444-55-66')
for contact, numbers in phones.items():
    print(f"Номери телефонів для {contact}: {', '.join(numbers)}")