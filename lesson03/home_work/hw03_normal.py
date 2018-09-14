# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 0
    b = 1
    if n < 2:
        print('fib1: {}'.format(b), end=' ')
    for i in range(2, m + 1):
        c = a + b
        a, b = b, c
        if i >= n:
            print('fib({}): {}'.format(i, c), end=' ')
try:
    n = int(input('Enter n: '))
    m = int(input('Enter m: '))
    if n <= m:
        fibonacci(n, m)
    else:
        print('n > m: not solved')
except:
    print('data error')

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list)):
        for j in range(len(origin_list) - 1, i, -1):
            if origin_list[j] < origin_list[j-1]:
                origin_list[j], origin_list[j-1] = origin_list[j-1], origin_list[j]

    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def is_parallelogramm(x1,y1,x2,y2,x3,y3,x4,y4):
    if (x2-x1 == x3-x4) and (y1-y4 == y2-y3):
        print("It's parallelogramm!")
    else:
        print("It's not a parallelogramm!")
try:
    x1 = int(input('enter A1(x1):'))
    y1 = int(input('enter A1(y1):'))
    x2 = int(input('enter A2(x2):'))
    y2 = int(input('enter A2(y2):'))
    x3 = int(input('enter A3(x3):'))
    y3 = int(input('enter A3(y3):'))
    x4 = int(input('enter A4(x4):'))
    y4 = int(input('enter A4(y4):'))
except ValueError:
    print('input error!')

is_parallelogramm(x1,y1,x2,y2,x3,y3,x4,y4)
