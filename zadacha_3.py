# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# 
# Пример:
# 
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

def udalenie_celogo(x):
    for i in range(len(x)):
        b = str(x[i])
        d = b.split('.')
        if len(d) != 2:
            d.append('0')
        c = '0.' + d[1]
        x[i] = float(c)
    return x

def poisk_null(x):
    coll = 0

    for i in x:
        if i == 0.0:
            coll+=1
    
    for i in range(coll):
        x.remove(0.0)
    
    return x

def raznitca(x):
    min = x[0]
    max = x[0]
    for i in x:
        if i < min:
            min = i
        elif i > max:
            max = i
    print(f'{max} - {min} = {max - min}')


spisok = [1.1, 1.2, 3.1, 5, 6, 10.01]
spisok = udalenie_celogo(spisok)
spisok = poisk_null(spisok)
raznitca(spisok)


