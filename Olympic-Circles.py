import pgzrun
HEIGHT = 1000
WIDTH = 1000

def draw():
    screen.fill("white")
    colors = ["blue", "black", "red"]
    color1 = ["yellow", "green",]
    x = 250
    y = 300
    for i in range(3):
        screen.draw.circle((x,y),100,colors[i],)
        x = x + 190


    a = 355
    b = 405
    for i in range(2):
        screen.draw.circle((a,b),100,color1[i])
        a = a + 170




pgzrun.go()