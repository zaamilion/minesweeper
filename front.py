def print_desk(desk):
    slots = desk.slots
    print('┌', ('-----' * len(slots)), '┐')
    for line in slots:
        print('| ', end='')
        for slot in line:
            print(f'[{slot}]', end=' ')
        print(' |')
    print('└', ('-----' * len(slots)), '┘')

def print_desk_opened(desk):
    slots = desk.slots
    print('┌', ('-----' * len(slots)), '┐')
    for line in slots:
        print('| ', end='')
        for slot in line:
            print(f'[{slot.back_symb}]', end=' ')
        print(' |')
    print('└', ('-----' * len(slots)), '┘')