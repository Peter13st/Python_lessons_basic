# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
fruits = ["груша", "яблоко", "слива", "банан", "киви", "дыня", "арбуз"]
i=1
for fruit in fruits:
    print('{0:d}.{1:>10}'.format(i, fruit))
    i+=1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
lst1 = ['q','w','e','r','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
print('list before removing:', lst1)
lst2 = ['p','k','n','g','r','d','z']
print('removing these items:', lst2)
for li in lst1:
    if li in lst2:
        lst1.remove(li)
print('list after removing:', lst1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
numint1 = [48,939,23565,23,9948,26,80,13,800,23551,736]
numint2 = []
for lnum in numint1:
    if lnum % 2 == 0:
        numint2.append(lnum / 4)
    else:
        numint2.append(lnum * 2)
print('first list:', numint1)
print('second list:', numint2)
