# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
import random
# Заполняем список произвольными целыми числами
lst_gr = []
le = int(input('Enter list lenght le: '))
lr = int(input('Enter list low range +-lr: '))
hr = int(input('Enter list high range +-hr: '))

lst_gr = [random.randint(lr, hr) for _ in range(le)]
print('lst_gr = ', lst_gr)
lst_p2 = [x**2 for x in lst_gr]
print('lst_p2 = ', lst_p2)
# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
fruits1 = ['абрикос', 'апельсин', 'арбуз', 'банан', 'груша', 'дыня', 'лимон', 'манго', 'маракуйя', 'персик', 'слива', 'фейхоа', 'черешня']
fruits2 = ['абрикос', 'авокадо', 'виноград', 'груша', 'дыня', 'лайм', 'манго', 'нектарин', 'слива', 'черешня']

fruits3 = list(set(fruits1) & set(fruits2))
fruits3.sort()

print('fruits1 = ', fruits1)
print('fruits2 = ', fruits2)
print('fruits3 = ', fruits3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
# Заполняем список произвольными целыми числами
lst_gr = []
le = int(input('Enter list lenght le: '))
lr = int(input('Enter list low range +-lr: '))
hr = int(input('Enter list high range +-hr: '))

lst_gr = [random.randint(lr, hr) for _ in range(le)]
print('lst_gr = ', lst_gr)
lst_valid = [x for x in lst_gr if x>0 and x%3==0 and x%4!=0]
print('lst_valid = ', lst_valid)
