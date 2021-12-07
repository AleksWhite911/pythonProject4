"""
Task 1
Даны 2 переменных, в которых хранятся строки произвольной длины: phrase_1 и phrase_2.
Напишите код, который проверяет какая из этих строк длиннее.

Примеры работы программы:

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики’
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
Результат:
Фраза 1 длиннее фразы 2

"""
string_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
string_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

if len(string_1) > len(string_2):
    print('Фраза 1 длиннее фразы 2')
elif len(string_2) > len(string_1):
    print('Фраза 2 длиннее фразы 1')
else:
    print('Фразы равной длины')

"""
Task 2
Дана переменная, в которой хранится четырехзначное число (год). 
Необходимо написать программу, которая выведет, является ли данный год високосным или обычным.

"""

year = 2020

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Год является високосным")
else:
    print("Обычный год")


"""
Task 3
Необходимо написать программу,
 которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака.
"""

day = int(input('Введите день: '))
month = int(input('Введите месяц: '))

if (day >= 21 and day <= 31 and month == 3) or ( month == 4 and day >= 1 and day <= 19):
   print("Знак зодиака:Овен")

elif (day >= 20 and day <= 30 and month == 4) or ( month == 5 and day >= 1 and day <= 20):
   print("Знак зодиака:Телец")

elif (day >= 21 and day <= 31 and month == 5) or ( month == 6 and day >= 1 and day <= 21):
   print("Знак зодиака:Близнецы")

elif (day >= 22 and day <= 30 and month == 6) or ( month == 7 and day >= 1 and day <= 22):
   print("Знак зодиака:Рак")

elif (day >= 23 and day <= 31 and month == 7) or ( month == 8 and day >= 1 and day <= 22):
   print("Знак зодиака:Лев")

elif (day >= 23 and day <= 31 and month == 8) or ( month == 9 and day >= 1 and day <= 22):
   print("Знак зодиака:Дева")

elif (day >= 23 and day <= 30 and month == 9) or ( month == 10 and day >= 1 and day <= 23):
   print("Знак зодиака:Весы")

elif (day >= 24 and day <= 31 and month == 10) or( month == 11 and day >= 1 and day <= 22):
   print("Знак зодиака:Скорпион")

elif (day >= 23 and day <= 30 and month == 11) or( month==12 and day >= 1 and day <= 21):
   print("Знак зодиака:Стрелец")

elif (day >= 22 and day <= 31 and month == 12) or( month == 1 and day >= 1 and day <= 20):
   print("Знак зодиака:Козерог")

elif (21 <= day <= 31 and month == 1) or(month == 2 and day >= 1 and day <= 18):
   print("Знак зодиака:Водолей")

elif (day >= 19 and day <= 29 and month == 2) or( month == 3 and day >= 1 and day <= 20):
   print("Знак зодиака:Рыбы")



"""

Task 4 
Вам нужно написать программу для подбора упаковок по размерам товара. 
Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):

"""


width = 15
length = 50
height = 15

if width <= 15 and length <= 15 and height <= 15:
    print("Ищем коробку номер 1")
elif (15 < width < 50) or (15 < length < 50) or (15 < height < 50):
    print("Ищем коробку номер 2")
elif length > 200:
    print("Ищем коробку для лыж")
else:
    print("Стандартная коробка номер 3")

"""
Task 5

Дана переменная, в которой хранится шестизначное число (номер проездного билета). 
Напишите программу, которая будет определять, является ли данный билет “счастливым”.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера.
"""

ticket_number = 123321
ticket_number = str(ticket_number)
n = 3
chunks = [ticket_number[i:i+n] for i in range(0, len(ticket_number), n)]
print(chunks)
if chunks[0] == chunks[1][::-1]:
    print("Счастливый билет")
else:
    print("Несчастливый билет")

"""
Task 6
Напишите программу, которая сможет вычислять площади трех фигур (круг, треугольник и прямоугольник). 
Тип фигуры запрашиваем через пользовательский ввод, после чего делаем запрос характеристик фигуры:

"""

import math

figure = input("Введите название фигуры: ")
if figure == 'Треугольник' or figure == 'треугольник':
    a = int(input("Введите первую сторону: "))
    b = int(input("Введите вторую сторону: "))
    c = int(input("Введите третью сторону: "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(s)
elif figure == 'Круг' or figure == 'круг':
    r = int(input("Введите радиус круга: "))
    s = 3.14 * (r**2)
    print(s)
elif figure == 'Прямоугольник' or figure == 'прямоугольник':
    a = int(input("Введите длину: "))
    b = int(input("Введите ширину: "))
    s = a * b
    print(s)
else:
    print("Других фигур не знаю сори")