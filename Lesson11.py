
from random import randint
from gfunction import *


start_game="Начинаем"
print("игра запущена")

while g_comand(start_game) == True:
    print(f"{start_game} игру. Задайте диапазон, в котором будет задано натуральное число.")
    min_n = int(input("Введите минимальное значение диапазона"))
    max_n = int(input("Введите максимальное значение диапазона"))
    num = randint(min_n, max_n)
    g_num(num, start_game)
else:
    print("Game Over")

