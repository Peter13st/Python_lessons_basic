# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
seq = equation.strip()
posx = seq.find('x')
startk = seq.rfind(' ',0,posx)+1
k = float(seq[startk:posx])
startb = seq.rfind(' ',posx)+1
b = float(seq[startb:])
y = k * x + b
print(equation)
print('x = ',x)
print('y = ',y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
# date = '01.11.1985'

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
date = input('Введите дату в виде строки формата "dd.mm.yyyy": ')
try:
    dl = date.split('.')
    if len(dl[0]) == 2 and len(dl[1]) == 2 and len(dl[2]) == 4:
        if dl[0].isdigit() and dl[1].isdigit() and dl[2].isdigit():
            dd = int(dl[0])
            mm = int(dl[1])
            yyyy = int(dl[2])
            if 1 < yyyy <= 9999 and 1 < mm <= 12:
                if (mm in (1, 3, 5, 7, 8, 10, 12) and 1 < dd <= 31) or (mm in (2, 4, 6, 9, 11) and 1 < dd <= 30):
                    print('Дата выглядит корректно!')
                else:
                    print('Несоответствие чисел и месяцев!')
            else:
                print('Год меньше 1 или больше 9999!')
        else:
            print('Введенная дата содержит не только цифры!')
    else:
        print('Введенная дата не в виде строки формата "dd.mm.yyyy"!')
except:
    print('Ошибка при вводе даты!')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
