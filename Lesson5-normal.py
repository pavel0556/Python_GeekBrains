# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os
import easy.py

i = int(input("Введите значение"))
if i == 1:
    print("Ваша текущая директория",os.getcwd())
    a = input("Введите полный путь к папки: ")
    print("Ваша директория изменена на:",a)
elif i == 2:
    print("Содержимое папки :",easy.list_dir(a))
elif i == 3:
    easy.delete_directory(name)
elif i == 4:
    easy.new_directory(name, number)
else:
    print("Проверьте правельность ввода")
