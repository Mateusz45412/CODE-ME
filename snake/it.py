WIDTH = 5
HEIGHT = 6
center_w = WIDTH//2
center_h = HEIGHT//2


snake_body = [(center_h, center_w)]
part_snake = (center_h, center_w + 1)

DIRECTIONS = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
direction = DIRECTIONS['right']
points = 0
CELLS = [(h, w) for h in range(HEIGHT) for w in range(WIDTH)]

def field():
    for c in CELLS:
        # if c[1] in (0, WIDTH - 1):
        if snake_body in c[0]:
            c[0]=c[-1]
field()