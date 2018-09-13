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

