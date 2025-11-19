import pgzrun
import random

TITLE = "Shooting Star"
HEIGHT = 1000
WIDTH = 1000

star = Actor("star")
star2 = Actor("star")

starslist = [Actor("star"),Actor("star")]

for stars in starslist:
    stars.x = random.randint(0, 1000)


def draw():
    screen.blit("backgroundg",(0,0))

    for star in starslist:
        star.draw()

def update():

    for star in starslist:
        star.x = star.x -3
        star.y = star.y + 3







pgzrun.go()