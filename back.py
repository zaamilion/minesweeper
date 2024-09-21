class Slot:
    def __init__(self, bomb):
        self.flag = False
        self.opened = False
        self.bomb = False
        self.is_counter = True
        self.counter = 0
        self.back_symb = '0'
        self.symb = '  '
    def to_bomb(self):
        self.is_counter = False
        self.bomb = True
        self.back_symb = '💣'
    def to_counter(self):
        self.is_counter = True
        self.back_symb = self.counter
    def counter_plus(self):
        self.counter += 1
        self.back_symb = self.counter
    def open(self):
        self.opened = True
        self.symb = self.back_symb
    def __repr__(self):
        if self.is_counter is True and self.opened is True:
            return str(self.symb) + ' '
        return str(self.symb) 
    

class Desk:
    def __init__(self, height, width, quantity_of_bombs, slots):
        self.height = height
        self.width = width
        self.quantity_of_bombs = quantity_of_bombs
        self.slots = slots

def open_around(desk, x,y, checked=[]):
    if (x,y) in checked:
        return True
    checked.append((x,y))
    if desk.slots[x][y].counter == 0 and desk.slots[x][y].is_counter == True:
        desk.slots[x][y].open()
        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
        for i, j in directions:
            try:
                if x + i < 0 or y + j < 0:
                    continue
                open_around(desk, x+i, y+j, checked)
            except IndexError:
                pass
    else:
        return True