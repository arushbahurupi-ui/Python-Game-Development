import pgzrun
from pgzhelper import *
import random


TITLE = "Collect the fruit!"
HEIGHT = 1000
WIDTH = 1000

game_over = False
score = 0


basket = Actor("subject")


fruitcol = ["apple","banana","fruit", "grapes", "watermelon", "pears"]

fruits = []
bombs = []


basket.pos = (500,800)

def create():

    fruit = Actor(random.choice(fruitcol))
    fruit.x = random.randint(50,1000)
    fruit.y = 200
    fruits.append(fruit)
    clock.schedule(create, random.randint(1, 3))
def createb():
    bomb = Actor("bomb")
    bomb.x = random.randint(50, 1000)
    bomb.y = 200
    clock.schedule(createb, random.randint(4, 7))
    bombs.append(bomb)

def draw():
    screen.blit("trees", (0, 0))
    for fruit in fruits:
        fruit.draw()
    for bomb in bombs:
        bomb.draw()
    basket.draw()
    screen.draw.text("Score: " + str(score), (10, 10), color="white")
    if game_over:
        screen.clear()

        screen.draw.text("Game Over! Your final score is:" + str(score), midtop = (500,500), color = "white" )

def update():  # runs constantly
    global score
    if keyboard.a:
        basket.x = basket.x-6
    if keyboard.d:
        basket.x = basket.x+6
    for fruit in fruits :
        fruit.y = fruit.y + 6
        if fruit.y >= 900:
            fruit.y = 0
        if basket.colliderect(fruit):
            score = score + 1
            fruits.remove(fruit)
    for bomb in bombs :
        bomb.y = bomb.y + 6
        if bomb.y >= 900:
            bomb.y = 0
        if basket.colliderect(bomb):
            score = score - 1
            bombs.remove(bomb)


def time_up():
    global game_over
    game_over = True

hide_mouse()
create()
createb()
clock.schedule(time_up,30.0)
pgzrun.go()