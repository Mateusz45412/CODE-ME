def field():
    for c in CELLS:
        if c[1] in (0, WIDTH - 1) or c[0] in (0, HEIGHT - 1):
            print('#', end='')
        else:
            print(' ', end='')
        if c[1] == WIDTH-1:
            print('')
WIDTH = 12
HEIGHT = 6
CELLS = [(h, w) for h in range(HEIGHT) for w in range(WIDTH)]
item_pos = (4, 5)
field()
