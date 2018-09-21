# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def cp_file():
#   cp <file_name> - создает копию указанного файла
    src = os.path.join(os.getcwd(), dir_name)
    print(src)
    try:
        dst_dir = os.path.join(os.getcwd(), 'temp')
        print(dst_dir)
        shutil.copy2(src, dst_dir)
    except Exception:
        print('Ошибка при копировании!')

def rm_file():
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
    print("Вы хотите удалить файл {}?".format(dir_name))
    yes_no = input("Наберите 'y'-да, 'n'-нет: ")
    if yes_no == 'y':
        try:
            os.remove(dir_name)
        except Exception:
            print('Ошибка при удалении!')

def ch_dir():
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
    if os.path.isabs(dir_name):
        try:
            os.chdir(dir_name)
            print(dir_name)
        except Exception:
            print('Ошибка при переходе!')
    else:
        try:
            os.chdir(os.path.join(os.getcwd(), dir_name))
        except Exception:
            print('Ошибка при переходе!')

def ls_dir():
#   ls - отображение полного пути текущей директории
    print(os.path.abspath(os.getcwd()))

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": cp_file,
    "rm": rm_file,
    "cd": ch_dir,
    "ls": ls_dir
    
}

try:
    dir_name = sys.argv[2]
    print(dir_name)
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
