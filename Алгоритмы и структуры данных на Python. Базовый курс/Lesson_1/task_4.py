#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a=input("Введите первое число 'a' : ")
b=input("Введите второе число 'b' : ")
c=input("Введите третье число 'с' : ")

if a>c>b:
    print(c)
elif c>a>b:
    print(a)
else:
    print(b)