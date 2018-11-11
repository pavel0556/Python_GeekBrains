# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil
first_file = ()
backup_file = ()

def copy_file(first_file,backup_file):
    try:
        first_file = input("Введите путь копируемого файла: ")
        backup_file = input("Укажите путь куда нужно скопировать файл: ")
        shutil.copy(first_file,backup_file)
    except:
        FileNotFoundError
        print("Указанный пусть не найдён")

copy_file(first_file,backup_file)
