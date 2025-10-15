import pgzrun
HEIGHT = 1000
WIDTH = 1000


def draw():
    screen.fill((162,220,213))
    rectangle = Rect((0,0),(600,600))
    x = 500
    y = 500
    for i in range(3):
        x = x - 20
        y = y - 20
        rectangle.center = (x,y)
        screen.draw.rect(rectangle, "blue")
    rectangle = Rect((0, 0), (200, 200))
    x = 500
    y = 500
    for i in range(3):
        x = x - 20
        y = y - 20
        rectangle.center = (x, y)
        screen.draw.filled_rect(rectangle, "blue")
    screen.draw.text("Hello World!", center = (500,500), color = "skyblue", fontsize = 50)


pgzrun.go()