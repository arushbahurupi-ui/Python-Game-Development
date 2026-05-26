import pgzrun
import random

HEIGHT = 900
WIDTH = 1000


player = Actor("spaceship##")
player.y = 800
player.x = 500

boss = Actor("boss")
boss.x = 500
boss.y = 200


listeny = []
laserlist = []
listenylaser = []
heartlist = []

speedx = -70
cooldown_max = 25
score = 0
hearts = 5
gameover = False
gameover1 = False
bosscooldown = False
boss_health = 25


def draw():
    if gameover:
        screen.blit("gameoverscreen",(0,0))
        return
    if gameover1:
        screen.blit("gameover1screen",(0,0))
        return
    screen.blit("spaceback",(0,0))
    screen.draw.text("Score: " + str(score), center = (80, 860), fontsize = 50)
    screen.draw.text("Hearts: " + str(hearts), center =(900, 860), fontsize=50)
    player.draw()
    for beem in laserlist:
        beem.draw()
    if bosscooldown == False:
        for enemy in listeny:
            enemy.draw()
    for beem in listenylaser:
        beem.draw()
    if bosscooldown:
        boss.draw()
    for heart in heartlist:
        heart.draw()


def update():

    global speedx
    global cooldown_max
    global hearts
    global gameover
    global gameover1
    global bosscooldown
    global boss_health
    global score


    if score == 50 and bosscooldown == False:
        bosscooldown = True
        shootboss()
    if cooldown_max > 0:
        cooldown_max -= 1
    if keyboard.d:
        player.x +=  6
    if keyboard.a:
        player.x -=  6
    if keyboard.space and cooldown_max == 0:
        shoot()
        cooldown_max = cooldown_max + 25

    for enemy in listeny:
        if enemy.colliderect(player):
            hearts -= 1
            listeny.remove(enemy)
        enemy.y +=  1.1
        for beem in laserlist:
            if beem.colliderect(enemy):
                listeny.remove(enemy)
                laserlist.remove(beem)
                score += 1


    for beem in laserlist:
        beem.y += -7.2

    for beem in laserlist:
        if beem.colliderect(boss):
            laserlist.remove(beem)
            score += 1
            boss_health -= 1

    for beem in listenylaser:
        beem.y += 10.2
        if beem.colliderect(player):
            listenylaser.remove(beem)
            hearts -= 1
    if hearts <= 0:
        gameover = True
    if boss_health <= 0:
        gameover1 = True

    if bosscooldown:
        boss.y += 0.25
        boss.x += random.randint(-2,2)
    if boss.y == 600:
        boss.y = 200
    for heart in heartlist:
        heart.y += 6
        if heart.colliderect(player):
            hearts += 1
            heartlist.remove(heart)
        if heart.y == 880:
            heartlist.remove(heart)





def shoot():
    beem = Actor("laserspace")
    beem.centerx = player.centerx
    beem.bottom = player.top
    laserlist.append(beem)

def shootenemy():
    if not bosscooldown:
        beem = Actor("enemylaser")
        enemylocal = random.choice(listeny)
        beem.centerx = enemylocal.centerx
        beem.top = enemylocal.bottom
        listenylaser.append(beem)
        clock.schedule(shootenemy,0.5)

def shootboss():
    beem = Actor("enemylaser")
    beem.centerx = boss.centerx + random.randint(-80,80)
    beem.top = boss.bottom
    listenylaser.append(beem)
    clock.schedule(shootboss, 0.5)


def create() :
    if not bosscooldown:
        for i in range(1,8):
            enemy = Actor("enemy")
            enemy.y = 100
            enemy.x = i * 125
            listeny.append(enemy)
        clock.schedule(create,5)


def createheart():
    heart = Actor("heart")
    heart.y = 100
    heart.x = random.randint(100,1000)
    heartlist.append(heart)
    clock.schedule(createheart,random.randint(17,27))

clock.schedule(shootenemy,0.5)
create()
clock.schedule(createheart,40)
pgzrun.go()