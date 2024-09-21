from gen import gen_desk
from front import print_desk, print_desk_opened
from back import *

def main():
    desk_size = int(input('Введите размер стола (int): '))
    quantity_of_bombs = int(input('Введите количество бомб (int): '))
    print('Все ходы имеют вид : x y')
    first_step = list(map(int, input('Сделайте свой первый ход: ').split()))
    x = first_step[1]
    y = first_step[0]
    desk = gen_desk(desk_size, desk_size, quantity_of_bombs, first_step)
    desk.slots[x][y].open()
    open_around(desk, x,y)
    print_desk(desk)

main()