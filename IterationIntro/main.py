# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------- ОПЕРАЦИИ НАД ПЕРЕМЕННЫМИ ------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# сложение, вычитаение, умножение, деление
a = 10
b = 10

# print("сложение:", a+b)             # сложение
# print("вычитаение:", a-b)           # вычитаение
# print('умножение:', a*b)            # умножение
# print('деление:', a/b)              # деление

# print('остаток при делении:', a%b)  # остаток при делении
# print('6'*3)       # string умножается на цифру! осторожно!

# сравнение
# print(a == b)   # ровно
# print(a != b)   # не равно
# print(a < b)    # а меньше, чем b
# print(a > b)    # а больше, чем b
# print(a <= b)   # а меньше, или ровно b
# print(a >= b)    # а больше, или ровно b

# логические "и", "или"
color1 = 'red'
color2 = 'red'

# print('логическое и:', (a == b) & (color1 == color2))
# print('логическое или:', (a == b) | (color1 == color2))

# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------- IF - ELIF - ELSE --------------------------------------------------
# ------------------------------------------------------------------------------------------------------------
# print('Введите ваш возраст:')
# age = int(input())

# if age < 18:
#    print('вы еще ребенок')
# elif 18 <= age < 63:
#    print('вы уже взрослый')
# elif 63 <= age < 80:
#    print('вы уже старый')
# else:
#    print('вы уже древний')

# ------------------------------------------------------------------------------------------------------------
# ---------------------------------------- FOR AND WHILE -----------------------------------------------------
# ------------------------------------------------------------------------------------------------------------

# Напишите программу, выводящую на экран значения 12, 23 и 55
# print(12)
# print(23)
# print(55)

myList = [12, 23, 55, 65, 89]

# for, break, continue
# for number in myList:
#    if number == 55:
#        continue
#    print(number)

length = 0

while length < 6:
    print(length)
    length = length + 1


# Упражнение: 1. Создать list с наиминованиями языков программирования.
#             2. Написать программу, которая методом перебора ищет значение Pyhton, и найдя его выводит на экран
#                "Pyhton очень красивый".
#             3. Дописать программу таким образом, чтобы для языков С, С++ был вывод "Почти как Pyhton, тоже красивый".


