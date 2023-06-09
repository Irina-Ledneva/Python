'''
Задача 11
Дано натуральное число A > 1. Определите,
каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.

Input:     5

Output:  6
'''

# 0 1 1 2 3 5 8 13 21 34
num = int(input('Введите число Фибоначи: '))
fib1 = 0
fib2 = 1
count = 2

for i in range(num + 1):
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    count += 1
    if fib3 == num:
        print(f'Число: {num} является {count} числом Фибоначи')
        break
    elif fib3 > num:
        print(f'Число: {num} не является числом Фибоначи')
        break
