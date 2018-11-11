import os
import shutil

def copy_file(first_file,backup_file): #копирование файла
    try:
        first_file = input("Введите путь копируемого файла: ")
        backup_file = input("Укажите путь куда нужно скопировать файл: ")
        shutil.copy(first_file,backup_file)
    except:
        FileNotFoundError
        print("Указанный пусть не найдён")

def new_directory (name,number): #создание новой директории
    name = input("Введите название директории - ")
    number = int(input("Введите кол-во новых директорий - "))
    try:
        for i in range(1,number):
            os.makedirs("{}//{}_{}".format(os.getcwd(),name,i))
    except:
        FileExistsError
        print("Директория уже существует")


def delete_directory (name): #удаление директории
    try:
        name = input("Укажие полный пусть удаляемой папки")
        os.rmdir(name)
        print("Папка удалена")
    except:
        FileNotFoundError
        print("Такой папки нет")


def list_dir(main_path): #отображение созданных папок
    main_path = input("Введите путь директории: ")
    for i in os.listdir(main_path):
        if os.path.isfile(i) == False:
            print(i)
        else:
            continue