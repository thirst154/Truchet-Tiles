import pygame as pg
from random import shuffle, randint

WIDTH = HEIGHT = 1000
SCL = 100
screen = pg.display.set_mode([WIDTH, HEIGHT])
colors = ["#F20530", "#0477BF", "#51A65E", "#F2B705"]

tiles = [ #4 triangles each rotated 90 deg
    lambda x, y, scl: [[x, y], [x, y + scl], [x + scl, y]],
    lambda x, y, scl: [[x + scl, y], [x, y], [x + scl, y + scl]],
    lambda x, y, scl: [[x + scl, y + scl], [x, y + scl], [x + scl, y]], 
    lambda x, y, scl: [[x, y + scl], [x, y], [x + scl, y + scl]],
]

grid = [[randint(0, len(tiles)-1) for w in range(WIDTH // SCL)] for h in range(HEIGHT // SCL)]

def loop():
    screen.fill("#F2F2F2")
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    #pg.draw.circle(screen, colors, (WIDTH // 2, HEIGHT // 2), 500)
    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            pg.draw.rect(screen, (255, 255, 255), (x * SCL, y * SCL, SCL, SCL), 1)

            pg.draw.polygon(screen, colors[tile], tiles[tile](x * SCL, y * SCL, SCL))

    pg.display.flip()


if __name__ == "__main__":
    loop()
    pg.image.save(screen, 'image.png')
