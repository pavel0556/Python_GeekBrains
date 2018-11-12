#Шушвар П.В.
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
main_path = ()

def list_dir(main_path):
    main_path = input("Введите путь директории: ")
    for i in os.listdir(main_path):
        if os.path.isfile(i) == False:
            print(i)
        else:
            continue


print(list_dir(main_path))