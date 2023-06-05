"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

5 -> 1 0 1 1 0
2
"""

coin = int(input('Сколько монет лежит на столе: '))
reverse = 0
for i in range(coin):
    side = int(input('Стороны монет: '))
    if side == 1:
        reverse += 1
print(f'Необходимо перевернуть {reverse if reverse < coin / 2 else coin - reverse} монеты')
