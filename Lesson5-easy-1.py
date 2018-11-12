#Шушвар П.В.
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
name = ()
number = []

def new_directory (name,number):
    name = input("Введите название директории - ")
    number = int(input("Введите кол-во новых директорий - "))
    try:
        for i in range(1,number):
            os.makedirs("{}//{}_{}".format(os.getcwd(),name,i))
    except:
        FileExistsError
        print("Директория уже существует")

print (new_directory(name,number))




# Удаление созданных директорий
def delete_directory (name):
    try:
        name = input("Укажие полный пусть удаляемой папки")
        os.rmdir(name)
        print("Папка удалена")
    except:
        FileNotFoundError
        print("Такой папки нет")


print(delete_directory(name))
