import pgzrun
import random

TITLE = "bee_game"
HEIGHT = 400
WIDTH = 400

score = 0

game_over = False

bee = Actor("bee")
bee.pos = (100,100) #(x,y)

flower = Actor("flower")
flower.pos = (200,200)

def draw():  # renders everything
    screen.blit("background", (0,0))
    bee.draw()
    flower.draw()

    screen.draw.text( "Score: " + str(score), (10,10), color = "white")

    if game_over:
        screen.clear()
        screen.fill("skyblue")
        screen.draw.text("Game Over! Your final score is:" + str(score), midtop = (200,200), color = "white" )


def touch_move():
    flower.x = random.randint(50,350)
    flower.y = random.randint(50, 350)

def update():  # runs constantly
    global score
    if keyboard.a:
        bee.x = bee.x-2
    if keyboard.d:
        bee.x = bee.x+2
    if keyboard.w:
        bee.y = bee.y-2
    if keyboard.s:
        bee.y = bee.y+2

    if bee.colliderect(flower):
        touch_move()
        score = score + 10

def time_up():
    global game_over
    game_over = True


touch_move()
clock.schedule(time_up,60.0) # stops automatically
pgzrun.go()
