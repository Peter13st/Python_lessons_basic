# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

fract_str = input('enter fraction operation "n x/y +- k m/s": ')
fr_lst = fract_str.split(' ')

if fr_lst.count('+') == 1:
    ops_indx = fr_lst.index('+')
    ops = 'add'

elif fr_lst.count('-') == 1:
    ops_indx = fr_lst.index('-')
    ops = 'subtract'

leftfr_int = '0'
leftfr_up = '0'
leftfr_lo = '1'
rightfr_int = '0'
rightfr_up = '0'
rightfr_lo = '1'

i = 0

while i < ops_indx:
    if fr_lst[i].count('/') == 1:
        leftfr_up = (fr_lst[i].split('/'))[0]
        leftfr_lo = (fr_lst[i].split('/'))[1]
    elif fr_lst[i].count('/') == 0:
        leftfr_int = fr_lst[i]
    i += 1

i = ops_indx + 1

while i < len(fr_lst):
    if fr_lst[i].count('/') == 1:
        rightfr_up = (fr_lst[i].split('/'))[0]
        rightfr_lo = (fr_lst[i].split('/'))[1]
    elif fr_lst[i].count('/') == 0:
        rightfr_int = fr_lst[i]
    i += 1


intp = 0
frup = 0
frlo = 1

dleftfr_int = int(leftfr_int)
dleftfr_up = int(leftfr_up)
dleftfr_lo = int(leftfr_lo)
drightfr_int = int(rightfr_int)
drightfr_up = int(rightfr_up)
drightfr_lo = int(rightfr_lo)
if dleftfr_int <0:
    dleftfr_up = -dleftfr_up
if drightfr_int <0:
    drightfr_up = -drightfr_up


if ops == 'add':
    intp = dleftfr_int + drightfr_int
    frlo = dleftfr_lo * drightfr_lo
    frup = dleftfr_up * drightfr_lo + drightfr_up * dleftfr_lo
    intp2 = frup // frlo
    frup2 = frup % frlo
    intp = intp + intp2
    print(intp, frup2, frlo)
    if frup2 != 0 or frlo != 1:
        outfr = '{} {}/{}'.format(intp, frup2, frlo)
    elif frup2 != 0 and frlo == 1:
        intp = intp + frup
        outfr = '{}'.format(intp)
    elif frup2 == 0:
        outfr = '{}'.format(intp)
        
elif ops == 'subtract':
    intp = dleftfr_int - drightfr_int
    frlo = dleftfr_lo * drightfr_lo
    frup = dleftfr_up * drightfr_lo - drightfr_up * dleftfr_lo
    intp2 = frup // frlo
    frup2 = frup % frlo
    intp = intp + intp2
    if frup2 != 0 or frlo != 1:
        outfr = '{} {}/{}'.format(intp, frup2, frlo)
    elif frup2 != 0 and frlo == 1:
        intp = intp + frup
        outfr = '{}'.format(intp)
    elif frup2 == 0:
        outfr = '{}'.format(intp)

print('Output: ',outfr)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
