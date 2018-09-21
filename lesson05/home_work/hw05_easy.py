# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Petr O.
#script1
import os
for i in range(9):
    dir_i = 'dir_'+str(i+1)
    dir_path = os.path.join(os.getcwd(), dir_i)
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

#script2
import os
for i in range(9):
    dir_i = 'dir_'+str(i+1)
    dir_path = os.path.join(os.getcwd(), dir_i)
    try:
        print('директория удаляется: ', dir_i)
        os.rmdir(dir_path) #- удаляет пустую директорию.
    except Exception:
       print('Такая директория не удаляется')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
dir_path = os.path.join(os.getcwd())
dirlist = [filename for filename in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path,filename))]
print(dirlist)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
dir_path = os.getcwd()
srcfile = os.path.realpath(__file__)
dir_name = 'my_fcopy'
destdir = dir_path + '\\' + dir_name
try:
    os.makedirs(dir_name)
except Exception:
    print('directory exists!')
shutil.copy(srcfile, destdir)
