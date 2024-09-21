from gen import gen_desk
from front import print_desk, print_desk_opened
from back import *
import itertools


def main():
    game = True
    desk_size = int(input("Введите размер стола (int): "))
    quantity_of_bombs = int(input("Введите количество бомб (int): "))
    print("Все ходы имеют вид : x y")
    first_step = list(map(int, input("Сделайте свой первый ход: ").split()))
    x = first_step[0]
    y = first_step[1]
    desk, real_quantity = gen_desk(desk_size, desk_size, quantity_of_bombs, first_step)
    desk.slots[x][y].open()
    open_around(desk, x, y)
    print_desk(desk)
    # сразу открытое поле (чекнуть генерацию)
    # print_desk_opened(desk)
    while game is True:
        step = list(map(int, input("Ваш ход: ").split()))
        x = step[0]
        y = step[1]
        desk.slots[x][y].open()
        if desk.slots[x][y].bomb is True:
            print("ю луз бомб хере")
            print_desk_opened(desk)
            game = False
            break
        open_around(desk, x, y)
        print_desk(desk)
        all_slots = list(itertools.chain.from_iterable(desk.slots))
        if all_slots.count("  ") == real_quantity:
            print("Ты выиграаал")
            print_desk_opened(desk)
            game = False


print("Игра закончена")


main()
