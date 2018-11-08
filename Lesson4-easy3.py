# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

import random
lst = []
lst = [random.randint(-20,20) for _ in range (20)]
kratno = []
kratno.append([i for i in lst if i%3 == 0]) #добавляем в список числа кратные 3
print(kratno)
nekratno = []
nekratno.append([i for i in lst if i%4 != 0]) # добавляем в список числа не кратные 4
print(nekratno)
poloj = []
poloj.append([i for i in lst if i > 0]) #добавляем в список положительные числа
print(poloj)




