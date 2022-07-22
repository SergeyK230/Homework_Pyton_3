# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# 
# Пример:
# 
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def nega_fibo(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return nega_fibo(n + 2) - nega_fibo(n + 1)



k = int(input('Введите число -> '))
fib = []
for i in range(-k,k+1):
    if i < 0:
        fib.append(nega_fibo(i))
    elif i == 0:
        fib.append(0)
    else:fib.append(fibo(i))

print(fib)

