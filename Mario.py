import pgzrun
import random
import time

HEIGHT = 1000
WIDTH = 1000



def randcoor():
    mario.x = random.randint(10,800)
    mario.y = random.randint(10,800)

score = 0

def on_mouse_down(pos):
    if mario.collidepoint(pos):
        global score
        score = score +1
        randcoor()



mario = Actor("mario")
mario.pos = (500,500)


def draw():
    screen.clear()
    mario.draw()
    screen.draw.text("Your score is: " + str(score), (50, 30), color="white")

def update():
    randcoor()
    time.sleep(0.5)






randcoor()
pgzrun.go()

