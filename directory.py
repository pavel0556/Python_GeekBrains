# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#import os

for number in range(1,10):
    dir_path = os.path.join(os.getcwd(), "dir_")
#    os.makedirs("{}//dir_{}".format(os.getcwd(),number))
for number in range(1,10):
 #   os.rmdir("{}//dir_{}".format(os.getcwd(),number))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os

print(os.listdir(os.getcwd()))



# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.



