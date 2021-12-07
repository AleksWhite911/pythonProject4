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