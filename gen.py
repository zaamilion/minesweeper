import random
from back import *
from front import print_desk


def gen_desk(width, height, quantity_of_bombs, first_step):
    slots = [[Slot(bomb=False) for _ in range(width)] for _ in range(height)]
    desk = Desk(
        height=height, width=width, quantity_of_bombs=quantity_of_bombs, slots=slots
    )
    bombs_xy = set(
        [random.randint(0, height * width - 1) for _ in range(quantity_of_bombs)]
    )
    directions = [
        (i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)
    ]
    bombs_xy.discard(first_step[0] + first_step[1] * len(desk.slots))
    real_quantity = 0
    for bomb_xy in bombs_xy:
        bomb_x = bomb_xy % height
        bomb_y = bomb_xy // height
        desk.slots[bomb_x][bomb_y].to_bomb()
        real_quantity += 1
    for bomb_xy in bombs_xy:
        bomb_x = bomb_xy % height
        bomb_y = bomb_xy // height
        for i, j in directions:
            try:
                if bomb_x + i < 0 or bomb_y + j < 0:
                    continue
                if desk.slots[bomb_x + i][bomb_y + j].bomb is False:
                    if desk.slots[bomb_x + i][bomb_y + j].is_counter is False:
                        desk.slots[bomb_x + i][bomb_y + j].to_counter()
                    desk.slots[bomb_x + i][bomb_y + j].counter_plus()
            except IndexError:
                pass
    return (desk, real_quantity)
